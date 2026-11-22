"""
Generate 4 Master 16:9 Widescreen Technological Framework Infographics
following the Data Centers project aesthetic:
- 16:9 widescreen ratio (16 x 9 inches, 220 DPI = 3520 x 1980 4K UHD)
- Clean white & light-gray blueprint grid background
- Deep navy, royal blue, cyan, emerald green, amber/gold, and crimson corporate palette
- Distinct rounded cards (FancyBboxPatch), metric badges, flow vectors, and sharp engineering typography
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

def add_header(ax, title, subtitle, challenge_code="NESFIC-D-02 | GOVERNMENT TRACK"):
    # Header bar
    header_box = FancyBboxPatch((0.5, 7.85), 15.0, 0.85, boxstyle="round,pad=0.08,rounding_size=0.15",
                                facecolor='#0f3a42', edgecolor='#d4af37', linewidth=1.8, zorder=3)
    ax.add_patch(header_box)
    
    # Badges inside header
    dept_badge = FancyBboxPatch((0.7, 8.35), 4.2, 0.25, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor='#0b4d26', edgecolor='none', zorder=4)
    ax.add_patch(dept_badge)
    ax.text(2.8, 8.47, "GOVERNMENT OF ASSAM • IRRIGATION DEPARTMENT", color='#86efac', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=5)
    
    code_badge = FancyBboxPatch((12.2, 8.35), 3.1, 0.25, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor='#b45309', edgecolor='none', zorder=4)
    ax.add_patch(code_badge)
    ax.text(13.75, 8.47, challenge_code, color='#fef08a', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=5)
    
    # Title & Subtitle
    ax.text(0.7, 8.12, title, color='white', fontsize=15, fontweight='bold', va='center', zorder=5)
    ax.text(0.7, 7.94, subtitle, color='#cbd5e1', fontsize=9, va='center', zorder=5)

# ==============================================================================
# INFOGRAPHIC 1: Master Technological Digital Twin Architecture
# ==============================================================================
print("Generating Infographic 1: Master Architecture...")
fig, ax = setup_canvas()
add_header(ax, "NEERDRISHTI ASSAM: CYBER-PHYSICAL DIGITAL TWIN ARCHITECTURE",
           "End-to-End Technological Framework for Canal Condition Monitoring & Predictive Maintenance")

# Metric Badges Ribbon
badges = [
    ("MONITORED CANALS", "5,800+ km State Network", "#0284c7"),
    ("CONVEYANCE EFFICIENCY", "+21% Water Recovered", "#059669"),
    ("SEEPAGE LATENCY", "< 15 Min Detection", "#d97706"),
    ("EARLY BREACH WARNING", "14.5 Hours Lead Time", "#dc2626"),
    ("TOTAL GRANT BUDGET", "₹ 40.0 Lakhs (TRL-6)", "#7c3aed")
]
for i, (kpi, val, bg) in enumerate(badges):
    xp = 0.5 + (i * 3.05)
    b_patch = FancyBboxPatch((xp, 7.2), 2.9, 0.52, boxstyle="round,pad=0.04,rounding_size=0.1",
                             facecolor='white', edgecolor=bg, linewidth=1.5, zorder=3)
    ax.add_patch(b_patch)
    # colored left bar
    l_bar = FancyBboxPatch((xp, 7.2), 0.15, 0.52, boxstyle="round,pad=0.01,rounding_size=0.05",
                           facecolor=bg, edgecolor='none', zorder=4)
    ax.add_patch(l_bar)
    ax.text(xp + 0.3, 7.55, kpi, color='#64748b', fontsize=7, fontweight='bold', zorder=4)
    ax.text(xp + 0.3, 7.33, val, color='#0f172a', fontsize=9.5, fontweight='bold', zorder=4)

# 4 Horizontal Architectural Tiers
layers = [
    ("TIER 4: DEPARTMENTAL GOVERNANCE & FIELD ACTION",
     "Executive Engineer (EE) GIS Canvas • Automated E-Nirman Work Orders via Assam PWD SOR • Mobile Offline Inspection App • Farmer WUA Equity Telemetry",
     [("State GIS Command Console", "Real-time reach health & breach triage map", "#0f3a42"),
      ("E-Nirman SOR Generator", "Instant BoQ estimation (geo-bags, rip-rap)", "#0284c7"),
      ("Mobile Field Inspection App", "Offline GPS-geotagged repair validation", "#059669"),
      ("Farmer Water Equity Portal", "Tail-end delivery equity index (DEI)", "#7c3aed")],
     5.35, 1.65, "#f3e8ff", "#6b21a8"),
    
    ("TIER 3: AI DIGITAL TWIN & PREDICTIVE PHYSICS ENGINE",
     "1D Saint-Venant Mass Balance Transit Loss Solver • Bishop Slope Stability Early Breach Predictor • Random Forest Asset Health Index (AHI)",
     [("Hydrodynamic Mass Balance", "Continuous ΔQ loss isolating abnormal piping", "#0284c7"),
      ("Bishop Slope Stability FoS", "Real-time Factor of Safety < 1.15 alert", "#dc2626"),
      ("Asset Health Index (AHI)", "Multivariate scoring (0-100) per 500m", "#b45309"),
      ("Automated Sluice Advisory", "Upstream throttling recommendation", "#059669")],
     3.55, 1.65, "#fef3c7", "#b45309"),
    
    ("TIER 2: EARTH OBSERVATION & AUTONOMOUS UAV PATROLS",
     "ESA Sentinel-2 Multispectral 10m NDWI Corridor Analysis • YOLOv8-Seg Computer Vision for Structural Crack, Scour & Weed Classification",
     [("Sentinel-2 NDWI Seepage", "100m canal buffer subsurface moisture plume", "#059669"),
      ("UAV Drone Video Patrols", "High-res RGB photogrammetry (4K/30fps)", "#0284c7"),
      ("YOLOv8 Defect Detection", "Automated crack, scour & weed segmentation", "#dc2626"),
      ("Bathymetric Silt Profiler", "Acoustic sediment bed rise quantitation", "#0f3a42")],
     1.75, 1.65, "#ecfdf5", "#047857"),
    
    ("TIER 1: EDGE HYDROLOGICAL & GEOTECHNICAL SENSING ARRAY",
     "Non-Contact IP68 Ultrasonic Water Level Transmitters • Acoustic Doppler Flow Meters • Vibrating-Wire Dyke Piezometers • Solar LoRaWAN/4G RTU",
     [("Ultrasonic Level Transmitters", "Non-contact, 0.3-8m range, ±1mm accuracy", "#0284c7"),
      ("Acoustic Doppler Velocimeters", "Bed-mounted bi-directional discharge gauge", "#0369a1"),
      ("Vibrating-Wire Piezometers", "Dyke toe pore-water pressure (0-200 kPa)", "#dc2626"),
      ("Solar LoRa/4G Edge RTU", "50W solar, LiFePO4, 30-day flash buffering", "#b45309")],
     -0.05, 1.65, "#e0f2fe", "#0369a1")
]

for title, desc, subcards, y_pos, height, bg_col, border_col in layers:
    # Outer Layer Card
    p = FancyBboxPatch((0.5, y_pos), 15.0, height, boxstyle="round,pad=0.05,rounding_size=0.12",
                       facecolor=bg_col, edgecolor=border_col, linewidth=1.6, zorder=2)
    ax.add_patch(p)
    
    # Layer Title Tag
    t_tag = FancyBboxPatch((0.7, y_pos + height - 0.3), 6.5, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor=border_col, edgecolor='none', zorder=3)
    ax.add_patch(t_tag)
    ax.text(3.95, y_pos + height - 0.17, title, color='white', fontsize=8, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(7.4, y_pos + height - 0.17, desc, color='#334155', fontsize=7.2, va='center', zorder=4)
    
    # Sub-cards
    for j, (sc_title, sc_desc, sc_col) in enumerate(subcards):
        cx = 0.7 + (j * 3.65)
        cy = y_pos + 0.12
        card = FancyBboxPatch((cx, cy), 3.45, 0.88, boxstyle="round,pad=0.03,rounding_size=0.08",
                              facecolor='white', edgecolor=sc_col, linewidth=1.2, zorder=3)
        ax.add_patch(card)
        
        # Pill indicator
        ax.add_patch(Circle((cx + 0.25, cy + 0.68), 0.08, facecolor=sc_col, zorder=4))
        ax.text(cx + 0.45, cy + 0.68, sc_title, color='#0f172a', fontsize=8.5, fontweight='bold', va='center', zorder=4)
        ax.text(cx + 0.45, cy + 0.35, sc_desc, color='#64748b', fontsize=7, va='center', zorder=4, wrap=True)

# Upward flow arrows between layers
for arrow_y in [1.63, 3.43, 5.23]:
    ax.annotate('', xy=(8.0, arrow_y + 0.12), xytext=(8.0, arrow_y - 0.04),
                arrowprops=dict(facecolor='#0f3a42', edgecolor='#0f3a42', arrowstyle="->", lw=2.2), zorder=5)
    ax.annotate('', xy=(4.0, arrow_y + 0.12), xytext=(4.0, arrow_y - 0.04),
                arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="->", lw=1.8), zorder=5)
    ax.annotate('', xy=(12.0, arrow_y + 0.12), xytext=(12.0, arrow_y - 0.04),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', arrowstyle="->", lw=1.8), zorder=5)

plt.tight_layout()
plt.savefig("assets/infographic_master_architecture_16x9.png", dpi=220)
plt.close()

# ==============================================================================
# INFOGRAPHIC 2: Saint-Venant Hydraulic Mass-Balance & Seepage Localization
# ==============================================================================
print("Generating Infographic 2: Hydraulic Mass Balance...")
fig, ax = setup_canvas()
add_header(ax, "SAINT-VENANT DYNAMIC HYDRAULIC MASS-BALANCE & SEEPAGE DETECTION ENGINE",
           "Continuous Reach-by-Reach Discharge Balancing Isolating Abnormal Conveyance Deficits (Jamuna Scheme RD 0-28.5 km)")

# Top Equation Banner
eq_patch = FancyBboxPatch((0.5, 6.75), 15.0, 0.95, boxstyle="round,pad=0.05,rounding_size=0.12",
                          facecolor='#0f172a', edgecolor='#0284c7', linewidth=1.5, zorder=3)
ax.add_patch(eq_patch)
ax.text(0.8, 7.45, "SAINT-VENANT CONTINUOUS MASS-CONSERVATION BALANCE EQUATION:", color='#38bdf8', fontsize=8.5, fontweight='bold', zorder=4)
ax.text(0.8, 7.15, "ΔQ_abnormal(t) = Q_headworks(t) - Σ Q_authorized_offtakes(t) - Q_tail_measured(t) - [ K_seep · P_wet · ΔL + E(t) · W_top · ΔL ]",
        color='#f8fafc', fontfamily='monospace', fontsize=10.5, fontweight='bold', zorder=4)
ax.text(0.8, 6.88, "Where K_seep is reach permeability coefficient (IS:9452), P_wet is wetted perimeter, E(t) is Penman-Monteith open evaporation, and W_top is canal top width.",
        color='#94a3b8', fontsize=7.2, zorder=4)

# Canal Reach Longitudinal Flow Visualization
flow_patch = FancyBboxPatch((0.5, 3.85), 15.0, 2.75, boxstyle="round,pad=0.05,rounding_size=0.12",
                            facecolor='white', edgecolor='#cbd5e1', linewidth=1.5, zorder=2)
ax.add_patch(flow_patch)
ax.text(0.8, 6.35, "JAMUNA IRRIGATION SCHEME: LONGITUDINAL REACH DISCHARGE & SEEPAGE PROFILING", color='#0f172a', fontsize=9.5, fontweight='bold', zorder=3)

# 4 Reach Stage Cards
stages = [
    ("HEADWORKS INFLOW (Q_in)", "Bakulia Barrage Head Regulator (RD 0.0 km)\n• Measured Q: 498.5 cusecs\n• Design Depth: 2.60 m (Water level 2.45m)\n• Status: Intact Masonry Lining", "#0284c7", 0.8),
    ("AUTHORIZED OFFTAKES (Σ Q_off)", "Distributaries D1 to D7 Offtakes (RD 6.5 km)\n• Total Allocated: 185.0 cusecs\n• Regulated Gate Positions Telemetry\n• Status: Legal Crop Allocation", "#64748b", 4.5),
    ("ABNORMAL PIPING SEEPAGE", "Doboka Section Embankment (RD 9.1 km)\n• Unaccounted Deficit: 62.5 cusecs\n• High Pore Pressure: 42 kPa | Fracture 35mm\n• STATUS: CRITICAL SEEPAGE FLAG", "#dc2626", 8.2),
    ("TAIL-END DELIVERY (Q_tail)", "Kaki Branch Distributary (RD 28.5 km)\n• Actual Tail Delivery: 178.0 cusecs\n• Tail Delivery Equity (DEI): 56.8%\n• STATUS: WATER DEFICIT (4,200 Farmers)", "#d97706", 11.9)
]

for title, desc, col, x in stages:
    card = FancyBboxPatch((x, 4.05), 3.3, 2.05, boxstyle="round,pad=0.04,rounding_size=0.08",
                          facecolor='#f8fafc', edgecolor=col, linewidth=1.6, zorder=3)
    ax.add_patch(card)
    tag = FancyBboxPatch((x + 0.1, 5.75), 3.1, 0.26, boxstyle="round,pad=0.02,rounding_size=0.05",
                         facecolor=col, edgecolor='none', zorder=4)
    ax.add_patch(tag)
    ax.text(x + 1.65, 5.88, title, color='white', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(x + 0.2, 4.85, desc, color='#334155', fontsize=7.2, va='center', zorder=4)

# Connectors between stages
for cx in [4.2, 7.9, 11.6]:
    ax.annotate('', xy=(cx + 0.25, 5.0), xytext=(cx - 0.1, 5.0),
                arrowprops=dict(facecolor='#0f3a42', arrowstyle="->", lw=2.5), zorder=5)

# Bottom Split Panels: Left (Satellite NDWI Heatmap), Right (Water Equity Impact)
left_p = FancyBboxPatch((0.5, 0.3), 7.3, 3.35, boxstyle="round,pad=0.05,rounding_size=0.12",
                        facecolor='#0f172a', edgecolor='#38bdf8', linewidth=1.4, zorder=2)
ax.add_patch(left_p)
ax.text(0.8, 3.35, "SATELLITE CORRIDOR: SENTINEL-2 NDWI MOISTURE PLUME", color='#38bdf8', fontsize=8.5, fontweight='bold', zorder=3)

# Inset plot for satellite heatmap
if os.path.exists("assets/satellite_seepage_ndvi.png"):
    img_sat = plt.imread("assets/satellite_seepage_ndvi.png")
    ax.imshow(img_sat, extent=[0.7, 7.5, 0.45, 3.1], zorder=3, aspect='auto')

# Right Panel: Water Equity & WUA Recovery
right_p = FancyBboxPatch((8.2, 0.3), 7.3, 3.35, boxstyle="round,pad=0.05,rounding_size=0.12",
                         facecolor='white', edgecolor='#059669', linewidth=1.4, zorder=2)
ax.add_patch(right_p)
ax.text(8.5, 3.35, "WATER USERS' ASSOCIATION (WUA) BENEFIT & RECOVERY METRICS", color='#059669', fontsize=8.5, fontweight='bold', zorder=3)

# 3 metric summary rows
recovery_metrics = [
    ("Conveyance Loss Reduction:", "Recovering 28 cusecs (+21% efficiency gain) directly into tail reaches", "#059669"),
    ("Command Area Expansion:", "Supplying 4,500 additional hectares of Boro paddy across 14 Gaon Panchayats", "#0284c7"),
    ("Automated Remedial Tender:", "Pre-calculated Bill of Quantities (BoQ) dispatched via E-Nirman within 24h", "#7c3aed")
]
for idx, (m_title, m_desc, m_col) in enumerate(recovery_metrics):
    my = 2.4 - (idx * 0.95)
    m_box = FancyBboxPatch((8.5, my), 6.7, 0.75, boxstyle="round,pad=0.03,rounding_size=0.06",
                           facecolor='#f8fafc', edgecolor=m_col, linewidth=1.2, zorder=3)
    ax.add_patch(m_box)
    ax.text(8.7, my + 0.52, m_title, color=m_col, fontsize=8, fontweight='bold', zorder=4)
    ax.text(8.7, my + 0.22, m_desc, color='#334155', fontsize=7.2, zorder=4)

plt.tight_layout()
plt.savefig("assets/infographic_hydraulic_loss_engine_16x9.png", dpi=220)
plt.close()

# ==============================================================================
# INFOGRAPHIC 3: Geotechnical Embankment Breach Prediction & Early Warning
# ==============================================================================
print("Generating Infographic 3: Geotechnical Breach Prediction...")
fig, ax = setup_canvas()
add_header(ax, "GEOTECHNICAL EMBANKMENT BREACH PREDICTION & EARLY WARNING HORIZON",
           "Coupled Transient Pore-Water Pressure Modeling & Bishop Factor of Safety Dynamics (Dhansiri RD 14.2 km)")

# Top Warning Horizon Banner
warn_patch = FancyBboxPatch((0.5, 6.75), 15.0, 0.95, boxstyle="round,pad=0.05,rounding_size=0.12",
                           facecolor='#7f1d1d', edgecolor='#ef4444', linewidth=1.8, zorder=3)
ax.add_patch(warn_patch)
ax.text(0.8, 7.42, "CRITICAL DISASTER MITIGATION HORIZON: 14.5 HOURS PREDICTIVE LEAD TIME", color='#fef08a', fontsize=10, fontweight='bold', zorder=4)
ax.text(0.8, 7.12, "Autonomous early warning alerts the Executive Engineer before backward piping shear failure occurs, preventing the inundation of 1,200 hectares of cropland.",
        color='white', fontsize=8, zorder=4)
ax.text(0.8, 6.88, "Algorithmic Model: Modified Bishop Limit-Equilibrium Slope Stability Method coupled with Transient Dyke Pore-Water Pressure Telemetry.",
        color='#fca5a5', fontsize=7.2, zorder=4)

# Left: 24h Early Breach Curve Graph Inset
left_chart = FancyBboxPatch((0.5, 0.3), 7.8, 6.25, boxstyle="round,pad=0.05,rounding_size=0.12",
                            facecolor='white', edgecolor='#cbd5e1', linewidth=1.5, zorder=2)
ax.add_patch(left_chart)
ax.text(0.8, 6.25, "TRANSIENT PORE PRESSURE VS. BISHOP FACTOR OF SAFETY (FoS)", color='#0f172a', fontsize=9, fontweight='bold', zorder=3)

if os.path.exists("assets/breach_forecasting_curve.png"):
    img_curve = plt.imread("assets/breach_forecasting_curve.png")
    ax.imshow(img_curve, extent=[0.7, 8.1, 0.45, 6.0], zorder=3, aspect='auto')

# Right: Technical CAD Cutaway & Sluice Advisory Card
right_cad = FancyBboxPatch((8.6, 2.7), 6.9, 3.85, boxstyle="round,pad=0.05,rounding_size=0.12",
                           facecolor='white', edgecolor='#cbd5e1', linewidth=1.5, zorder=2)
ax.add_patch(right_cad)
ax.text(8.9, 6.25, "EMBANKMENT CROSS-SECTION & SENSOR TELEMETRY TOPOLOGY", color='#0f172a', fontsize=9, fontweight='bold', zorder=3)

if os.path.exists("assets/iot_edge_hardware_schematic.png"):
    img_cad = plt.imread("assets/iot_edge_hardware_schematic.png")
    ax.imshow(img_cad, extent=[8.8, 15.3, 2.85, 6.0], zorder=3, aspect='auto')

# Bottom Right: Automated Sluice Gate Action Card
action_patch = FancyBboxPatch((8.6, 0.3), 6.9, 2.25, boxstyle="round,pad=0.05,rounding_size=0.12",
                              facecolor='#0f172a', edgecolor='#d4af37', linewidth=1.5, zorder=2)
ax.add_patch(action_patch)
ax.text(8.9, 2.25, "AUTOMATED DECISION SUPPORT: SLUICE GATE MITIGATION ADVISORY", color='#d4af37', fontsize=8.5, fontweight='bold', zorder=3)

advisories = [
    ("Action 1 (Barrage Throttling):", "Throttle Bhairabkunda head regulator gates by -350 cusecs to dissipate hydrostatic pressure.", "#38bdf8"),
    ("Action 2 (Civil Defense Dispatch):", "Dispatch 450 geo-textile bags and boulder rip-rap to embankment toe at RD 14.2 km.", "#4ade80"),
    ("Action 3 (E-Nirman Emergency Ticket):", "Pre-approved emergency requisition code generated for Udalguri Irrigation Division EE.", "#facc15")
]
for idx, (a_title, a_desc, a_col) in enumerate(advisories):
    ay = 1.7 - (idx * 0.58)
    ax.text(8.9, ay + 0.12, a_title, color=a_col, fontsize=7.5, fontweight='bold', zorder=4)
    ax.text(8.9, ay - 0.08, a_desc, color='#cbd5e1', fontsize=7, zorder=4)

plt.tight_layout()
plt.savefig("assets/infographic_breach_forecasting_geotech_16x9.png", dpi=220)
plt.close()

# ==============================================================================
# INFOGRAPHIC 4: YOLOv8 Computer Vision Defect Classification Matrix
# ==============================================================================
print("Generating Infographic 4: Computer Vision Defect Matrix...")
fig, ax = setup_canvas()
add_header(ax, "YOLOv8 & MASK-RCNN CANAL STRUCTURAL DEFECT CLASSIFICATION MATRIX",
           "Autonomous Computer Vision Triage, Geometrical Quantitation & Assam Irrigation SOR Remediation")

# 4 Quadrants for the 4 primary defect categories
quadrants = [
    ("DEFECT CLASS 1: EMBANKMENT SCOUR & TOE SLUMP",
     "Visual Symptoms: Toe erosion, rotational slump slip, gully incisions along alluvial dykes\n"
     "AI Model: YOLOv8-Seg (Polygon Segmentation) | Validation mAP@50: 96.4%\n"
     "Geometric Metric: Length: 14.5m, Scour Depth: 1.2m, Soil Loss: 42.0 m³\n"
     "Assam SOR Remediation: Geo-textile sandbag pitching, boulder rip-rap dumping & compaction\n"
     "Estimated Unit Cost: ₹ 3,85,000 (Udalguri Irrigation Division)",
     "#dc2626", "#fee2e2", 0.5, 3.8),
    
    ("DEFECT CLASS 2: CONCRETE LINING FRACTURE & CAVITATION",
     "Visual Symptoms: Longitudinal crack aperture > 25mm, joint separation, sub-base piping\n"
     "AI Model: Mask-RCNN CrackNet | Validation mAP@50: 92.1%\n"
     "Geometric Metric: Longitudinal crack 8.4m length, aperture 35mm, depth 180mm\n"
     "Assam SOR Remediation: Polymer-modified mortar pressure grouting & elastomeric sealant\n"
     "Estimated Unit Cost: ₹ 1,42,000 (Hojai Irrigation Division)",
     "#b45309", "#fef3c7", 8.2, 3.8),
    
    ("DEFECT CLASS 3: AQUATIC WEED & HYACINTH CHOKING",
     "Visual Symptoms: Dense water hyacinth (Eichhornia crassipes) surface mats choking velocity\n"
     "AI Model: YOLOv8 Object Detection + Sentinel-2 NDWI | mAP@50: 98.2%\n"
     "Geometric Metric: Continuous hyacinth mat spanning 450m length (100% surface choke)\n"
     "Assam SOR Remediation: Amphibious mechanical weed harvester & manual disposal squad\n"
     "Estimated Unit Cost: ₹ 85,000 (Kaki Sub-Division Section)",
     "#047857", "#ecfdf5", 0.5, 0.4),
    
    ("DEFECT CLASS 4: HEAVY SILT DEPOSITION & BED RISE",
     "Visual Symptoms: Sand bar formation, loss of hydraulic radius, reverse bed slopes\n"
     "AI Model: Acoustic Doppler Profiler + CV Bathymetric Model | mAP@50: 91.5%\n"
     "Geometric Metric: Silt deposition depth: 0.85m to 1.15m | Discharge reduction: -28%\n"
     "Assam SOR Remediation: Targeted mechanical desiltation tender work-order\n"
     "Estimated Unit Cost: ₹ 2,15,000 (Naokata Section, Sukla Scheme)",
     "#0369a1", "#e0f2fe", 8.2, 0.4)
]

for title, content, border_col, bg_col, qx, qy in quadrants:
    q_patch = FancyBboxPatch((qx, qy), 7.3, 3.2, boxstyle="round,pad=0.05,rounding_size=0.12",
                            facecolor=bg_col, edgecolor=border_col, linewidth=1.6, zorder=2)
    ax.add_patch(q_patch)
    
    # Header tag
    tag = FancyBboxPatch((qx + 0.1, qy + 2.8), 7.1, 0.32, boxstyle="round,pad=0.02,rounding_size=0.06",
                         facecolor=border_col, edgecolor='none', zorder=3)
    ax.add_patch(tag)
    ax.text(qx + 3.65, qy + 2.96, title, color='white', fontsize=7.8, fontweight='bold', ha='center', va='center', zorder=4)
    
    # Internal white details card
    i_card = FancyBboxPatch((qx + 0.2, qy + 0.18), 6.9, 2.5, boxstyle="round,pad=0.03,rounding_size=0.08",
                            facecolor='white', edgecolor=border_col, linewidth=1.0, zorder=3)
    ax.add_patch(i_card)
    
    lines = content.split("\n")
    for l_idx, line in enumerate(lines):
        ly = qy + 2.35 - (l_idx * 0.48)
        if ":" in line:
            label, val = line.split(":", 1)
            ax.text(qx + 0.4, ly, label + ":", color='#0f172a', fontsize=7.5, fontweight='bold', zorder=4)
            ax.text(qx + 0.4 + (len(label)*0.09) + 0.1, ly, val, color='#334155', fontsize=7.2, zorder=4)
        else:
            ax.text(qx + 0.4, ly, line, color='#334155', fontsize=7.2, zorder=4)

plt.tight_layout()
plt.savefig("assets/infographic_cv_defect_matrix_16x9.png", dpi=220)
plt.close()

print("All 4 master 16:9 widescreen technological infographics generated successfully!")
