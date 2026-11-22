"""
Generate high-resolution charts and diagrams for the Proof of Work PDF.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("assets", exist_ok=True)

# 1. Hydraulic Mass Balance Chart
plt.figure(figsize=(7, 3.8), dpi=200)
categories = ['Head Inflow\n(Bakulia)', 'Authorized\nOfftakes', 'Tail Delivery\n(Kaki Branch)', 'Permissible\nLoss (IS:9452)', 'Unaccounted\nSeepage / Loss']
values = [498.5, 185.0, 178.0, 35.0, 100.5]
colors = ['#0284c7', '#64748b', '#059669', '#d97706', '#dc2626']

bars = plt.bar(categories, values, color=colors, width=0.55, edgecolor='#1e293b', linewidth=1)
plt.ylabel('Discharge Rate (Cusecs)', fontsize=10, fontweight='bold', color='#1e293b')
plt.title('Jamuna Irrigation Scheme - Reach RD 0.0 to 28.5 km Hydraulic Mass Balance', fontsize=11, fontweight='bold', pad=12, color='#0f172a')
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 10, f'{yval} cfs', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.ylim(0, 560)
plt.tight_layout()
plt.savefig("assets/hydro_mass_balance_chart.png")
plt.close()

# 2. Asset Health Index vs Pore Pressure
plt.figure(figsize=(7, 3.8), dpi=200)
chainages = np.array([0, 4, 8, 12, 14.2, 18, 22, 28.5])
ahi_scores = np.array([92, 88, 74, 52, 36, 42, 60, 41])
pore_pressure = np.array([16, 19, 32, 48, 68, 55, 38, 22])

fig, ax1 = plt.subplots(figsize=(7, 3.8), dpi=200)

color = '#0284c7'
ax1.set_xlabel('Canal Chainage RD (km)', fontweight='bold', fontsize=10)
ax1.set_ylabel('Asset Health Index (0-100)', color=color, fontweight='bold', fontsize=10)
line1 = ax1.plot(chainages, ahi_scores, color=color, marker='o', linewidth=2.5, label='Asset Health Index (AHI)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(20, 100)
ax1.axhspan(20, 50, color='#fee2e2', alpha=0.5, label='Critical Breach Risk Zone')
ax1.grid(True, linestyle=':', alpha=0.6)

ax2 = ax1.twinx()
color = '#dc2626'
ax2.set_ylabel('Soil Pore Pressure (kPa)', color=color, fontweight='bold', fontsize=10)
line2 = ax2.plot(chainages, pore_pressure, color=color, marker='s', linestyle='--', linewidth=2.5, label='Embankment Pore Pressure')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(10, 85)

plt.title('Chainage Profile: Asset Health vs Embankment Pore Pressure (Dhansiri Main Canal)', fontsize=11, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig("assets/canal_health_chart.png")
plt.close()

# 3. System Architecture Diagram
fig, ax = plt.subplots(figsize=(8, 4.2), dpi=200)
ax.axis('off')

# Layer boxes
boxes = [
    ("LAYER 1: SENSING & TELEMETRY EDGE", ["Ultrasonic Water Level", "Acoustic Doppler Flow", "Soil Pore Piezometers", "Solar LoRa/4G Nodes"], 0.05, 0.68, 0.4, 0.26, '#e0f2fe', '#0369a1'),
    ("LAYER 2: REMOTE SENSING & DRONES", ["Sentinel-2 NDVI/NDWI", "PlanetScope 3m Seepage", "UAV RGB Drone Patrols", "YOLOv8 Crack & Weed CV"], 0.55, 0.68, 0.4, 0.26, '#ecfdf5', '#047857'),
    ("LAYER 3: AI & DIGITAL TWIN ENGINE", ["Saint-Venant Hydrodynamic 1D Model", "Mass Balance Seepage Detection", "Geotech Bishop Slope Stability", "Predictive Failure Classifier"], 0.05, 0.36, 0.9, 0.24, '#fef3c7', '#b45309'),
    ("LAYER 4: DECISION SUPPORT & GOV INTERACTION", ["Assam State GIS Dashboard", "E-Nirman Automated Work Orders", "WhatsApp/SMS Alert Gateway", "Farmer Water Equity Tracker"], 0.05, 0.04, 0.9, 0.24, '#f3e8ff', '#6b21a8')
]

for title, items, x, y, w, h, bg, border in boxes:
    rect = plt.Rectangle((x, y), w, h, facecolor=bg, edgecolor=border, linewidth=1.5, transform=ax.transAxes, zorder=2)
    ax.add_patch(rect)
    ax.text(x + 0.02, y + h - 0.06, title, fontsize=9.5, fontweight='bold', color=border, transform=ax.transAxes, zorder=3)
    item_str = " • ".join(items)
    ax.text(x + 0.02, y + 0.06, item_str, fontsize=8.2, color='#1e293b', transform=ax.transAxes, zorder=3, wrap=True)

# Add connector arrows
ax.annotate('', xy=(0.5, 0.63), xytext=(0.5, 0.68), arrowprops=dict(facecolor='#64748b', arrowstyle="->", lw=2), transform=ax.transAxes)
ax.annotate('', xy=(0.5, 0.31), xytext=(0.5, 0.36), arrowprops=dict(facecolor='#64748b', arrowstyle="->", lw=2), transform=ax.transAxes)

plt.title('NeerDrishti Assam - End-to-End System Architecture (NESFIC-D-02)', fontsize=11, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig("assets/architecture_diagram.png")
plt.close()

# 4. Wireframe Layout
fig, ax = plt.subplots(figsize=(8, 4.2), dpi=200)
ax.axis('off')

# Outer container
rect = plt.Rectangle((0.02, 0.02), 0.96, 0.96, facecolor='#f8fafc', edgecolor='#334155', linewidth=2, transform=ax.transAxes)
ax.add_patch(rect)

# Top Bar
rect_top = plt.Rectangle((0.02, 0.84), 0.96, 0.14, facecolor='#0f3a42', edgecolor='#d4af37', linewidth=1.5, transform=ax.transAxes)
ax.add_patch(rect_top)
ax.text(0.05, 0.91, "NeerDrishti Assam | Irrigation Dept, Govt of Assam [NESFIC-D-02]", color='white', fontsize=9.5, fontweight='bold', transform=ax.transAxes)
ax.text(0.05, 0.86, "State Command Dashboard • Telemetry Active • Live ASDC Sync", color='#cbd5e1', fontsize=7.5, transform=ax.transAxes)

# KPI row
for i, (kpi, val) in enumerate([("Monitored Length", "84.5 km"), ("Asset Health", "61.7/100"), ("Breach Alerts", "1 Active"), ("Tail Equity", "68.4%"), ("Water Saved", "34.6 MLD"), ("Work Orders", "3 Dispatched")]):
    xp = 0.04 + (i * 0.155)
    rect_k = plt.Rectangle((xp, 0.70), 0.14, 0.11, facecolor='white', edgecolor='#cbd5e1', linewidth=1, transform=ax.transAxes)
    ax.add_patch(rect_k)
    ax.text(xp + 0.01, 0.77, kpi, fontsize=6.5, color='#64748b', fontweight='bold', transform=ax.transAxes)
    ax.text(xp + 0.01, 0.72, val, fontsize=8, color='#0f172a', fontweight='bold', transform=ax.transAxes)

# Left: GIS Canal Map
rect_map = plt.Rectangle((0.04, 0.06), 0.58, 0.61, facecolor='#0f172a', edgecolor='#cbd5e1', linewidth=1, transform=ax.transAxes)
ax.add_patch(rect_map)
ax.text(0.06, 0.62, "GIS DIGITAL TWIN & REAL-TIME REACH TELEMETRY", color='#38bdf8', fontsize=8, fontweight='bold', transform=ax.transAxes)
ax.text(0.06, 0.48, "[Interactive Canal Chainage Line RD 0.0 -> RD 28.5 km]", color='#94a3b8', fontsize=7.5, transform=ax.transAxes)
ax.text(0.06, 0.38, "RD 0.0 - 6.5: Green (AHI 88.5)", color='#4ade80', fontsize=7, transform=ax.transAxes)
ax.text(0.06, 0.30, "RD 6.5 - 15.0: Amber (AHI 54.0 - Seepage 8.4 L/s/km)", color='#facc15', fontsize=7, transform=ax.transAxes)
ax.text(0.06, 0.22, "RD 14.2: RED (AHI 36.0 - High Pore Pressure 68 kPa)", color='#f87171', fontsize=7, fontweight='bold', transform=ax.transAxes)
ax.text(0.06, 0.14, "RD 15.0 - 28.5: Amber (AHI 41.5 - Silt Deposition 1.15m)", color='#facc15', fontsize=7, transform=ax.transAxes)

# Right: Work Orders & Alerts
rect_orders = plt.Rectangle((0.64, 0.06), 0.32, 0.61, facecolor='white', edgecolor='#cbd5e1', linewidth=1, transform=ax.transAxes)
ax.add_patch(rect_orders)
ax.text(0.66, 0.62, "PREDICTIVE WORK ORDERS", color='#0f172a', fontsize=8, fontweight='bold', transform=ax.transAxes)
ax.text(0.66, 0.54, "WO-041: Dhansiri RD 14.2 km\n• Slumping Breach | Est: ₹3.85L\n• Status: Dispatched (Udalguri Div)", color='#dc2626', fontsize=7, transform=ax.transAxes)
ax.text(0.66, 0.40, "WO-038: Jamuna RD 9.1 km\n• Lining Fracture | Est: ₹1.42L\n• Status: In Progress (Hojai Div)", color='#d97706', fontsize=7, transform=ax.transAxes)
ax.text(0.66, 0.26, "WO-035: Jamuna RD 18.5 km\n• Weed Clearance | Est: ₹85K\n• Status: Open (Kaki Sec)", color='#0284c7', fontsize=7, transform=ax.transAxes)
ax.text(0.66, 0.12, "[+ Create New Work Order (E-Nirman)]", color='#047857', fontsize=7, fontweight='bold', transform=ax.transAxes)

plt.title('NeerDrishti Assam - UI Wireframe & Operator Workflow Layout', fontsize=11, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig("assets/wireframe_schematic.png")
plt.close()

print("All charts and diagrams successfully generated in assets/!")
