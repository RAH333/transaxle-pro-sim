def generate_transaxle_dfmea():
    dfmea_data = [
        ["Crown Wheel Gear", "Tooth Root Fatigue Cracking", "Loss of drive to differential axle assembly", 8, "Improper induction hardening", 3, "Material chemical inspection logs", 4],
        ["Transaxle Input Shaft", "Torsional Shear Structural Snap", "Immediate loss of powertrain lines", 9, "Incorrect fillet radii profile", 2, "Finite Element Analysis check", 3],
        ["Tapered Axle Bearings", "Pitting on Roller Tracks", "Excessive noise, gear axial misalignment", 6, "Inadequate lubrication flow paths", 4, "Oil level sensor verification", 3]
    ]
    
    # Custom lightweight text formatter replacing tabulate module
    header = f"| {'Component':<22} | {'Failure Mode':<33} | {'Severity (S)':<12} | {'Occurrence (O)':<14} | {'Detection (D)':<13} | {'RPN':<5} |"
    divider = "-" * len(header)
    
    print(divider)
    print(header)
    print(divider)
    
    for row in dfmea_data:
        rpn = row[3] * row[5] * row[7]
        print(f"| {row[0]:<22} | {row[1]:<33} | {row[3]:<12} | {row[5]:<14} | {row[7]:<13} | {rpn:<5} |")
    print(divider)

if __name__ == "__main__":
    print("\n======================= AUTOMATED TRANSAXLE DFMEA REPORT ENGINE =======================")
    generate_transaxle_dfmea()
