def calculate_l10_life(dynamic_load_rating_kn, equivalent_radial_load_kn, rpm, bearing_type="roller"):
    """
    Computes basic L10 fatigue life in hours for transaxle bearings 
    supporting shafts under consistent operation.
    """
    # Lifespan power coefficient: 3.0 for ball bearings, 10/3 (3.33) for roller bearings
    p = 3.33 if bearing_type == "roller" else 3.0
    
    # Life in millions of revolutions (L10)
    l10_revolutions = (dynamic_load_rating_kn / equivalent_radial_load_kn) ** p
    
    # Life in hours
    l10_hours = (l10_revolutions * 1e6) / (60.0 * rpm)
    
    return {
        "L10 Bearing Life (Millions of Revs)": round(l10_revolutions, 2),
        "Expected Service Life (Hours)": round(l10_hours, 2)
    }

if __name__ == "__main__":
    print("\n--- Tapered Roller Bearing Life Assessment ---")
    bearing_metrics = calculate_l10_life(
        dynamic_load_rating_kn=85.0, 
        equivalent_radial_load_kn=24.5, 
        rpm=1800
    )
    for key, value in bearing_metrics.items():
        print(f"{key}: {value}")
      
