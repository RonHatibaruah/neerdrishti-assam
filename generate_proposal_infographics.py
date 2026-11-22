"""
Generate additional high-impact 16:9 widescreen infographics tailored for the Official Proposal PDF:
1. infographic_user_journey_workflow_16x9.png - Current Manual Routine vs NeerDrishti Automated Loop
2. infographic_roadmap_gantt_milestones_16x9.png - 7-Month Agile-V Roadmap & Validation Milestones
3. infographic_governance_security_16x9.png - ASDC Cloud Architecture, TLS 1.3, RBAC & Human-in-the-Loop
4. infographic_competitive_budget_16x9.png - Competitive Matrix & ₹40 Lakhs Grant Resource Allocation
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
import numpy as np
import os

os.environ['MPLCONFIGDIR'] = '/tmp'
os.makedirs("assets", exist_ok=True)

def setup_canvas():
    fig, ax = plt.subplots(figsize=(16, 9), dpi=220)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    
    # Clean blueprint grid background
    ax.set_facecolor('#f8fafc')
    fig.patch.set_facecolor('#f8fafc')
    
    # Draw subtle blueprint gridlines
    for x in np.arange(0, 16, 0.5):
        ax.axvline(x, color='#e2e8f0', linestyle='-', linewidth=0.5, alpha=0.6, zorder=1)
    for y in np.arange(0, 9, 0.5):
        ax.axhline(y, color='#e2e8f0', linestyle='-', linewidth=0.5, alpha=0.6, zorder=1)
        
    return fig, ax

def add_header(ax, title, subtitle, challenge_code="NESFIC-D-02 | PROPOSAL EVIDENCE"):
    header_box = FancyBboxPatch((0.5, 7.85), 15.0, 0.85, boxstyle="round,pad=0.08,rounding_size=0.15",
                                facecolor='#0f3a42', edgecolor='#d4af37', linewidth=1.8, zorder=3)
    ax.add_patch(header_box)
    
    dept_badge = FancyBboxPatch((0.7, 8.35), 4.2, 0.25, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor='#0b4d26', edgecolor='none', zorder=4)
    ax.add_patch(dept_badge)
    ax.text(2.8, 8.47, "GOVERNMENT OF ASSAM • IRRIGATION DEPARTMENT", color='#86efac', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=5)
    
    code_badge = FancyBboxPatch((12.2, 8.35), 3.1, 0.25, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor='#b45309', edgecolor='none', zorder=4)
    ax.add_patch(code_badge)
    ax.text(13.75, 8.47, challenge_code, color='#fef08a', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=5)
    
    ax.text(0.7, 8.12, title, color='white', fontsize=14, fontweight='bold', va='center', zorder=5)
    ax.text(0.7, 7.94, subtitle, color='#cbd5e1', fontsize=8.8, va='center', zorder=5)

# ==============================================================================
# 1. USER WORKFLOW COMPARISON INFOGRAPHIC
# ==============================================================================
print("Generating Proposal Infographic 1: Workflow Comparison...")
fig, ax = setup_canvas()
add_header(ax, "PARADIGM SHIFT: CURRENT STATUS QUO VS. NEERDRISHTI AUTOMATED WORKFLOW",
           "Transitioning Assam's Canal Asset Management from Reactive Crisis Firefighting to Autonomous Predictive Prevention")

# Upper Track: Current Status Quo (Red/Gray theme)
p_cur = FancyBboxPatch((0.5, 4.3), 15.0, 3.25, boxstyle="round,pad=0.05,rounding_size=0.12",
                       facecolor='#fef2f2', edgecolor='#dc2626', linewidth=1.6, zorder=2)
ax.add_patch(p_cur)
t_cur = FancyBboxPatch((0.7, 7.25), 5.5, 0.25, boxstyle="round,pad=0.02,rounding_size=0.06",
                       facecolor='#dc2626', edgecolor='none', zorder=3)
ax.add_patch(t_cur)
ax.text(3.45, 7.37, "CURRENT MANUAL & REACTIVE ROUTINE (STATUS QUO)", color='white', fontsize=8, fontweight='bold', ha='center', va='center', zorder=4)

cur_steps = [
    ("1. MANUAL VISUAL PATROLS", "Chowkidars & patrolmen walk canal bunds sporadically\n• Infeasible for 5,800 km\n• Zero night or flood coverage", "#991b1b", 0.7),
    ("2. 5-14 DAYS PAPER LAG", "Defects recorded on paper logs or informal WhatsApp\n• High latency in reporting\n• Missing exact chainage coordinates", "#991b1b", 4.5),
    ("3. CATASTROPHIC BREACH", "Saturated dykes fail via backward piping & slumping\n• Village farmland inundated\n• Parched tail-end cultivators", "#b91c1c", 8.3),
    ("4. EMERGENCY CRISIS TENDER", "Emergency repair tenders post-disaster\n• High financial costs\n• Months of delayed crop irrigation", "#7f1d1d", 12.1)
]
for title, desc, col, x in cur_steps:
    c = FancyBboxPatch((x, 4.5), 3.2, 2.55, boxstyle="round,pad=0.03,rounding_size=0.08",
                       facecolor='white', edgecolor=col, linewidth=1.2, zorder=3)
    ax.add_patch(c)
    tag = FancyBboxPatch((x + 0.1, 6.7), 3.0, 0.24, boxstyle="round,pad=0.02,rounding_size=0.05",
                         facecolor=col, edgecolor='none', zorder=4)
    ax.add_patch(tag)
    ax.text(x + 1.6, 6.82, title, color='white', fontsize=7.2, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(x + 0.2, 5.5, desc, color='#334155', fontsize=7.2, va='center', zorder=4)

for cx in [4.0, 7.8, 11.6]:
    ax.annotate('', xy=(cx + 0.4, 5.8), xytext=(cx - 0.05, 5.8),
                arrowprops=dict(facecolor='#dc2626', arrowstyle="->", lw=2.2), zorder=5)

# Lower Track: NeerDrishti Automated Loop (Green/Blue theme)
p_nd = FancyBboxPatch((0.5, 0.4), 15.0, 3.5, boxstyle="round,pad=0.05,rounding_size=0.12",
                      facecolor='#ecfdf5', edgecolor='#059669', linewidth=1.6, zorder=2)
ax.add_patch(p_nd)
t_nd = FancyBboxPatch((0.7, 3.55), 5.5, 0.25, boxstyle="round,pad=0.02,rounding_size=0.06",
                      facecolor='#059669', edgecolor='none', zorder=3)
ax.add_patch(t_nd)
ax.text(3.45, 3.67, "NEERDRISHTI AUTONOMOUS DIGITAL TWIN WORKFLOW", color='white', fontsize=8, fontweight='bold', ha='center', va='center', zorder=4)

nd_steps = [
    ("1. AUTONOMOUS EDGE IOT", "Ultrasonic level, velocity & dyke pore pressure telemetry\n• 10-minute continuous transmission\n• 100% solar LoRa/4G uptime", "#0284c7", 0.7),
    ("2. <15 MIN ANOMALY TRIAGE", "Saint-Venant mass-balance flags abnormal seepage\n• Sentinel-2 NDWI plume mapping\n• Instant incident alert to SDO/EE", "#0284c7", 4.5),
    ("3. 14.5H BREACH WARNING", "Bishop Slope Stability model forecasts failure horizon\n• Automated barrage throttling advice\n• Complete village flood protection", "#059669", 8.3),
    ("4. AUTO E-NIRMAN WORK ORDER", "Work orders auto-calculated via Assam PWD SOR\n• Geo-bags & rip-rap BoQ generated\n• Verified tail-end water equity", "#047857", 12.1)
]
for title, desc, col, x in nd_steps:
    c = FancyBboxPatch((x, 0.6), 3.2, 2.75, boxstyle="round,pad=0.03,rounding_size=0.08",
                       facecolor='white', edgecolor=col, linewidth=1.2, zorder=3)
    ax.add_patch(c)
    tag = FancyBboxPatch((x + 0.1, 3.0), 3.0, 0.24, boxstyle="round,pad=0.02,rounding_size=0.05",
                         facecolor=col, edgecolor='none', zorder=4)
    ax.add_patch(tag)
    ax.text(x + 1.6, 3.12, title, color='white', fontsize=7.2, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(x + 0.2, 1.75, desc, color='#334155', fontsize=7.2, va='center', zorder=4)

for cx in [4.0, 7.8, 11.6]:
    ax.annotate('', xy=(cx + 0.4, 2.0), xytext=(cx - 0.05, 2.0),
                arrowprops=dict(facecolor='#059669', arrowstyle="->", lw=2.2), zorder=5)

plt.tight_layout()
plt.savefig("assets/infographic_user_journey_workflow_16x9.png", dpi=220)
plt.close()

# ==============================================================================
# 2. ROADMAP & GANTT MILESTONES INFOGRAPHIC
# ==============================================================================
print("Generating Proposal Infographic 2: Roadmap & Gantt...")
fig, ax = setup_canvas()
add_header(ax, "7-MONTH AGILE-V DEVELOPMENT ROADMAP & FIELD VALIDATION GATES",
           "Iterative Software Sprints Integrated with Rigorous CWC/BIS Civil Engineering Verification Gates")

# 7-Month Columns
months = ["Month 1 (W1-4)", "Month 2 (W5-8)", "Month 3 (W9-12)", "Month 4 (W13-16)", "Month 5 (W17-20)", "Month 6 (W21-24)", "Month 7 (W25-28)"]
for m_idx, m_name in enumerate(months):
    mx = 0.5 + (m_idx * 2.14)
    m_box = FancyBboxPatch((mx, 7.15), 2.08, 0.55, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#0f3a42', edgecolor='#d4af37', linewidth=1.2, zorder=3)
    ax.add_patch(m_box)
    ax.text(mx + 1.04, 7.42, m_name, color='white', fontsize=7.8, fontweight='bold', ha='center', va='center', zorder=4)

# Gantt Track Bars
tracks = [
    ("TRACK 1: Civil Survey & GIS Baseline", 0.5, 0.5 + 2.14*2, 6.2, "#0284c7", "Jamuna & Dhansiri Bathymetric Profiling & Sensor Topology Matrix"),
    ("TRACK 2: Edge IoT Firmware & Prototyping", 0.5 + 2.14, 0.5 + 2.14*3, 5.2, "#0369a1", "IP68 Enclosure Weatherproofing, Solar Power & LoRa/4G RTU Build"),
    ("TRACK 3: AI Digital Twin & Mass Balance", 0.5 + 2.14*2, 0.5 + 2.14*4, 4.2, "#b45309", "1D Saint-Venant Solver, Bishop FoS Breach Predictor & YOLOv8 Training"),
    ("TRACK 4: Web GIS Console & Mobile App", 0.5 + 2.14*3, 0.5 + 2.14*5, 3.2, "#7c3aed", "Full-Stack Dashboard, Assam PWD SOR Engine & Offline Android APK"),
    ("TRACK 5: 30 km Field Pilot Deployment", 0.5 + 2.14*4, 0.5 + 2.14*6, 2.2, "#dc2626", "Sensors Installed at Jamuna RD 0-15 & Dhansiri RD 12-24.5 [VALIDATION GATE]"),
    ("TRACK 6: Pilot Audit & E-Nirman Handover", 0.5 + 2.14*5, 0.5 + 2.14*7, 1.2, "#059669", "Joint Departmental Validation, Water Loss Recovery Audit & Scale Blueprint")
]

for track_name, start_x, end_x, y_pos, col, desc in tracks:
    # Track title label
    ax.text(0.6, y_pos + 0.65, track_name, color='#0f172a', fontsize=8.2, fontweight='bold', zorder=4)
    # Background full track line
    ax.plot([0.5, 15.5], [y_pos + 0.3, y_pos + 0.3], color='#e2e8f0', linewidth=10, zorder=2)
    # Active Gantt Bar
    bar_patch = FancyBboxPatch((start_x, y_pos + 0.08), (end_x - start_x), 0.44, boxstyle="round,pad=0.02,rounding_size=0.08",
                               facecolor=col, edgecolor='none', zorder=3)
    ax.add_patch(bar_patch)
    ax.text(start_x + (end_x - start_x)/2.0, y_pos + 0.3, desc, color='white', fontsize=7.2, fontweight='bold', ha='center', va='center', zorder=4)

# Validation Gate Banner on Month 5
vg_patch = FancyBboxPatch((0.5 + 2.14*4 + 0.1, 0.3), 4.15, 0.7, boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor='#fef08a', edgecolor='#ca8a04', linewidth=1.5, zorder=3)
ax.add_patch(vg_patch)
ax.text(0.5 + 2.14*4 + 2.17, 0.65, "FIELD VALIDATION READINESS GATE (WEEK 20)", color='#854d0e', fontsize=7.5, fontweight='bold', ha='center', zorder=4)
ax.text(0.5 + 2.14*4 + 2.17, 0.45, "30 km Sensor Telemetry Live Streaming to Assam State Data Centre (ASDC)", color='#1e293b', fontsize=6.8, ha='center', zorder=4)

plt.tight_layout()
plt.savefig("assets/infographic_roadmap_gantt_milestones_16x9.png", dpi=220)
plt.close()

# ==============================================================================
# 3. GOVERNANCE & SECURITY INFOGRAPHIC
# ==============================================================================
print("Generating Proposal Infographic 3: Governance & Security...")
fig, ax = setup_canvas()
add_header(ax, "ASDC CLOUD DEPLOYMENT, CYBERSECURITY & HUMAN-IN-THE-LOOP GOVERNANCE",
           "Enterprise Security Architecture Adhering to MeitY, CWC Guidelines & CERT-In Benchmarks")

gov_boxes = [
    ("1. ASSAM STATE DATA CENTRE (ASDC) SOVEREIGN HOSTING",
     "• Deployed within Tier-III Certified ASDC, Guwahati\n"
     "• 100% Data Sovereignty: No international cloud transmission\n"
     "• TimescaleDB Time-Series Clustering (>10,000 pings/sec)\n"
     "• PostGIS Spatial Geometry Engine for 5,800 km Canal Network\n"
     "• Containerized Microservices on Secure Hardened Kubernetes",
     "#0284c7", "#e0f2fe", 0.5, 4.0),
    
    ("2. END-TO-END CRYPTOGRAPHIC SECURITY (TLS 1.3 & AES-256)",
     "• TLS 1.3 Transport Encryption with Pre-Shared Cryptographic Keys\n"
     "• AES-256 Storage Encryption for Telemetry & Asset Registers\n"
     "• Hardware Security Module (HSM) Key Management\n"
     "• Strict CERT-In Guidelines & OWASP Top 10 API Security Alignment\n"
     "• Automated Penetration Testing & Vulnerability Scanning (VAPT)",
     "#059669", "#ecfdf5", 8.2, 4.0),
    
    ("3. ROLE-BASED ACCESS CONTROL (RBAC) & AUDITABILITY",
     "• State Chief Engineer: Statewide KPI Oversight & Policy Planning\n"
     "• Division Executive Engineer: Tender Approval & Gate Authorization\n"
     "• Sub-Divisional Officer (SDO): Work-Order Review & Dispatch\n"
     "• Section Officer (SO): Geotagged Field Inspection Verification\n"
     "• Immutable Audit Trail: Every alert & work order timestamped with GPS",
     "#7c3aed", "#f3e8ff", 0.5, 0.4),
    
    ("4. HUMAN-IN-THE-LOOP CRITICAL SAFETY SAFEGUARD",
     "• AI Acts Exclusively as an Intelligent Advisory Decision Support\n"
     "• NO Autonomous Gate Actuation: Upstream throttling requires EE approval\n"
     "• NO Autonomous Financial Outlay: Tenders routed via Assam E-Nirman\n"
     "• Fail-Safe Mechanical Override on all Headworks Barrage Gates\n"
     "• Dual-Factor Authentication (MFA) via Gov-SMS OTP for all critical actions",
     "#b45309", "#fef3c7", 8.2, 0.4)
]

for title, content, border_col, bg_col, qx, qy in gov_boxes:
    q_patch = FancyBboxPatch((qx, qy), 7.3, 3.2, boxstyle="round,pad=0.05,rounding_size=0.12",
                            facecolor=bg_col, edgecolor=border_col, linewidth=1.6, zorder=2)
    ax.add_patch(q_patch)
    tag = FancyBboxPatch((qx + 0.1, qy + 2.8), 7.1, 0.32, boxstyle="round,pad=0.02,rounding_size=0.06",
                         facecolor=border_col, edgecolor='none', zorder=3)
    ax.add_patch(tag)
    ax.text(qx + 3.65, qy + 2.96, title, color='white', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=4)
    
    i_card = FancyBboxPatch((qx + 0.2, qy + 0.18), 6.9, 2.5, boxstyle="round,pad=0.03,rounding_size=0.08",
                            facecolor='white', edgecolor=border_col, linewidth=1.0, zorder=3)
    ax.add_patch(i_card)
    
    lines = content.split("\n")
    for l_idx, line in enumerate(lines):
        ly = qy + 2.35 - (l_idx * 0.48)
        ax.text(qx + 0.4, ly, line, color='#334155', fontsize=7.5, zorder=4)

plt.tight_layout()
plt.savefig("assets/infographic_governance_security_16x9.png", dpi=220)
plt.close()

# ==============================================================================
# 4. COMPETITIVE MATRIX & BUDGET INFOGRAPHIC
# ==============================================================================
print("Generating Proposal Infographic 4: Competitive Matrix & Budget...")
fig, ax = setup_canvas()
add_header(ax, "INNOVATION DIFFERENTIATION & ₹40.0 LAKHS GRANT RESOURCE ALLOCATION",
           "Competitive Advantage Over Legacy Practice and Transparent Fiscal Planning for 30 km Pilot Deployment")

# Left: Competitive Differentiation Cards
left_p = FancyBboxPatch((0.5, 0.4), 7.6, 6.8, boxstyle="round,pad=0.05,rounding_size=0.12",
                        facecolor='white', edgecolor='#0f3a42', linewidth=1.6, zorder=2)
ax.add_patch(left_p)
ax.text(0.8, 6.85, "COMPETITIVE ADVANTAGE MATRIX", color='#0f3a42', fontsize=9.5, fontweight='bold', zorder=3)

diff_items = [
    ("DETECTION SPEED", "Manual Patrols: 5-14 days | Satellite: 5-10 days (cloud-prone)", "NeerDrishti: < 15 Minutes Autonomous Telemetry", "#059669"),
    ("BREACH FORECASTING", "Manual/SCADA: Zero predictive ability | Post-disaster reaction", "NeerDrishti: 14.5 Hours Advance Warning (Bishop FoS)", "#059669"),
    ("WATER EQUITY TRACKING", "Legacy: Reactive farmer complaints & tail-end crop parching", "NeerDrishti: Real-Time Tail-End Delivery Equity Index (DEI)", "#0284c7"),
    ("PROCUREMENT LINK", "Legacy: 3-6 weeks paper approvals & crisis tendering", "NeerDrishti: Auto BoQ Generated via Assam Irrigation SOR", "#7c3aed"),
    ("CAPITAL OUTLAY", "Mains SCADA: Rs. 20-50 Lakhs per gate | High power grid dependence", "NeerDrishti: Ultra-low-power Solar LoRa/4G Edge Sensors", "#b45309")
]
for idx, (dim, leg, nd, col) in enumerate(diff_items):
    iy = 5.6 - (idx * 1.25)
    i_box = FancyBboxPatch((0.8, iy), 7.0, 1.15, boxstyle="round,pad=0.03,rounding_size=0.06",
                           facecolor='#f8fafc', edgecolor=col, linewidth=1.2, zorder=3)
    ax.add_patch(i_box)
    ax.text(1.0, iy + 0.9, dim, color=col, fontsize=7.5, fontweight='bold', zorder=4)
    ax.text(1.0, iy + 0.6, leg, color='#64748b', fontsize=6.8, zorder=4)
    ax.text(1.0, iy + 0.25, nd, color='#0f172a', fontsize=7.5, fontweight='bold', zorder=4)

# Right: Budget Allocation Visualization (₹40.0 Lakhs)
right_p = FancyBboxPatch((8.4, 0.4), 7.1, 6.8, boxstyle="round,pad=0.05,rounding_size=0.12",
                         facecolor='white', edgecolor='#d4af37', linewidth=1.6, zorder=2)
ax.add_patch(right_p)
ax.text(8.7, 6.85, "TOTAL GRANT ALLOCATION: ₹ 40.0 LAKHS (100%)", color='#b45309', fontsize=9.5, fontweight='bold', zorder=3)

budget_bars = [
    ("Software Development & Engineering Team", "₹ 20,00,000", "50.0%", 5.0, "#0f3a42", "7-Month Specialized Engineering Team (AI/ML, GIS, Water Lead, Geotech)"),
    ("IoT Sensors & Edge Telemetry Hardware", "₹ 11,50,000", "28.8%", 2.88, "#0284c7", "12 Ultrasonic Sensors, 6 ADCP Flow Meters, 18 Piezometers, 8 Solar Gateways"),
    ("Field Installation & RTK Topographic Survey", "₹ 4,00,000", "10.0%", 1.0, "#059669", "RTK Bathymetric Profiling, Steel Cantilever Mountings above 100-yr HFL"),
    ("Pilot Validation & Farmer WUA Outreach", "₹ 2,50,000", "6.2%", 0.62, "#d97706", "Joint Departmental Calibration Trials & 14 Gaon Panchayat WUA Workshops"),
    ("Cloud Infrastructure & ASDC Deployment", "₹ 2,00,000", "5.0%", 0.5, "#7c3aed", "Assam State Data Centre (ASDC) Tier-III Containers, TimescaleDB & E-Nirman API")
]

for b_idx, (b_cat, b_amt, b_pct, b_len, b_col, b_desc) in enumerate(budget_bars):
    by = 5.6 - (b_idx * 1.25)
    b_card = FancyBboxPatch((8.7, by), 6.5, 1.15, boxstyle="round,pad=0.03,rounding_size=0.06",
                            facecolor='#f8fafc', edgecolor=b_col, linewidth=1.2, zorder=3)
    ax.add_patch(b_card)
    ax.text(8.9, by + 0.9, b_cat, color='#0f172a', fontsize=7.5, fontweight='bold', zorder=4)
    ax.text(14.9, by + 0.9, f"{b_amt} ({b_pct})", color=b_col, fontsize=7.5, fontweight='bold', ha='right', zorder=4)
    
    # Progress bar
    ax.plot([8.9, 14.9], [by + 0.58, by + 0.58], color='#e2e8f0', linewidth=6, zorder=3)
    ax.plot([8.9, 8.9 + (b_len * 1.2)], [by + 0.58, by + 0.58], color=b_col, linewidth=6, zorder=4)
    
    ax.text(8.9, by + 0.22, b_desc, color='#64748b', fontsize=6.8, zorder=4)

plt.tight_layout()
plt.savefig("assets/infographic_competitive_budget_16x9.png", dpi=220)
plt.close()

print("All 4 Proposal 16:9 widescreen infographics generated successfully!")
