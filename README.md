# transaxle-pro-sim
mechanical engineering relies on python scripts for simulation, data visualization, and calculation validation, this project will compute Transaxle Gear Parameters, Bearing Reliability, and DFMEA Risk Matrices directly via code.

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
