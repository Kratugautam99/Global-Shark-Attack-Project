<p align="center">
  <img src="https://raw.githubusercontent.com/Kratugautam99/Global-Shark-Attack-Project/refs/heads/main/Web_Deployment_Files/static/shark-icon.png" alt="Shark Icon" width="150"/>
</p>

# 🌊 Global Shark Attack Warner

[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> An engaging, interactive Flask application that predicts shark‑attack risk based on user inputs such as **activity, shark species, time of day, attack type, and location**.  
> Designed to be lightweight, fast, and visually immersive, it blends machine learning with a playful UI to make risk prediction both informative and fun.

---

## 📖 Table of Contents

- [✨ Features](#-features)  
- [📸 Demo Screenshots](#-dem)  
- [⚙️ Setup & Installation](#-setup--installation)  
- [🖼️ Preparing Assets](#-preparing-assets)  
- [🚀 Running the App](#-running-the-app)  
- [🖥️ Usage Guide](#-usage-guide)  
- [🐞 Troubleshooting](#-troubleshooting)  
- [🎨 Customization](#-customization)  
- [🌐 Deployment](#-deployment)  
- [📜 License](#-license)  

---

## ✨ Features

- 🦈 **Risk Prediction**  
  Classifies scenarios into **High Risk** or **Low Risk** shark‑attack likelihood, based on your chosen parameters.  

- 🎛️ **Interactive UI**  
  Clean dropdown menus for **Attack Type, Activity, Country, Time of Day, and Shark Species**, making it beginner‑friendly and intuitive.  

- 🎨 **Animated Background**  
  A beach scene with moving shark sprites creates an immersive, game‑like experience while you interact with the model.  

- 🚀 **Lightweight & Fast**  
  Minimal dependencies ensure instant Flask startup and smooth performance across environments.  

---
<a id = "-dem"></a>
## 📸 Demo Screenshots

### 🌐 Site Overview
<p align="center">
  <img src="https://raw.githubusercontent.com/Kratugautam99/Global-Shark-Attack-Project/main/Demo/SiteView.png" alt="Site View" width="80%" />
</p>
The landing page of the application, where users can input details and explore shark attack data.

---

### ✅ Positive Prediction
<p align="center">
  <img src="https://raw.githubusercontent.com/Kratugautam99/Global-Shark-Attack-Project/main/Demo/PredictionYES.png" alt="Prediction YES" width="60%" />
</p>
When the model predicts a **likely shark attack scenario**, the interface clearly highlights the risk.

---

### ❌ Negative Prediction
<p align="center">
  <img src="https://raw.githubusercontent.com/Kratugautam99/Global-Shark-Attack-Project/main/Demo/PredictionNO.png" alt="Prediction NO" width="60%" />
</p>
A safe outcome prediction, showing that the given conditions are unlikely to result in an attack.

---

### ⚠️ Duplicate Input Detection
<p align="center">
  <img src="https://raw.githubusercontent.com/Kratugautam99/Global-Shark-Attack-Project/main/Demo/SameInputDetected.png" alt="Same Input Detected" width="60%" />
</p>
The system prevents redundant queries by detecting repeated inputs, ensuring efficient usage.

---

<a id="-setup--installation"></a>
## ⚙️ Setup & Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Kratugautam99/Global-Shark-Attack-Project.git
   cd Global-Shark-Attack-Project
   ```

2. **Create a virtual environment**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Alternative: Conda environment (Recommended)**  
   ```bash
   conda env create -f environment.yml
   conda activate shark-env
   ```

---

<a id="-preparing-assets"></a>
## 🖼️ Preparing Assets

1. **Background Image**  
   Add a beach scene image as `static/background.jpg`.  

2. **Shark Sprites**  
   - Open `static/create_shark_images.html` in your browser.  
   - Right‑click each shark and **Save As** `shark1.png`, `shark2.png` into the `static/` folder.  

---

## 🚀 Running the App

```bash
cd Web_Deployment_Files
python app.py
```

Then open your browser at:  
```
http://127.0.0.1:5000/
```

---

<a id="-usage-guide"></a>
## 🖥️ Usage Guide

1. **Select Options**  
   - **Attack Type**: Provoked / Unprovoked  
   - **Activity**: Boating, Swimming, Surfing, etc.  
   - **Country**: Location of the incident  
   - **Time of Day**: Dawn, Day, Dusk, Night  
   - **Shark Species**: e.g., Great White, Tiger, Bull  

2. **Predict**  
   - Click **Predict Risk**  
   - Instantly view the result: **High Risk** (“Yes”) or **Low Risk** (“No”).  

---

## 🐞 Troubleshooting

- ❌ **Model load error?**  
  Ensure `model/Global_Shark_Attack.joblib` exists or update `model_path` in `app.py`.  

- ❌ **Missing images?**  
  Confirm `background.jpg`, `shark1.png`, and `shark2.png` are present in `static/`.  

- ❌ **Flask crashes?**  
  Check terminal logs and verify all Python packages are installed correctly.  

---

## 🎨 Customization

- **Color Scheme**  
  Modify CSS variables in `static/style.css` to change the theme.  

- **Animations**  
  Adjust `@keyframes` in the stylesheet to tweak shark speed, direction, or effects.  

- **Model Features**  
  Expand the form in `templates/index.html` and update `app.py` to handle new inputs or features.  

---

## 🌐 Deployment

This project is containerized and available as a Docker image on DockerHub:  

👉 [Global Shark Attack Project on DockerHub](https://hub.docker.com/r/kratuzen/global-shark-attack-project)

---

## 📜 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for full details.  

---

Made with 🧠 by Kratu Gautam
