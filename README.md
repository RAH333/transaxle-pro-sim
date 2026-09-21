# transaxle-pro-sim
mechanical engineering relies on python scripts for simulation, data visualization, and calculation validation, this project will compute Transaxle Gear Parameters, Bearing Reliability, and DFMEA Risk Matrices directly via code.

# Transaxle Architecture Calculation & Prototyping Engine (`transaxle-pro-sim`)

A comprehensive mechanical engineering automation suite designed to simulate structural loading limits, layout tolerances, and mechanical lifetimes across key components of an automotive/tractor multi-speed transaxle system. 

This programmatic layout mirrors the mathematical engine foundational to enterprise utilities like **ROMAX** and **Kisssoft**, providing analytical verification across physical design elements.

## Key Solvers Engineered

1. **Gear Mesh Optimization Engine (`gear_mesh_calc.py`)**: Computes tooth-bending stresses using parametric input variables to balance target transmission layouts safely under maximum output torque.
2. **Shaft Deflection Profiler (`shaft_deflection.py`)**: Models safe shaft diameters against combined torque profiles and bending loops under heavy-duty low-gear loading steps.
3. **Bearing Fatigue Analyzer (`bearing_lifecycle.py`)**: Evaluates basic L10 mechanical lifetimes for high-capacity tapered roller configurations using standard dynamic loading vectors.
4. **DFMEA Generator Engine (`dfmea_matrix.py`)**: Automatically traces, handles, and builds structured Risk Priority Number (RPN) tables matching standard manufacturing quality criteria.

## Execution & Deployment Guide

To run local calculation modules inside your environment, configure and deploy utilizing the steps listed below:

```bash
# Clone the calculation suite
git clone https://github.com
cd transaxle-pro-sim

# Set up project dependency tracking
pip install -r requirements.txt

# Run complete gear calculation solver checks
python core_solvers/gear_mesh_calc.py
python core_solvers/shaft_deflection.py
python core_solvers/bearing_lifecycle.py

# Run standard corporate failure risk engine reports
python analytical_tools/dfmea_matrix.py
```


```
transaxle-pro-sim/
│
├── README.md                 # Project Overview, Equations, Layout Specs & Guide
├── requirements.txt          # Python dependencies (numpy, tabulate)
│
├── core_solvers/
│   ├── __init__.py           
│   ├── gear_mesh_calc.py     # Solves tooth stresses, bending limits, and geometries
│   ├── shaft_deflection.py   # Computes bending moments and minimum shaft diameter
│   └── bearing_lifecycle.py  # Calculates dynamic load capacities and L10 lifecycles
│
└── analytical_tools/
    ├── __init__.py           
    └── dfmea_matrix.py       # Auto-generates Transaxle RPN (Risk Priority Numbers)
```
