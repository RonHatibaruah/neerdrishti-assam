/**
 * NeerDrishti Assam - Frontend Application Logic
 * NESFIC-D-02: Irrigation Canals Condition Monitoring & Predictive Maintenance
 */

let state = {
  canals: [],
  telemetry: [],
  defects: [],
  workOrders: [],
  activeTab: 'tab-gis',
  selectedCanal: null
};

document.addEventListener('DOMContentLoaded', () => {
  fetchLatestData();
  // Poll telemetry every 10 seconds for real-time live feed
  setInterval(pollTelemetry, 10000);

  // Initialize hash-based SEO deep-linking
  initHashRouting();
  window.addEventListener('hashchange', initHashRouting);

  // Close modals on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeDispatchModal();
      closeTutorialModal();
    }
  });
});

function initHashRouting() {
  const hash = window.location.hash.toLowerCase();
  if (hash === '#tutorial') {
    openTutorialModal(false);
  } else if (hash === '#gis-digital-twin' || hash === '#gis') {
    switchTab('tab-gis', false);
  } else if (hash === '#hydraulic-mass-balance' || hash === '#hydro-loss-balance' || hash === '#balance') {
    switchTab('tab-balance', false);
  } else if (hash === '#drone-defect-matrix' || hash === '#drone-defects' || hash === '#defects') {
    switchTab('tab-defects', false);
  } else if (hash === '#predictive-work-orders' || hash === '#work-orders' || hash === '#orders') {
    switchTab('tab-orders', false);
  } else if (hash === '#breach-warning-simulation' || hash === '#breach-simulation' || hash === '#surge') {
    switchTab('tab-surge', false);
  }
}

async function fetchLatestData() {
  try {
    const [kpiRes, canalsRes, telemRes, defectRes, orderRes] = await Promise.all([
      fetch('/api/summary'),
      fetch('/api/canals'),
      fetch('/api/telemetry'),
      fetch('/api/defects'),
      fetch('/api/work-orders')
    ]);

    const kpiData = await kpiRes.json();
    const canalsData = await canalsRes.json();
    const telemData = await telemRes.json();
    const defectData = await defectRes.json();
    const orderData = await orderRes.json();

    state.canals = canalsData.canals;
    state.telemetry = telemData.nodes;
    state.defects = defectData.defects;
    state.workOrders = orderData.work_orders;

    renderKPIs(kpiData);
    renderCanalReaches();
    renderTelemetryFeed();
    renderDefectCards();
    renderWorkOrders();
    loadHydroBalance('Jamuna Irrigation Scheme');

    document.getElementById('lastSyncTime').innerText = kpiData.last_sync.split(' ')[1] + ' IST';
  } catch (err) {
    console.error('Error fetching data:', err);
  }
}

async function pollTelemetry() {
  try {
    const res = await fetch('/api/telemetry');
    const data = await res.json();
    state.telemetry = data.nodes;
    renderTelemetryFeed();
  } catch (err) {
    console.warn('Telemetry polling error:', err);
  }
}

function renderKPIs(kpis) {
  document.getElementById('kpiLength').innerHTML = `${kpis.total_monitored_length_km} <span class="text-xs font-normal text-slate-500">km</span>`;
  document.getElementById('kpiHealth').innerHTML = `${kpis.average_asset_health_index} <span class="text-xs font-normal text-slate-500">/ 100</span>`;
  document.getElementById('kpiBreaches').innerHTML = `${kpis.critical_risk_sections} <span class="text-xs font-normal text-red-500">Active</span>`;
  document.getElementById('kpiEquity').innerHTML = `${kpis.tail_end_equity_index_pct} <span class="text-xs font-normal text-slate-500">%</span>`;
  document.getElementById('kpiSaved').innerHTML = `${kpis.estimated_prevented_water_loss_mld} <span class="text-xs font-normal text-slate-500">MLD</span>`;
  document.getElementById('kpiOrders').innerHTML = `${kpis.active_maintenance_work_orders} <span class="text-xs font-normal text-slate-500">Dispatched</span>`;

  const banner = document.getElementById('breachAlertBanner');
  if (kpis.critical_risk_sections > 0) {
    banner.classList.remove('hidden');
  } else {
    banner.classList.add('hidden');
  }
}

function renderCanalReaches() {
  const container = document.getElementById('canalReachVisualizer');
  container.innerHTML = '';

  state.canals.forEach(c => {
    let healthColor = 'bg-emerald-500';
    let textColor = 'text-emerald-400';
    let borderColor = 'border-slate-800 hover:border-emerald-500';

    if (c.risk_level === 'CRITICAL') {
      healthColor = 'bg-red-600 animate-pulse';
      textColor = 'text-red-400';
      borderColor = 'border-red-900 bg-red-950/30 hover:border-red-500';
    } else if (c.risk_level === 'HIGH' || c.risk_level === 'MODERATE') {
      healthColor = 'bg-amber-500';
      textColor = 'text-amber-400';
      borderColor = 'border-amber-900/60 bg-amber-950/20 hover:border-amber-500';
    }

    const item = document.createElement('div');
    item.className = `p-3 rounded-lg border ${borderColor} transition cursor-pointer`;
    item.onclick = () => selectReach(c.id);

    item.innerHTML = `
      <div class="flex flex-wrap justify-between items-center text-xs gap-2">
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full ${healthColor}"></span>
          <span class="font-bold text-white">${c.canal_name}</span>
          <span class="text-[10px] text-slate-400 px-1.5 py-0.5 rounded bg-slate-800">RD ${c.chainage_start_km} - ${c.chainage_end_km} km</span>
        </div>
        <div class="flex items-center gap-4 text-[11px]">
          <span>Discharge: <strong class="text-sky-300 font-mono">${c.current_discharge_cusecs} cusecs</strong></span>
          <span>Pore P: <strong class="${c.pore_pressure_kpa > 40 ? 'text-red-400' : 'text-slate-300'} font-mono">${c.pore_pressure_kpa} kPa</strong></span>
          <span>AHI: <strong class="${textColor} font-mono">${c.asset_health_index}/100</strong></span>
        </div>
      </div>
      <div class="w-full bg-slate-800 h-1.5 rounded-full mt-2.5 overflow-hidden">
        <div class="${healthColor} h-1.5 rounded-full" style="width: ${c.asset_health_index}%"></div>
      </div>
      ${c.detected_defects.length > 0 ? `
        <div class="flex gap-2 mt-2">
          ${c.detected_defects.map(d => `<span class="text-[9px] bg-red-900/60 text-red-300 px-1.5 py-0.5 rounded border border-red-800">${d}</span>`).join('')}
        </div>
      ` : ''}
    `;

    container.appendChild(item);
  });
}

function selectReach(id) {
  const c = state.canals.find(x => x.id === id);
  if (!c) return;

  document.getElementById('cardTitle').innerText = c.canal_name;
  document.getElementById('cardDistrict').innerText = `District: ${c.district} • Chainage: RD ${c.chainage_start_km} to ${c.chainage_end_km} km`;
  document.getElementById('cardAhi').innerHTML = `${c.asset_health_index} <span class="text-xs font-normal">/100</span>`;
  document.getElementById('cardQ').innerHTML = `${c.current_discharge_cusecs} <span class="text-[10px] text-slate-500">cusecs</span>`;
  document.getElementById('cardDepth').innerHTML = `${c.water_level_m} <span class="text-[10px] text-slate-500">m</span>`;
  document.getElementById('cardSilt').innerHTML = `${c.silt_depth_m} <span class="text-[10px] text-slate-500">m</span>`;
  document.getElementById('cardPore').innerHTML = `${c.pore_pressure_kpa} <span class="text-[10px] text-slate-500">kPa</span>`;

  const badge = document.getElementById('cardBadge');
  if (c.risk_level === 'CRITICAL') {
    badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded bg-red-100 text-red-800 uppercase';
    badge.innerText = 'CRITICAL REACH RISK';
  } else if (c.risk_level === 'HIGH' || c.risk_level === 'MODERATE') {
    badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-800 uppercase';
    badge.innerText = 'STRESSED REACH';
  } else {
    badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 uppercase';
    badge.innerText = 'NORMAL ASSET CONDITION';
  }

  const defectCont = document.getElementById('cardDefectBadges');
  if (c.detected_defects.length > 0) {
    defectCont.innerHTML = c.detected_defects.map(d => `<span class="text-xs text-red-700 bg-red-100 px-2 py-0.5 rounded font-medium">${d}</span>`).join('');
  } else {
    defectCont.innerHTML = `<span class="text-xs text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded font-medium">No Structural Anomalies Detected</span>`;
  }
}

function renderTelemetryFeed() {
  const container = document.getElementById('telemetryFeedContainer');
  container.innerHTML = '';

  state.telemetry.forEach(node => {
    let statusBadge = '<span class="text-[9px] bg-emerald-100 text-emerald-700 px-1.5 py-0.5 rounded font-bold">ONLINE</span>';
    let border = 'border-slate-200';

    if (node.status === 'IMMINENT_BREACH_ALERT') {
      statusBadge = '<span class="text-[9px] bg-red-600 text-white px-1.5 py-0.5 rounded font-bold animate-pulse">BREACH ALERT</span>';
      border = 'border-red-300 bg-red-50/30';
    } else if (node.status === 'ALERT_SEEPAGE') {
      statusBadge = '<span class="text-[9px] bg-amber-100 text-amber-800 px-1.5 py-0.5 rounded font-bold">SEEPAGE ALERT</span>';
      border = 'border-amber-200 bg-amber-50/20';
    } else if (node.status === 'CRITICAL_DEFICIT') {
      statusBadge = '<span class="text-[9px] bg-purple-100 text-purple-800 px-1.5 py-0.5 rounded font-bold">TAIL DEFICIT</span>';
    }

    const card = document.createElement('div');
    card.className = `p-3 rounded-lg border ${border} bg-white shadow-xs text-xs space-y-1.5`;
    card.innerHTML = `
      <div class="flex justify-between items-center">
        <span class="font-bold text-slate-800 text-[11px]">${node.node_id}</span>
        ${statusBadge}
      </div>
      <p class="text-[11px] font-medium text-slate-600">${node.location_name}</p>
      <div class="grid grid-cols-2 gap-1.5 text-[10px] text-slate-500 pt-1 border-t border-slate-100">
        <div>Level: <strong class="text-slate-700 font-mono">${node.water_level_m}m</strong></div>
        <div>Flow: <strong class="text-slate-700 font-mono">${node.flow_velocity_mps} m/s</strong></div>
        <div>Pore P: <strong class="${node.pore_pressure_kpa > 40 ? 'text-red-600' : 'text-slate-700'} font-mono">${node.pore_pressure_kpa} kPa</strong></div>
        <div>Battery: <strong class="text-emerald-600 font-mono">${node.battery_pct}%</strong></div>
      </div>
      <div class="flex justify-between text-[9px] text-slate-400 pt-0.5">
        <span>Signal: ${node.signal_strength_dbm} dBm</span>
        <span>Ping: ${node.last_ping}</span>
      </div>
    `;
    container.appendChild(card);
  });
}

async function loadHydroBalance(scheme) {
  try {
    const res = await fetch(`/api/hydro-balance?scheme=${encodeURIComponent(scheme)}`);
    const data = await res.json();

    document.getElementById('mbInflow').innerHTML = `${data.inflow_headworks_cusecs} <span class="text-sm font-normal">cusecs</span>`;
    document.getElementById('mbOfftakes').innerHTML = `${data.authorized_offtakes_cusecs} <span class="text-sm font-normal">cusecs</span>`;
    document.getElementById('mbTail').innerHTML = `${data.actual_tail_delivery_cusecs} <span class="text-sm font-normal">cusecs</span>`;
    document.getElementById('mbUnaccounted').innerHTML = `${data.unaccounted_water_loss_cusecs} <span class="text-sm font-normal">cusecs</span>`;
    document.getElementById('mbLossPct').innerText = `${data.unaccounted_loss_percentage}% Total Loss Rate`;
    document.getElementById('mbEquityRatio').innerText = `${data.tail_delivery_equity_ratio}%`;
  } catch (err) {
    console.error('Error loading hydro balance:', err);
  }
}

function renderDefectCards() {
  const container = document.getElementById('defectCardsContainer');
  container.innerHTML = '';

  state.defects.forEach(d => {
    let sevBadge = 'bg-amber-100 text-amber-800';
    if (d.severity === 'CRITICAL') sevBadge = 'bg-red-100 text-red-800 font-bold';

    const card = document.createElement('div');
    card.className = 'bg-white rounded-lg border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition text-xs flex flex-col justify-between';

    card.innerHTML = `
      <div class="h-32 bg-slate-800 relative flex items-center justify-center overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-t from-slate-900 to-transparent z-10"></div>
        <div class="z-20 text-center px-4">
          <i class="fa-solid fa-camera-retro text-2xl text-slate-300 mb-1"></i>
          <p class="text-[10px] text-amber-300 font-mono tracking-wider">AI CV DETECTION BOX</p>
          <p class="text-xs text-white font-bold">${d.defect_type}</p>
        </div>
        <span class="absolute top-2 right-2 z-20 ${sevBadge} text-[9px] px-2 py-0.5 rounded uppercase">${d.severity}</span>
        <span class="absolute bottom-2 left-2 z-20 text-[10px] font-mono text-emerald-400 font-bold">Conf: ${d.confidence_pct}%</span>
      </div>

      <div class="p-4 space-y-2 flex-grow">
        <div class="flex justify-between text-[11px]">
          <span class="text-slate-500 font-mono">${d.id}</span>
          <span class="text-slate-600 font-bold">RD ${d.chainage_km} km</span>
        </div>
        <p class="text-slate-700 font-semibold">${d.defect_dimensions}</p>
        <p class="text-[11px] text-slate-500">Source: ${d.detection_source}</p>
        <p class="text-[10px] font-mono text-slate-400">GPS: ${d.gps}</p>
      </div>

      <div class="p-3 bg-slate-50 border-t border-slate-200 flex justify-between items-center">
        <span class="text-[10px] text-slate-400">${d.date_detected}</span>
        <button onclick="openDispatchModal('${d.canal_id}', ${d.chainage_km}, '${d.defect_type}', '${d.defect_type}', 180000)" class="text-xs bg-deepTeal hover:bg-slate-800 text-white px-2.5 py-1 rounded font-medium">
          Create Work Order
        </button>
      </div>
    `;

    container.appendChild(card);
  });
}

function renderWorkOrders() {
  const tbody = document.getElementById('workOrderTableBody');
  tbody.innerHTML = '';

  state.workOrders.forEach(w => {
    let statusClass = 'bg-slate-100 text-slate-700';
    if (w.status === 'DISPATCHED') statusClass = 'bg-blue-100 text-blue-800 font-bold';
    if (w.status === 'IN_PROGRESS') statusClass = 'bg-amber-100 text-amber-800 font-bold';
    if (w.status === 'COMPLETED') statusClass = 'bg-emerald-100 text-emerald-800 font-bold';

    let sevClass = 'text-amber-600 font-bold';
    if (w.severity === 'CRITICAL') sevClass = 'text-red-600 font-bold';

    const tr = document.createElement('tr');
    tr.className = 'hover:bg-slate-50 transition border-b border-slate-100';

    tr.innerHTML = `
      <td class="py-2.5 px-3 font-mono font-bold text-slate-800">${w.id}</td>
      <td class="py-2.5 px-3">
        <div class="font-semibold text-slate-800">${w.canal_name}</div>
        <div class="text-[10px] text-slate-500">RD ${w.chainage_km} km</div>
      </td>
      <td class="py-2.5 px-3 font-medium">${w.defect_type}</td>
      <td class="py-2.5 px-3 ${sevClass}">${w.severity}</td>
      <td class="py-2.5 px-3">
        <div class="font-medium text-slate-800">${w.assigned_officer}</div>
        <div class="text-[10px] text-slate-500">${w.assigned_division}</div>
      </td>
      <td class="py-2.5 px-3 font-mono font-bold text-slate-800">₹ ${w.estimated_cost_inr.toLocaleString('en-IN')}</td>
      <td class="py-2.5 px-3"><span class="px-2 py-0.5 rounded text-[10px] ${statusClass}">${w.status}</span></td>
      <td class="py-2.5 px-3">
        <button onclick="alert('Work Order ${w.id} details dispatched to E-Nirman & Division WhatsApp Alert channel.')" class="text-deepTeal hover:text-slate-900 font-bold text-[11px]">
          <i class="fa-solid fa-arrow-up-right-from-square"></i>
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function switchTab(tabId, updateHash = true) {
  state.activeTab = tabId;
  document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
  const target = document.getElementById(tabId);
  if (target) target.classList.remove('hidden');

  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.remove('text-waterBlue', 'border-waterBlue');
    btn.classList.add('text-slate-500', 'border-transparent');
  });

  const activeBtn = document.getElementById(`btn-${tabId}`);
  if (activeBtn) {
    activeBtn.classList.remove('text-slate-500', 'border-transparent');
    activeBtn.classList.add('text-waterBlue', 'border-waterBlue');
  }

  if (updateHash) {
    const hashMap = {
      'tab-gis': 'gis-digital-twin',
      'tab-balance': 'hydraulic-mass-balance',
      'tab-defects': 'drone-defect-matrix',
      'tab-orders': 'predictive-work-orders',
      'tab-surge': 'breach-warning-simulation'
    };
    if (hashMap[tabId]) {
      history.replaceState(null, '', '#' + hashMap[tabId]);
    }
  }
}

function openTutorialModal(updateHash = true) {
  const modal = document.getElementById('tutorialModal');
  if (modal) modal.classList.remove('hidden');
  if (updateHash) {
    history.replaceState(null, '', '#tutorial');
  }
}

function closeTutorialModal() {
  const modal = document.getElementById('tutorialModal');
  if (modal) modal.classList.add('hidden');
  // Restore tab hash
  const hashMap = {
    'tab-gis': 'gis-digital-twin',
    'tab-balance': 'hydraulic-mass-balance',
    'tab-defects': 'drone-defect-matrix',
    'tab-orders': 'predictive-work-orders',
    'tab-surge': 'breach-warning-simulation'
  };
  const currentTab = state.activeTab || 'tab-gis';
  if (hashMap[currentTab]) {
    history.replaceState(null, '', '#' + hashMap[currentTab]);
  }
}

function switchTutTab(tutTabId) {
  document.querySelectorAll('.tut-content').forEach(el => el.classList.add('hidden'));
  const target = document.getElementById(tutTabId);
  if (target) target.classList.remove('hidden');

  document.querySelectorAll('.tut-nav-btn').forEach(btn => {
    btn.classList.remove('text-deepTeal', 'border-deepTeal', 'font-bold');
    btn.classList.add('text-slate-500', 'border-transparent', 'font-semibold');
  });

  const activeBtn = document.getElementById(`btn-${tutTabId}`);
  if (activeBtn) {
    activeBtn.classList.remove('text-slate-500', 'border-transparent', 'font-semibold');
    activeBtn.classList.add('text-deepTeal', 'border-deepTeal', 'font-bold');
  }
}

async function changeSimulationMode(mode) {
  try {
    const res = await fetch(`/api/simulate?mode=${mode}`, { method: 'POST' });
    const data = await res.json();
    alert(`System State Updated: ${mode}`);
    fetchLatestData();
  } catch (err) {
    console.error('Error changing simulation mode:', err);
  }
}

function updateSurgeSlider(val) {
  const headQ = Math.round(1100 + (val * 8.5));
  const pore = Math.round(68.0 + (val * 0.25));
  const fos = (1.45 - (val * 0.0055)).toFixed(2);

  document.getElementById('simHeadQ').innerText = `${headQ.toLocaleString()} cusecs`;
  document.getElementById('simPorePressure').innerText = `${pore} kPa`;
  document.getElementById('simFoS').innerHTML = `${fos} ${fos < 1.15 ? '<span class="text-red-600 font-bold">(CRITICAL UNSTABLE)</span>' : '<span class="text-emerald-600">(STABLE)</span>'}`;
}

function runScenarioAnalysis() {
  const val = parseInt(document.getElementById('surgeSlider').value);
  if (val > 40) {
    document.getElementById('simResultTitle').innerText = 'CRITICAL FORECAST: Imminent Slope Shear & Breach in 11.2 Hours';
    document.getElementById('simResultDesc').innerText = 'Pore-water pressure has saturated the embankment toe along Dhansiri RD 14.2 km. Without immediate head regulator throttling of 400 cusecs and placement of weighted geo-bags, a complete breach will inundate 1,450 hectares in Udalguri district.';
  } else {
    document.getElementById('simResultTitle').innerText = 'MODERATE FORECAST: Controlled High Inflow, Seepage Elevated';
    document.getElementById('simResultDesc').innerText = 'Pore-water pressure remains within acceptable transient parameters. Enhanced monitoring active on vulnerable reach RD 8.4 - 15.0 km.';
  }
}

function triggerAutomatedSluiceAdvisory() {
  alert('AUTOMATED SLUICE COMMAND EXECUTED: Headworks gates throttled by -350 cusecs. Hydro-pressure dissipating. Division Chief Engineer notified.');
}

function openDispatchModal(canalId, chainage, canalName, defect, cost) {
  document.getElementById('moCanal').value = canalName || 'Dhansiri Main Canal';
  document.getElementById('moChainage').value = chainage || 14.2;
  document.getElementById('moDefect').value = defect || 'Embankment Scouring / Slumping';
  document.getElementById('moCost').value = cost || 180000;
  document.getElementById('dispatchModal').classList.remove('hidden');
}

function closeDispatchModal() {
  document.getElementById('dispatchModal').classList.add('hidden');
}

async function submitWorkOrder(e) {
  e.preventDefault();
  const payload = {
    chainage_km: parseFloat(document.getElementById('moChainage').value),
    location_name: `${document.getElementById('moCanal').value} RD ${document.getElementById('moChainage').value} km`,
    canal_name: document.getElementById('moCanal').value,
    defect_type: document.getElementById('moDefect').value,
    severity: document.getElementById('moSeverity').value,
    estimated_cost_inr: parseFloat(document.getElementById('moCost').value),
    assigned_division: document.getElementById('moDivision').value,
    assigned_officer: document.getElementById('moOfficer').value,
    description: document.getElementById('moDescription').value || 'Immediate remediation dispatched via NeerDrishti AI.'
  };

  try {
    const res = await fetch('/api/work-orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const result = await res.json();
    alert(`Work Order ${result.work_order.id} Successfully Dispatched!`);
    closeDispatchModal();
    fetchLatestData();
  } catch (err) {
    console.error('Error creating work order:', err);
  }
}
