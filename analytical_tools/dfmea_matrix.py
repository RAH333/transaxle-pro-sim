from tabulate import tabulate

def generate_transaxle_dfmea():
    """
    Generates and processes a text-based DFMEA (Design Failure Mode and Effects Analysis) 
    dashboard mapping critical system vulnerabilities for evaluation.
    """
    # Headers: Component, Failure Mode, Local Effect, Severity (S), Potential Cause, Occurrence (O), Current Controls, Detection (D), RPN
    dfmea_data = [
        ["Crown Wheel Gear", "Tooth Root Fatigue Fatigue Cracking", "Loss of drive transmission to differential axle assembly", 8, "Improper induction hardening layer profile", 3, "Material chemical inspection logs", 4],
        ["Transaxle Input Shaft", "Torsional Shear Structural Snap", "Immediate loss of powertrain connection lines", 9, "Incorrect fillet radii profile under high torque load", 2, "Finite Element Analysis layout check", 3],
        ["Tapered Axle Bearings", "Pitting / Flaking on Roller Tracks", "Excessive operational noise, gear axial misalignment", 6, "Inadequate lubrication flow paths in case", 4, "Oil level sensor testing verification", 3]
    ]
    
    processed_table = []
    for row in dfmea_data:
        severity = row[3]
        occurrence = row[5]
        detection = row[7]
        # Calculate Risk Priority Number: RPN = S * O * D
        rpn = severity * occurrence * detection
        
        # Build out final rows
        processed_row = [row[0], row[1], row[2], severity, row[4], occurrence, row[6], detection, rpn]
        processed_table.append(processed_row)
        
    headers = ["Component", "Failure Mode", "Effect", "S", "Potential Cause", "O", "Controls", "D", "RPN"]
    return tabulate(processed_table, headers=headers, tablefmt="grid")

if __name__ == "__main__":
    print("\n======================= AUTOMATED TRANSAXLE DFMEA REPORT ENGINE =======================")
    print(generate_transaxle_dfmea())
  
