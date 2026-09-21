import math

def analyze_tolerance_stackup(components):
    total_nominal = 0.0
    worst_case_tolerance = 0.0
    rss_tolerance_squared = 0.0
    
    header = f"| {'Component Name':<32} | {'Nominal (mm)':<13} | {'Tolerance':<10} | {'Direction':<9} |"
    divider = "-" * len(header)
    
    print("\n=================== TRANSAXLE ASSEMBLY TOLERANCE STACK REPORT ===================")
    print(divider)
    print(header)
    print(divider)
    
    for name, (nominal, tolerance, sign) in components.items():
        directed_nominal = nominal * sign
        total_nominal += directed_nominal
        worst_case_tolerance += abs(tolerance)
        rss_tolerance_squared += tolerance ** 2
        direction = "+" if sign == 1 else "-"
        print(f"| {name:<32} | {nominal:<13.3f} | ±{tolerance:<8.3f} | {direction:<9} |")
        
    print(divider)
    
    rss_tolerance = math.sqrt(rss_tolerance_squared)
    wc_min, wc_max = total_nominal - worst_case_tolerance, total_nominal + worst_case_tolerance
    rss_min, rss_max = total_nominal - rss_tolerance, total_nominal + rss_tolerance
    
    print(f"\n[Calculated Nominal Assembly Gap]: {total_nominal:.3f} mm")
    print(f"🔴 WORST-CASE ANALYSIS: ±{worst_case_tolerance:.3f} mm -> [{wc_min:.3f} mm to {wc_max:.3f} mm]")
    print(f" 🟢 STATISTICAL ANALYSIS (RSS): ±{rss_tolerance:.3f} mm -> [{rss_min:.3f} mm to {rss_max:.3f} mm]")
    print("=================================================================================\n")

if __name__ == "__main__":
    transaxle_axial_loop = {
        "Housing Casing Internal Width": (150.000, 0.080, 1),
        "Input Shaft Shoulder Length":   (85.000, 0.050, -1),
        "Left Roller Bearing Width":     (22.000, 0.030, -1),
        "Right Roller Bearing Width":    (22.000, 0.030, -1),
        "Selected Selective Shim Spacer":(20.500, 0.015, -1)
    }
    analyze_tolerance_stackup(transaxle_axial_loop)
