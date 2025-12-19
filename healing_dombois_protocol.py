import numpy as np
import pandas as pd

# Akustische Konstante (Schallgeschwindigkeit im Knochen)
SPEED_OF_SOUND_BONE = 3500 * 1000 # mm/s (ca 3500 m/s in kortikalem Knochen)

def calculate_healing_frequency(patient_femur_mm, patient_humerus_mm):
    # 1. Analyse des Ist-Zustands
    current_ratio = patient_humerus_mm / patient_femur_mm
    
    # 2. Das "Dombois-Ideal" (Der gesunde Attraktor)
    # Wir wissen aus den Daten: Mensch sollte bei ~0.707 liegen
    ideal_ratio = 0.7071 
    
    # 3. Abweichung (Dissonanz)
    deviation = abs(current_ratio - ideal_ratio)
    
    # 4. Berechnung der Korrektur
    # Welche Länge sollte der Humerus eigentlich haben?
    target_humerus = patient_femur_mm * ideal_ratio
    diff_mm = target_humerus - patient_humerus_mm
    
    # 5. Die Heilungs-Frequenz
    # Frequenz, die nötig ist, um die stehende Welle für die ZIEL-Länge zu erzeugen
    # f = c / (2 * L)  (Lambda halbe für Grundresonanz)
    healing_freq_hz = SPEED_OF_SOUND_BONE / (2 * target_humerus)
    
    return {
        'Current Ratio': round(current_ratio, 4),
        'Status': 'Resonant (Healthy)' if deviation < 0.02 else 'Dissonant (Pathological)',
        'Deviation': f"{deviation*100:.1f}%",
        'Target Humerus Length': f"{target_humerus:.1f} mm",
        'Correction Needed': f"{diff_mm:.1f} mm",
        'THERAPEUTIC FREQUENCY': f"{healing_freq_hz:.1f} Hz"
    }

# --- SIMULATION EINES PATIENTEN ---
# Fall: Ein Kind mit Wachstumsstörung im Arm (zu kurz)
patient_data = calculate_healing_frequency(patient_femur_mm=400.0, patient_humerus_mm=250.0)

print("--- DOMBOIS DIAGNOSTIC PROTOCOL ---")
for k, v in patient_data.items():
    print(f"{k}: {v}")
