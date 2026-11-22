"""
Domain Models and Analytical Formulations for NESFIC-D-02:
Irrigation Canals Condition Monitoring & Predictive Maintenance (Govt of Assam)
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from enum import Enum
from datetime import datetime

class RiskLevel(str, Enum):
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class DefectType(str, Enum):
    SEEPAGE = "Abnormal Seepage / Piping"
    EROSION = "Embankment Scouring / Slumping"
    CRACK = "Concrete Lining Fracture"
    SILTATION = "Heavy Silt Deposition"
    WEED = "Aquatic Weed / Hyacinth Clogging"
    UNAUTHORIZED_CUT = "Unauthorized Sluice / Cut"

class CanalSegment(BaseModel):
    id: str
    scheme_name: str
    canal_name: str
    reach_type: str  # Head-Reach, Mid-Reach, Tail-Reach
    chainage_start_km: float
    chainage_end_km: float
    design_discharge_cusecs: float
    current_discharge_cusecs: float
    water_level_m: float
    design_depth_m: float
    silt_depth_m: float
    pore_pressure_kpa: float
    seepage_rate_lps_per_km: float
    asset_health_index: float  # 0 to 100
    risk_level: RiskLevel
    detected_defects: List[DefectType]
    coordinates: List[List[float]]  # GeoJSON path [[lat, lon], ...]
    last_inspected: str

class TelemetryNode(BaseModel):
    node_id: str
    chainage_km: float
    location_name: str
    sensor_types: List[str]
    water_level_m: float
    flow_velocity_mps: float
    discharge_cusecs: float
    soil_moisture_pct: float
    pore_pressure_kpa: float
    battery_pct: float
    solar_status: str
    signal_strength_dbm: int
    last_ping: str
    status: str

class WorkOrder(BaseModel):
    id: str
    chainage_km: float
    location_name: str
    canal_name: str
    defect_type: DefectType
    severity: RiskLevel
    estimated_cost_inr: float
    assigned_division: str
    assigned_officer: str
    status: str  # OPEN, DISPATCHED, IN_PROGRESS, COMPLETED, VERIFIED
    created_at: str
    target_completion: str
    description: str

class HydroBalanceResult(BaseModel):
    scheme_name: str
    inflow_headworks_cusecs: float
    total_offtake_cusecs: float
    measured_tail_cusecs: float
    permissible_transit_loss_cusecs: float
    unaccounted_water_loss_cusecs: float
    loss_percentage: float
    tail_delivery_equity_ratio: float
    status: str
