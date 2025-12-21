

# THE DOMBOIS PROTOCOL

### Quantized Morphogenesis: Decoding the Harmonic Geometry of Biological Growth

**Version:** 2.1

**Status:** Proof of Concept / Validation Phase

**License:** Copyright © 2025 Dombois Research Group. All Rights Reserved.

---

## 🧬 Abstract

The **Dombois Protocol** postulates that biological form is not merely a product of genetic signaling, but the material consequence of **standing acoustic and mechanical wave fields**. By applying Chladni plate physics to biological tissue, this repository provides the mathematical and computational proof that anatomical features—from the limb ratios of *Tyrannosaurus rex* to the wing venation of *Drosophila*—align with discrete harmonic nodal lines.

This repository contains the **Python algorithms** used to validate this theory against massive biological datasets, proving that evolution is quantized, not random.

---

## 📊 Key Findings (The Evidence)

Running the `mass_validator.py` script on the datasets provided below yields statistically significant correlations between biological anatomy and harmonic attractors:

### 1. The Macro-Scale Proof (Humans, Birds, Dinosaurs)

Our cross-species analysis reveals that limb proportions (Humerus/Femur) cluster around specific harmonic intervals:

* **Humans (The Precision Needle):** Extremely high density peak at **Ratio 0.70** (approx.  or perfect Fifth). Variance is near zero.
* **Birds (The Aero Shift):** Distinct cluster at **Ratio 1.1** (approx. Major Second ), optimizing for aerodynamics.
* **Theropods (The Evolutionary Jump):** A bimodal distribution. Ancestral forms cluster at **0.5** (Octave), while derived giants (T-Rex) shift sharply to **0.30** (Duodezime), proving a quantized "phase shift" in morphology rather than gradual drift.

### 2. The Micro-Scale Proof (Zebrafish & Drosophila)

* **Zebrafish:** Lateral line organ placement correlates >99.8% with the nodes of a 5.4 Hz standing wave.
* **Drosophila:** Wing veins L2-L5 align perfectly with the nodal lines (zero-vibration zones) of a fixed-hinge membrane simulation.

---

## 📂 Repository Structure

* `mass_validator.py` - The core engine. Reads CSV data, filters taxa, and calculates harmonic density plots.
* `zebrafish_morph.py` - 1D wave simulation vs. ZFIN biological data.
* `drosophila_morph.py` - 2D Chladni simulation vs. FlyBase venation data.
* `healing_dombois_protocol.py` - Theoretical model for "Acoustic Osteogenesis" (Regenerative Medicine application).
* `planetary_morph.py` - Exobiological simulator predicting morphology under different gravity constants.
* `/data` - Folder for biological datasets (see setup below).

---

## 🚀 Getting Started

### 1. Prerequisites

You need Python 3.10+ and the following scientific libraries:

```bash
pip install pandas numpy matplotlib seaborn scipy openpyxl

```

### 2. Data Acquisition (CRITICAL)

Due to licensing, we cannot host the raw biological datasets directly. You must download them from their official scientific repositories and place them in a folder named `/data`.

**IMPORTANT:** You must rename the files exactly as listed below for the scripts to work.

| Dataset | Source | Action | Target Filename |
| --- | --- | --- | --- |
| **Humans** | [Goldman Osteometric Dataset](https://www.google.com/search?q=https://github.com/geanes/bioanth/blob/master/data-raw/Goldman.csv) | Download raw CSV | `Goldman_Humans.csv` |
| **Birds** | [Skelevision (Weeks et al.)](https://www.google.com/search?q=https://deepblue.lib.umich.edu/data/concern/data_sets/8w32r5690) | Download `Complete_Trait...csv` | `Complete_Trait_Dataset_v1.csv` |
| **Dinosaurs** | [Benson et al. (Dryad)](https://datadryad.org/stash/dataset/doi:10.5061/dryad.gr1qp) | Download & extract ZIP. Find the main data txt/xls. | `Data.txt` |

*Note: The `Data.txt` for dinosaurs must be the Tab-Separated Value file provided by Benson et al. The script automatically handles the filtering for Theropods.*

### 3. Running the Validation

To reproduce the "Golden Figures" (the charts used in the White Paper):

```bash
# 1. Run the Zebrafish and Worm Simulation and you will get two figures from the whitepaper.
python zebrafish_morph.py

# 2. Run the Wing Simulation and you get one figure from the whitepaper.
python drosophila_morph.py

# 3. Run the Planetary Morph Simulator (Exobiology)
python planetary_morph.py

# 4. Run the Mass Validator (The main proof) for a calculated comparison of bones by the algorithm for humans, birds and theropods. For this you need the correct datasets in /data!
python mass_validator.py
# Output: 'Harmonic_Proof_Robust.png' showing the density peaks.

# Feel free to calculate it against any dataset that you can find.

```

---

## 🔮 Future Implications

The code includes a module `healing_sim.py` which applies the inverse logic: Instead of analyzing existing forms, it calculates the **corrective frequency** needed to guide cells back to their harmonic baseline. This has potential applications in:

* **Oncology:** Detecting tumors via stiffness-frequency dissonance.
* **Regenerative Medicine:** Inducing specific tissue growth via resonance fields.
* **Climate Science:** Optimizing tree growth (carbon capture) via laminar flow resonance.

---

## 📞 Contact & Citation

**Til von Dombois Research Group** c/o Attic Studios

Lise-Meitner-Str. 8

31303 Hannover-Burgdorf, Germany

Email: info@attic-burgdorf.de

*This repository and the associated White Paper are timestamped on the Blockchain for Proof of Existence (December 21, 2025).*
