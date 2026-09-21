import math

def compute_minimum_shaft_diameter(torque_nm, bending_moment_nm, allowable_shear_stress_mpa=55.0):
    """
    Calculates minimum required transaxle shaft diameter using ASME code 
    for transmission shafting configurations under combined loads.
    """
    # Convert MPa to N/m^2
    tau_allowable = allowable_shear_stress_mpa * 1e6
    
    # Equivalent Torsional Moment Formula: Meq = sqrt(M^2 + T^2)
    equivalent_moment = math.sqrt((bending_moment_nm ** 2) + (torque_nm ** 2))
    
    # Diameter formula: d = ((16 * Meq) / (pi * tau))^ (1/3)
    diameter_meters = ((16 * equivalent_moment) / (math.pi * tau_allowable)) ** (1/3)
    diameter_mm = diameter_meters * 1000.0
    
    return {
        "Equivalent Torsional Load (Nm)": round(equivalent_moment, 2),
        "Minimum Safe Shaft Diameter (mm)": round(diameter_mm, 2)
    }

if __name__ == "__main__":
    print("\n--- Transaxle Input/Counter Shaft Sizing Tool ---")
    shaft_metrics = compute_minimum_shaft_diameter(torque_nm=350.0, bending_moment_nm=180.0)
    for key, value in shaft_metrics.items():
        print(f"{key}: {value}")
      
