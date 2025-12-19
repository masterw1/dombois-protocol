import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. PHYSIK-ENGINE
# ---------------------------------------------------------
# Die Formel: f_neu = f_alt * sqrt(g_neu / g_alt)
# Die Länge: L_neu = c / f_neu
# Das bedeutet: L_neu = L_alt * sqrt(g_alt / g_neu)

def simulate_environment(name, gravity_g, base_femur_mm, base_humerus_mm, skull_height_mm):
    
    # Faktor der Dehnung (Wellenlängen-Verlängerung durch geringere Spannung)
    # Auf der Erde ist g_alt = 1.0
    morph_factor = np.sqrt(1.0 / gravity_g)
    
    # Neue Maße
    new_femur = base_femur_mm * morph_factor
    new_humerus = base_humerus_mm * morph_factor
    new_skull = skull_height_mm * morph_factor
    
    # Check: Rastet das neue Verhältnis in einen Attraktor ein?
    # Auf der Erde ist das Ratio 0.7 (Mensch). Bleibt das so?
    # Da BEIDE Knochen vom gleichen Faktor betroffen sind, bleibt das Ratio theoretisch gleich (Isometrie).
    # ABER: Die absolute Größe ändert sich massiv.
    
    return {
        'Planet': name,
        'Gravity (g)': gravity_g,
        'Morph Factor': morph_factor,
        'Femur (mm)': new_femur,
        'Humerus (mm)': new_humerus,
        'Skull Height (mm)': new_skull,
        'Total Height (est. m)': (new_femur * 4) / 1000 # Grobe Schätzung: Femur ist ca 1/4 der Höhe
    }

# 2. BASIS-DATEN (Der "Standard-Erdling")
# ---------------------------------------------------------
# Durchschnittswerte aus unserem Goldman-Datensatz
earth_human = {
    'femur': 430.0,   # mm
    'humerus': 305.0, # mm
    'skull': 220.0    # mm (Kopfhöhe)
}

# 3. SIMULATION LAUFEN LASSEN
# ---------------------------------------------------------
scenarios = [
    ('Earth', 1.0),
    ('Mars', 0.38),
    ('Moon', 0.16),
    ('Super-Earth (Kepler-22b)', 2.4)
]

results = []
for planet, g in scenarios:
    res = simulate_environment(planet, g, earth_human['femur'], earth_human['humerus'], earth_human['skull'])
    results.append(res)

df_morph = pd.DataFrame(results)

# 4. VISUALISIERUNG
# ---------------------------------------------------------
print("--- DER EXOBIOLOGIE-REPORT ---")
print(df_morph[['Planet', 'Gravity (g)', 'Morph Factor', 'Skull Height (mm)', 'Total Height (est. m)']])

# Plotting the "Heads"
plt.figure(figsize=(10, 6))
x = np.arange(len(df_morph))
heights = df_morph['Skull Height (mm)']

bars = plt.bar(x, heights, color=['green', 'red', 'gray', 'blue'])
plt.xticks(x, df_morph['Planet'])
plt.ylabel('Kopf-Höhe (mm)')
plt.title('DER MARS-KOPF: Morphogenetische Verzerrung durch Gravitation')
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Add text
for i, v in enumerate(heights):
    plt.text(i, v + 5, f"{v:.0f} mm", ha='center', fontweight='bold')

plt.show()
