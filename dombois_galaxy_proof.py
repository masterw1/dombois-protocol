import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

# --- CONFIG ---
NUM_PARTICLES = 4000
G_CONST = 0.5  # Newtonsche Gravitationskraft
BG_COLOR = '#080808'
PARTICLE_COLOR = '#00ccff'

class GalacticGenesis:
    def __init__(self):
        # 1. Initiale Gaswolke (Zufällig verteilt)
        self.r = np.random.uniform(0.5, 5.0, NUM_PARTICLES) # Radius
        self.theta = np.random.uniform(0, 2*np.pi, NUM_PARTICLES) # Winkel
        
        # Umrechnung in Kartesisch
        self.x = self.r * np.cos(self.theta)
        self.y = self.r * np.sin(self.theta)
        
        # Geschwindigkeiten (Drehimpuls, damit es nicht sofort kollabiert)
        self.vx = -self.y * 0.5
        self.vy = self.x * 0.5
        
        # --- DOMBOIS VARIABLEN ---
        self.acoustic_strength = 0.0 # Start bei 0 (Nur Newton)
        self.frequency = 4.0         # Die "Tonhöhe" des Schwarzen Lochs

        # Setup Plot
        self.fig, self.ax = plt.subplots(figsize=(10, 8), facecolor=BG_COLOR)
        self.fig.canvas.manager.set_window_title("DOMBOIS PROTOCOL: GALACTIC RESONANCE PROOF")
        plt.subplots_adjust(bottom=0.25) # Platz unten für Slider
        
        self.scat = self.ax.scatter(self.x, self.y, s=2, c=PARTICLE_COLOR, alpha=0.6, edgecolors='none')
        
        # Schwarzes Loch (Zentrum)
        self.hole_visual = plt.Circle((0,0), 0.2, color='black', ec='white', lw=2, zorder=10)
        self.ax.add_patch(self.hole_visual)
        
        self.ax.set_xlim(-6, 6)
        self.ax.set_ylim(-6, 6)
        self.ax.axis('off')
        
        # UI
        self.setup_ui()
        
    def setup_ui(self):
        # Slider für Dombois-Feld
        ax_res = plt.axes([0.2, 0.1, 0.6, 0.03], facecolor='#222')
        self.sl_res = Slider(ax_res, 'Acoustic Field', 0.0, 1.0, valinit=0.0, color='#00ffcc')
        self.sl_res.label.set_color('white') # FIX: Weiße Schrift
        
        ax_freq = plt.axes([0.2, 0.05, 0.6, 0.03], facecolor='#222')
        self.sl_freq = Slider(ax_freq, 'Hole Frequency', 1.0, 8.0, valinit=4.0, color='#ff0055')
        self.sl_freq.label.set_color('white') # FIX: Weiße Schrift
        
        self.sl_res.on_changed(self.update_params)
        self.sl_freq.on_changed(self.update_params)
        
        # Info Text
        self.info_text = self.ax.text(0.05, 0.95, "MODE: NEWTONIAN GRAVITY (Standard)", 
                                      transform=self.ax.transAxes, color='white', fontsize=12)

    def update_params(self, val):
        self.acoustic_strength = self.sl_res.val
        self.frequency = self.sl_freq.val
        
        if self.acoustic_strength > 0.1:
            self.info_text.set_text("MODE: DOMBOIS RESONANCE (Structure Forming)")
            self.info_text.set_color('#00ffcc')
        else:
            self.info_text.set_text("MODE: NEWTONIAN GRAVITY (Chaos)")
            self.info_text.set_color('gray')

    def dombois_field_equation(self, r, theta):
        """
        DAS HERZSTÜCK: Die akustische Wellengleichung einer Galaxie.
        L = 1/2f * sqrt(E/rho)
        Hier simuliert: Eine rotierende Spiralwelle.
        """
        # Distanz-abhängige Phase (weil c mit Radius zunimmt, da Dichte abnimmt)
        # In der Natur nimmt die Dichte nach außen ab -> c steigt -> Wellenlänge wird länger.
        phase = self.frequency * np.log(r + 1) 
        
        # Spiral-Gleichung: Interferenz zwischen Radial-Welle und Rotation
        # Wir erzeugen "Täler" im Raum-Potential
        wave_potential = np.sin(phase - 2*theta) # 2 Arme (typisch Balkenspirale)
        
        return wave_potential

    def update(self, frame):
        # 1. Radius und Winkel berechnen
        r = np.sqrt(self.x**2 + self.y**2) + 0.01
        theta = np.arctan2(self.y, self.x)
        
        # 2. NEWTON FORCE (Zum Zentrum ziehen)
        # F = G * M / r^2
        force = G_CONST / (r**2)
        acc_x = -force * (self.x / r)
        acc_y = -force * (self.y / r)
        
        # 3. DOMBOIS ACOUSTIC FORCE (Das "Beweis-Feld")
        # Teilchen werden in die Knotenpunkte der stehenden Welle gedrückt (Chladni)
        if self.acoustic_strength > 0:
            # Gradient des akustischen Potentials
            wave = self.dombois_field_equation(r, theta)
            
            # Die "Kraft" drückt Materie in die Täler der Welle
            # Wir leiten nach Winkel ab, um Tangentialkräfte zu simulieren
            acoustic_force = -1.0 * wave * self.acoustic_strength
            
            # Diese Kraft wirkt senkrecht zum Radius (formt die Arme)
            acc_x += -acoustic_force * np.sin(theta) 
            acc_y += acoustic_force * np.cos(theta)
            
            # Radiale Stabilisierung (Hält die Arme auf Abstand)
            acc_x += (wave * self.x/r) * 0.1 * self.acoustic_strength
            acc_y += (wave * self.y/r) * 0.1 * self.acoustic_strength

        # 4. Integration (Bewegung)
        self.vx += acc_x * 0.1
        self.vy += acc_y * 0.1
        
        # Dämpfung (Reibung im Gas), damit sich Strukturen stabilisieren
        self.vx *= 0.96
        self.vy *= 0.96
        
        self.x += self.vx
        self.y += self.vy
        
        # Update Plot
        data = np.stack([self.x, self.y]).T
        self.scat.set_offsets(data)
        
        # Farbe basierend auf Dichte/Resonanz
        # Teilchen in Resonanz leuchten heller
        if self.acoustic_strength > 0:
            wave_val = self.dombois_field_equation(r, theta)
            # Normalisieren für Colormap (0..1)
            colors = (wave_val + 1) / 2
            self.scat.set_array(colors)
            self.scat.set_cmap('winter') # Dombois Blau/Grün
        else:
            self.scat.set_array(None)
            self.scat.set_color(PARTICLE_COLOR)

        return self.scat,

    def start(self):
        anim = FuncAnimation(self.fig, self.update, frames=200, interval=20, blit=False)
        plt.show()

if __name__ == "__main__":
    sim = GalacticGenesis()
    sim.start()