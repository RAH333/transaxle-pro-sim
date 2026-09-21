import math
from tabulate import tabulate

def analyze_tolerance_stackup(components):
    """
    Performs Worst-Case and Statistical (Root-Sum-Square / RSS) Tolerance 
    Stack-up Analysis for a transaxle assembly (e.g., casing, shaft lengths, bearings, shims).
    
    Expects a dictionary where:
    Key = Component Name
    Value = (Nominal Dimension in mm, Symmetric Tolerance in mm, Sign [1 for addition, -1 for subtraction])
    """
    total_nominal = 0.0
    worst_case_tolerance = 0.0
    rss_tolerance_squared = 0.0
    
    table_rows = []
    
    for name, (nominal, tolerance, sign) in components.items():
        directed_nominal = nominal * sign
        total_nominal += directed_nominal
        worst_case_tolerance += abs(tolerance)
        rss_tolerance_squared += tolerance ** 2
        
        table_rows.append([
            name, 
            f"{nominal:.3f}", 
            f"±{tolerance:.3f}", 
            "+" if sign == 1 else "-"
        ])
        
    rss_tolerance = math.sqrt(rss_tolerance_squared)
    
    # Calculate operational clearance boundaries
    wc_min = total_nominal - worst_case_tolerance
    wc_max = total_nominal + worst_case_tolerance
    rss_min = total_nominal - rss_tolerance
    rss_max = total_nominal + rss_tolerance
    
    print("\n=================== TRANSAXLE ASSEMBLY TOLERANCE STACK REPORT ===================")
    print(tabulate(table_rows, headers=["Component Name", "Nominal (mm)", "Tolerance (mm)", "Loop Direction"], tablefmt="grid"))
    
    print(f"\n[Calculated Nominal Assembly Gap]: {total_nominal:.3f} mm")
    print(f"---------------------------------------------------------------------------------")
    print(f"🔴 WORST-CASE ANALYSIS (100% Interchangeability Profile):")
    print(f"   • Cumulative Loop Stack-up: ±{worst_case_tolerance:.3f} mm")
    print(f"   • Resulting Assembly Gap Range: [{wc_min:.3f} mm to {wc_max:.3f} mm]")
    
    print(f"\n🟢 STATISTICAL ANALYSIS (Root-Sum-Square / RSS Approach):")
    print(f"   • Cumulative Loop Stack-up: ±{rss_tolerance:.3f} mm")
    print(f"   • Resulting Assembly Gap Range: [{rss_min:.3f} mm to {rss_max:.3f} mm]")
    print(f"=================================================================================\n")

if __name__ == "__main__":
    # Simulation setup mimicking input shaft assembly axial clearances inside a housing casing
    # Structure: Component_Name: (Nominal_Dim, Tolerance, Loop_Sign)
    transaxle_axial_loop = {
        "Housing Casing Internal Width": (150.000, 0.080, 1),   # Base container gap
        "Input Shaft Shoulder Length":   (85.000, 0.050, -1),  # Subtracts space
        "Left Roller Bearing Width":     (22.000, 0.030, -1),  # Subtracts space
        "Right Roller Bearing Width":    (22.000, 0.030, -1),  # Subtracts space
        "Selected Selective Shim Spacer":(20.500, 0.015, -1)   # Subtracts space to leave clearance gap
    }
    
    analyze_tolerance_stackup(transaxle_axial_loop)
  
