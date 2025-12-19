import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# 1. SETUP & HARMONISCHE KONSTANTEN
# ==========================================
HARMONIC_ATTRACTORS = {
    '1:4 (Double Octave)': 0.25,
    '1:3 (Twelfth)': 0.333,
    '1:2 (Octave)': 0.5,
    'Golden (0.618)': 0.618,
    '3:4 (Fourth)': 0.75,
    '1:1 (Unison)': 1.0,
    '4:3 (Fourth Up)': 1.333
}

# ==========================================
# 2. ROBUSTE DATEN-VORBEREITUNG
# ==========================================
def prepare_theropod_data():
    source_file = 'Data.txt'
    target_file = 'Theropods_Only.csv'
    
    if not os.path.exists(source_file):
        print(f"❌ FEHLER: {source_file} nicht gefunden.")
        return

    print(f"--- Starte Daten-Filterung aus {source_file} ---")
    try:
        # Robusteres Einlesen mit Python-Engine
        df = pd.read_csv(source_file, sep='\t', encoding='latin1', on_bad_lines='skip', engine='python')
        
        # Spalten in Zahlen umwandeln
        df['Femur'] = pd.to_numeric(df['FL'], errors='coerce')
        df['Humerus'] = pd.to_numeric(df['HL'], errors='coerce')
        
        # ---------------------------------------------------------
        # FILTER-STRATEGIE (Hier passiert die Magie!)
        # ---------------------------------------------------------
        
        # 1. Versuch: Nur Tyrannosauroiden (Der "scharfe Peak")
# KORRIGIERTER FILTER: Sucht jetzt auch in 'Subclade'
        mask_tyranno = df['Taxon'].astype(str).str.contains('Tyranno', case=False) | \
                       df['Clade'].astype(str).str.contains('Tyranno', case=False) | \
                       df['Subclade'].astype(str).str.contains('Tyranno', case=False)
        
        tyrannos = df[mask_tyranno].dropna(subset=['Femur', 'Humerus'])
        
        # CHECK: Haben wir genug Daten für eine Kurve? (Mindestens 2)
        if len(tyrannos) > 1:
            print(f"✅ TREFFER: {len(tyrannos)} Tyrannosauroiden gefunden! Nutze den scharfen Filter.")
            final_df = tyrannos
        else:
            print(f"⚠️ WARNUNG: Nur {len(tyrannos)} Tyrannosauroid gefunden (zu wenig für Density Plot).")
            print("👉 Schalte um auf 'Alle Theropoden' (breiter Filter)...")
            
            # 2. Versuch: Alle Theropoden (Der "0.45 Peak")
            mask_thero = df['Clade'] == 'Theropoda'
            theros = df[mask_thero].dropna(subset=['Femur', 'Humerus'])
            final_df = theros
            print(f"✅ FALLBACK: {len(final_df)} Theropoden geladen.")

        # Speichern
        final_df.to_csv(target_file, index=False)
        print(f"Daten gespeichert in: {target_file}\n")
        
    except Exception as e:
        print(f"❌ Kritischer Fehler bei der Datenaufbereitung: {e}")

# ==========================================
# 3. DER VALIDATOR (PLOT)
# ==========================================
class UniversalValidator:
    def __init__(self):
        self.data = pd.DataFrame()

    def load_dinos(self, path):
        try:
            df = pd.read_csv(path) # Liest die vorbereitete CSV
            clean = pd.DataFrame({
                'Group': 'Dinosaur (Theropods)',
                'Femur': df['Femur'],
                'Humerus': df['Humerus']
            })
            self._add(clean)
        except: pass

    def load_birds(self, path):
        try:
            df = pd.read_csv(path, encoding='latin1', on_bad_lines='skip')
            clean = pd.DataFrame({
                'Group': 'Bird',
                'Femur': pd.to_numeric(df['femur'], errors='coerce'),
                'Humerus': pd.to_numeric(df['humerus'], errors='coerce')
            })
            self._add(clean)
        except: pass

    def load_humans(self, path):
        try:
            df = pd.read_csv(path, encoding='latin1', on_bad_lines='skip')
            clean = pd.DataFrame({
                'Group': 'Human',
                'Femur': pd.to_numeric(df['LFML'], errors='coerce'),
                'Humerus': pd.to_numeric(df['LHML'], errors='coerce')
            })
            self._add(clean)
        except: pass

    def _add(self, df):
        df = df.dropna().loc[(df['Femur'] > 0) & (df['Humerus'] > 0)]
        self.data = pd.concat([self.data, df], ignore_index=True)

    def analyze(self):
        if self.data.empty:
            print("Keine Daten für Plot.")
            return

        df = self.data
        df['Ratio'] = df['Humerus'] / df['Femur']
        
        plt.figure(figsize=(14, 8))
        sns.set_style("darkgrid")
        
        # KDE Plot mit Fehler-Handling
        try:
            sns.kdeplot(data=df, x='Ratio', hue='Group', fill=True, 
                        common_norm=False, palette='bright', alpha=0.4, linewidth=2, warn_singular=False)
        except Exception as e:
            print(f"KDE Plot Fehler (zu wenig Daten?): {e}")
            # Fallback: Histogramm wenn KDE nicht geht
            sns.histplot(data=df, x='Ratio', hue='Group', element="step", stat="density", common_norm=False)
        
        # Linien
        for name, val in HARMONIC_ATTRACTORS.items():
            plt.axvline(val, color='red', linestyle='--', alpha=0.6)
            plt.text(val, 0.5, name, rotation=90, color='red', fontweight='bold', fontsize=9)

        plt.title("HARMONISCHE RESONANZ: Evolutionäre Attraktoren", fontsize=16)
        plt.xlabel("Ratio (Humerus / Femur)")
        plt.xlim(0.0, 1.6)
        
        print("Speichere Plot als 'Harmonic_Proof_Robust.png'...")
        plt.savefig("Harmonic_Proof_Robust.png")
        plt.show()

# --- RUN ---
prepare_theropod_data()

validator = UniversalValidator()
validator.load_dinos('Theropods_Only.csv')
validator.load_birds('Complete_Trait_Dataset_v1.csv')
validator.load_humans('Goldman_Humans.csv')
validator.analyze()
