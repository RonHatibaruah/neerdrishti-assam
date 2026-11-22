/**
 * Cloudflare Pages Functions - Edge API router for NeerDrishti Assam
 * Problem Statement: NESFIC-D-02 (Irrigation Department, Govt of Assam)
 */

let SIMULATION_STATE = {
  mode: "NORMAL",
  surge_intensity: 0,
  last_updated: new Date().toISOString()
};

const CANAL_SEGMENTS = [
  {
    id: "JIS-MC-01",
    scheme_name: "Jamuna Irrigation Scheme",
    canal_name: "Jamuna Main Canal (Head Reach)",
    reach_type: "Head-Reach",
    chainage_start_km: 0.0,
    chainage_end_km: 6.5,
    district: "Hojai / Karbi Anglong",
    design_discharge_cusecs: 520.0,
    current_discharge_cusecs: 498.5,
    water_level_m: 2.45,
    design_depth_m: 2.60,
    silt_depth_m: 0.35,
    pore_pressure_kpa: 18.5,
    seepage_rate_lps_per_km: 1.8,
    asset_health_index: 88.5,
    risk_level: "LOW",
    detected_defects: [],
    coordinates: [
      [26.0125, 93.0245],
      [26.0230, 93.0410],
      [26.0350, 93.0580],
      [26.0480, 93.0720]
    ],
    last_inspected: "2026-11-20T10:30:00"
  },
  {
    id: "JIS-MC-02",
    scheme_name: "Jamuna Irrigation Scheme",
    canal_name: "Jamuna Main Canal (Mid Reach - Doboka Sec)",
    reach_type: "Mid-Reach",
    chainage_start_km: 6.5,
    chainage_end_km: 15.0,
    district: "Hojai",
    design_discharge_cusecs: 450.0,
    current_discharge_cusecs: 372.0,
    water_level_m: 2.15,
    design_depth_m: 2.40,
    silt_depth_m: 0.85,
    pore_pressure_kpa: 42.0,
    seepage_rate_lps_per_km: 8.4,
    asset_health_index: 54.0,
    risk_level: "HIGH",
    detected_defects: ["Abnormal Seepage / Piping", "Concrete Lining Fracture"],
    coordinates: [
      [26.0480, 93.0720],
      [26.0610, 93.0890],
      [26.0740, 93.1040],
      [26.0890, 93.1250]
    ],
    last_inspected: "2026-11-21T14:15:00"
  },
  {
    id: "JIS-MC-03",
    scheme_name: "Jamuna Irrigation Scheme",
    canal_name: "Jamuna Main Canal (Tail Reach - Kaki Branch)",
    reach_type: "Tail-Reach",
    chainage_start_km: 15.0,
    chainage_end_km: 28.5,
    district: "Hojai / Nagaon",
    design_discharge_cusecs: 280.0,
    current_discharge_cusecs: 178.0,
    water_level_m: 1.10,
    design_depth_m: 1.80,
    silt_depth_m: 1.15,
    pore_pressure_kpa: 12.0,
    seepage_rate_lps_per_km: 14.2,
    asset_health_index: 41.5,
    risk_level: "CRITICAL",
    detected_defects: ["Heavy Silt Deposition", "Aquatic Weed / Hyacinth Clogging"],
    coordinates: [
      [26.0890, 93.1250],
      [26.1050, 93.1420],
      [26.1210, 93.1630],
      [26.1380, 93.1850]
    ],
    last_inspected: "2026-11-22T09:00:00"
  },
  {
    id: "DIP-MC-01",
    scheme_name: "Dhansiri Irrigation Project",
    canal_name: "Dhansiri Main Canal (Bhairabkunda Headworks)",
    reach_type: "Head-Reach",
    chainage_start_km: 0.0,
    chainage_end_km: 12.0,
    district: "Udalguri (BTR)",
    design_discharge_cusecs: 1100.0,
    current_discharge_cusecs: 1045.0,
    water_level_m: 3.20,
    design_depth_m: 3.40,
    silt_depth_m: 0.40,
    pore_pressure_kpa: 24.0,
    seepage_rate_lps_per_km: 3.1,
    asset_health_index: 82.0,
    risk_level: "LOW",
    detected_defects: [],
    coordinates: [
      [26.8850, 92.1120],
      [26.8650, 92.1350],
      [26.8420, 92.1580],
      [26.8150, 92.1850]
    ],
    last_inspected: "2026-11-19T11:45:00"
  },
  {
    id: "DIP-MC-02",
    scheme_name: "Dhansiri Irrigation Project",
    canal_name: "Dhansiri Main Canal (Embankment Stretch RD 14.2 km)",
    reach_type: "Mid-Reach",
    chainage_start_km: 12.0,
    chainage_end_km: 24.5,
    district: "Udalguri",
    design_discharge_cusecs: 850.0,
    current_discharge_cusecs: 710.0,
    water_level_m: 2.85,
    design_depth_m: 3.00,
    silt_depth_m: 0.65,
    pore_pressure_kpa: 68.0,
    seepage_rate_lps_per_km: 18.5,
    asset_health_index: 36.0,
    risk_level: "CRITICAL",
    detected_defects: ["Embankment Scouring / Slumping", "Abnormal Seepage / Piping"],
    coordinates: [
      [26.8150, 92.1850],
      [26.7900, 92.2100],
      [26.7650, 92.2350],
      [26.7350, 92.2650]
    ],
    last_inspected: "2026-11-22T08:30:00"
  },
  {
    id: "SIS-MC-01",
    scheme_name: "Sukla Irrigation Scheme",
    canal_name: "Sukla Main Canal (Naokata Section)",
    reach_type: "Mid-Reach",
    chainage_start_km: 4.0,
    chainage_end_km: 14.5,
    district: "Baksa (BTR)",
    design_discharge_cusecs: 340.0,
    current_discharge_cusecs: 285.0,
    water_level_m: 1.75,
    design_depth_m: 1.90,
    silt_depth_m: 0.50,
    pore_pressure_kpa: 31.0,
    seepage_rate_lps_per_km: 6.2,
    asset_health_index: 68.0,
    risk_level: "MODERATE",
    detected_defects: ["Aquatic Weed / Hyacinth Clogging"],
    coordinates: [
      [26.6850, 91.6850],
      [26.6620, 91.7050],
      [26.6400, 91.7300],
      [26.6150, 91.7550]
    ],
    last_inspected: "2026-11-21T16:00:00"
  }
];

const TELEMETRY_NODES = [
  {
    node_id: "TEL-JAM-01",
    chainage_km: 0.2,
    location_name: "Jamuna Head Regulator (Bakulia)",
    sensor_types: ["Ultrasonic Level", "Acoustic Doppler Flow", "Solar Power Engine"],
    water_level_m: 2.45,
    flow_velocity_mps: 1.42,
    discharge_cusecs: 498.5,
    soil_moisture_pct: 28.4,
    pore_pressure_kpa: 18.5,
    battery_pct: 98,
    solar_status: "CHARGING",
    signal_strength_dbm: -68,
    last_ping: "1 min ago",
    status: "ONLINE"
  },
  {
    node_id: "TEL-JAM-02",
    chainage_km: 8.4,
    location_name: "Doboka Cross-Regulator Aqueduct",
    sensor_types: ["Ultrasonic Level", "Pore Pressure Piezometer", "Structural Inclinometer"],
    water_level_m: 2.15,
    flow_velocity_mps: 1.15,
    discharge_cusecs: 372.0,
    soil_moisture_pct: 52.8,
    pore_pressure_kpa: 42.0,
    battery_pct: 91,
    solar_status: "CHARGING",
    signal_strength_dbm: -74,
    last_ping: "Just now",
    status: "ALERT_SEEPAGE"
  },
  {
    node_id: "TEL-JAM-03",
    chainage_km: 19.8,
    location_name: "Kaki Tail-End Distributary RD 20",
    sensor_types: ["Ultrasonic Level", "Acoustic Sediment Silt Gauge"],
    water_level_m: 1.10,
    flow_velocity_mps: 0.65,
    discharge_cusecs: 178.0,
    soil_moisture_pct: 34.0,
    pore_pressure_kpa: 12.0,
    battery_pct: 84,
    solar_status: "NORMAL",
    signal_strength_dbm: -81,
    last_ping: "3 mins ago",
    status: "CRITICAL_DEFICIT"
  },
  {
    node_id: "TEL-DHN-01",
    chainage_km: 14.2,
    location_name: "Dhansiri Right Bank Embankment RD 14.2",
    sensor_types: ["Piezometer Array", "Vibrating Wire Pore Pressure", "Tilt Sensor"],
    water_level_m: 2.85,
    flow_velocity_mps: 1.68,
    discharge_cusecs: 710.0,
    soil_moisture_pct: 74.5,
    pore_pressure_kpa: 68.0,
    battery_pct: 95,
    solar_status: "CHARGING",
    signal_strength_dbm: -65,
    last_ping: "Just now",
    status: "IMMINENT_BREACH_ALERT"
  }
];

const CV_DETECTIONS = [
  {
    id: "DET-2026-089",
    canal_id: "DIP-MC-02",
    chainage_km: 14.2,
    defect_type: "Embankment Scouring / Slumping",
    severity: "CRITICAL",
    confidence_pct: 96.4,
    defect_dimensions: "Length: 14.5m, Scour Depth: 1.2m, Slope angle: 48°",
    estimated_soil_loss_cum: 42.0,
    image_thumbnail: "assets/infographic_cv_defect_matrix_16x9.png",
    detection_source: "Assam Drone Patrol Wing (Mission D-14)",
    gps: "26.7912 N, 92.2115 E",
    date_detected: "2026-11-22 08:30"
  },
  {
    id: "DET-2026-082",
    canal_id: "JIS-MC-02",
    chainage_km: 9.1,
    defect_type: "Concrete Lining Fracture",
    severity: "HIGH",
    confidence_pct: 92.1,
    defect_dimensions: "Longitudinal crack 8.4m length, aperture 35mm",
    estimated_soil_loss_cum: 8.5,
    image_thumbnail: "assets/infographic_cv_defect_matrix_16x9.png",
    detection_source: "Field Mobile App - SDO Hojai Patrol",
    gps: "26.0645 N, 93.0910 E",
    date_detected: "2026-11-21 14:15"
  },
  {
    id: "DET-2026-075",
    canal_id: "JIS-MC-03",
    chainage_km: 18.5,
    defect_type: "Aquatic Weed / Hyacinth Choking",
    severity: "HIGH",
    confidence_pct: 98.2,
    defect_dimensions: "Dense hyacinth mat spanning 450m length, 100% surface choke",
    estimated_soil_loss_cum: 0.0,
    image_thumbnail: "assets/infographic_cv_defect_matrix_16x9.png",
    detection_source: "Satellite Sentinel-2 NDWI anomaly",
    gps: "26.1150 N, 93.1550 E",
    date_detected: "2026-11-22 06:00"
  }
];

let WORK_ORDERS = [
  {
    id: "WO-2026-041",
    chainage_km: 14.2,
    location_name: "Dhansiri Main Canal RD 14.2 km (Bhairabkunda Div)",
    canal_name: "Dhansiri Main Canal",
    defect_type: "Embankment Scouring / Slumping",
    severity: "CRITICAL",
    estimated_cost_inr: 385000.0,
    assigned_division: "Udalguri Irrigation Division",
    assigned_officer: "Sri B. K. Sarma, Executive Engineer",
    status: "DISPATCHED",
    created_at: "2026-11-22T08:45:00",
    target_completion: "2026-11-24T18:00:00",
    description: "Urgent geo-textile bag pitching, boulder rip-rap dumping and compaction along outer bank to prevent catastrophic breach."
  },
  {
    id: "WO-2026-038",
    chainage_km: 9.1,
    location_name: "Jamuna Main Canal RD 9.1 km (Doboka Sub-Div)",
    canal_name: "Jamuna Main Canal",
    defect_type: "Concrete Lining Fracture",
    severity: "HIGH",
    estimated_cost_inr: 142000.0,
    assigned_division: "Hojai Irrigation Division",
    assigned_officer: "Er. P. Baruah, SDO",
    status: "IN_PROGRESS",
    created_at: "2026-11-21T15:00:00",
    target_completion: "2026-11-25T18:00:00",
    description: "Polymer-modified mortar pressure grouting and elastomeric sealant injection into lining aperture to halt sub-base erosion."
  },
  {
    id: "WO-2026-035",
    chainage_km: 18.5,
    location_name: "Jamuna Canal Tail Reach (Kaki Sub-Div)",
    canal_name: "Jamuna Main Canal",
    defect_type: "Aquatic Weed / Hyacinth Choking",
    severity: "HIGH",
    estimated_cost_inr: 85000.0,
    assigned_division: "Hojai Irrigation Division",
    assigned_officer: "Sri M. Teron, Section Officer",
    status: "OPEN",
    created_at: "2026-11-22T09:30:00",
    target_completion: "2026-11-26T17:00:00",
    description: "Deployment of aquatic weed harvester and manual clearance team to restore discharge flow to tail-end cultivators."
  }
];

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const path = url.pathname;
  const method = context.request.method;

  const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Content-Type": "application/json; charset=utf-8"
  };

  if (method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders });
  }

  if (path === "/api/summary") {
    const total_length_km = CANAL_SEGMENTS.reduce((acc, c) => acc + (c.chainage_end_km - c.chainage_start_km), 0);
    const avg_health = CANAL_SEGMENTS.reduce((acc, c) => acc + c.asset_health_index, 0) / CANAL_SEGMENTS.length;
    const critical_breaches = CANAL_SEGMENTS.filter(c => c.risk_level === "CRITICAL").length;
    const open_orders = WORK_ORDERS.filter(w => ["OPEN", "DISPATCHED", "IN_PROGRESS"].includes(w.status)).length;
    const water_saved_mld = SIMULATION_STATE.mode !== "MONSOON_SURGE" ? 34.6 : 62.8;

    return new Response(JSON.stringify({
      total_monitored_length_km: Number(total_length_km.toFixed(1)),
      total_schemes_active: new Set(CANAL_SEGMENTS.map(c => c.scheme_name)).size,
      average_asset_health_index: Number(avg_health.toFixed(1)),
      critical_risk_sections: critical_breaches,
      active_maintenance_work_orders: open_orders,
      tail_end_equity_index_pct: SIMULATION_STATE.mode === "NORMAL" ? 68.4 : 42.1,
      estimated_prevented_water_loss_mld: water_saved_mld,
      simulation_mode: SIMULATION_STATE.mode,
      telemetry_health_pct: 98.2,
      last_sync: new Date().toISOString().replace('T', ' ').substring(0, 19) + ' IST'
    }), { headers: corsHeaders });
  }

  if (path === "/api/canals") {
    return new Response(JSON.stringify({
      canals: CANAL_SEGMENTS,
      simulation: SIMULATION_STATE
    }), { headers: corsHeaders });
  }

  if (path === "/api/telemetry") {
    const nodes = TELEMETRY_NODES.map(t => {
      const jitter = (Math.random() - 0.5) * 0.04;
      return {
        ...t,
        water_level_m: Number((t.water_level_m + jitter).toFixed(2)),
        flow_velocity_mps: Number((t.flow_velocity_mps + jitter * 0.5).toFixed(2)),
        discharge_cusecs: Number((t.discharge_cusecs + jitter * 2.0).toFixed(1))
      };
    });
    return new Response(JSON.stringify({ nodes }), { headers: corsHeaders });
  }

  if (path === "/api/hydro-balance") {
    const scheme = url.searchParams.get("scheme") || "Jamuna Irrigation Scheme";
    let inflow, offtakes, tail_measured, transit_designed;
    if (scheme === "Jamuna Irrigation Scheme") {
      inflow = 498.5; offtakes = 185.0; tail_measured = 178.0; transit_designed = 35.0;
    } else {
      inflow = 1045.0; offtakes = 210.0; tail_measured = 710.0; transit_designed = 55.0;
    }
    const unaccounted = inflow - offtakes - tail_measured - transit_designed;
    const loss_pct = (unaccounted / inflow) * 100.0;
    const equity_ratio = (tail_measured / (inflow - offtakes)) * 100.0;

    return new Response(JSON.stringify({
      scheme_name: scheme,
      inflow_headworks_cusecs: Number(inflow.toFixed(1)),
      authorized_offtakes_cusecs: Number(offtakes.toFixed(1)),
      actual_tail_delivery_cusecs: Number(tail_measured.toFixed(1)),
      permissible_conveyance_loss_cusecs: Number(transit_designed.toFixed(1)),
      unaccounted_water_loss_cusecs: Number(Math.max(0, unaccounted).toFixed(1)),
      unaccounted_loss_percentage: Number(Math.max(0, loss_pct).toFixed(1)),
      tail_delivery_equity_ratio: Number(equity_ratio.toFixed(1)),
      status: unaccounted > 30 ? "ABNORMAL_SEEPAGE_FLAGGED" : "OPTIMAL_BALANCE"
    }), { headers: corsHeaders });
  }

  if (path === "/api/defects") {
    return new Response(JSON.stringify({ defects: CV_DETECTIONS }), { headers: corsHeaders });
  }

  if (path === "/api/work-orders") {
    if (method === "POST") {
      try {
        const body = await context.request.json();
        const new_id = `WO-2026-0${WORK_ORDERS.length + 42}`;
        const wo = {
          id: new_id,
          chainage_km: body.chainage_km,
          location_name: body.location_name,
          canal_name: body.canal_name,
          defect_type: body.defect_type,
          severity: body.severity,
          estimated_cost_inr: body.estimated_cost_inr,
          assigned_division: body.assigned_division,
          assigned_officer: body.assigned_officer,
          status: "DISPATCHED",
          created_at: new Date().toISOString(),
          target_completion: new Date(Date.now() + 3*86400000).toISOString().replace('T', ' ').substring(0, 19),
          description: body.description
        };
        WORK_ORDERS.unshift(wo);
        return new Response(JSON.stringify({ status: "SUCCESS", work_order: wo }), { headers: corsHeaders });
      } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 400, headers: corsHeaders });
      }
    }
    return new Response(JSON.stringify({ work_orders: WORK_ORDERS }), { headers: corsHeaders });
  }

  if (path === "/api/simulate") {
    const mode = url.searchParams.get("mode") || "NORMAL";
    SIMULATION_STATE.mode = mode;
    SIMULATION_STATE.last_updated = new Date().toISOString();
    return new Response(JSON.stringify({ message: `Simulation set to ${mode}`, simulation: SIMULATION_STATE }), { headers: corsHeaders });
  }

  return new Response(JSON.stringify({ error: "Endpoint not found" }), { status: 404, headers: corsHeaders });
}
