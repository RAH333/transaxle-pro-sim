import math

def calculate_lewis_bending_stress(torque_nm, pitch_diameter_mm, face_width_mm, module, lewis_form_factor=0.35):
    """
    Computes tangential force and bending stress on a Spur Transaxle Gear 
    using fundamental Lewis equation principles.
    """
    # Convert torque to Tangential Force (Wt) in Newtons
    radius_m = (pitch_diameter_mm / 2.0) / 1000.0
    wt_n = torque_nm / radius_m
    
    # Lewis Equation: Stress = Wt / (b * m * Y)
    stress_mpa = wt_n / (face_width_mm * module * lewis_form_factor)
    
    return {
        "Tangential Force (N)": round(wt_n, 2),
        "Lewis Bending Stress (MPa)": round(stress_mpa, 2)
    }

if __name__ == "__main__":
    print("--- Transaxle Spur/Helical Gear Mesh Check ---")
    # Simulation data matching typical tractor/automotive low-gear torque outputs
    results = calculate_lewis_bending_stress(
        torque_nm=350.0, 
        pitch_diameter_mm=120.0, 
        face_width_mm=35.0, 
        module=4.0
    )
    for key, value in results.items():
        print(f"{key}: {value}")
      
