# 🌊 Global Shark Attack Warner

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A fun, interactive Flask app that predicts shark-attack risk based on user inputs: activity, shark species, time of day, attack type, and location.

---
## 📖 Table of Contents

- [✨ Features](#-features)  
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
  – Classifies “High” or “Low” shark-attack risk using your selections.  
- 🎛️ **Interactive UI**  
  – Simple dropdowns for Attack Type, Activity, Country, Time of Day, and Shark Species.  
- 🎨 **Animated Background**  
  – Beach scene with moving shark sprites for immersive UX.  
- 🚀 **Lightweight & Fast**  
  – Minimal dependencies, instant Flask startup.  

---
<a id="-setup--installation"></a>
## ⚙️ Setup & Installation

1. **Clone the repo**  
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
   pip install flask joblib numpy pandas scikit-learn
   ```

---
<a id="-preparing-assets"></a>
## 🖼️ Preparing Assets

1. **Background Image**  
   - Place a beach scene as `static/background.jpg`.  
2. **Shark Sprites**  
   - Open `static/create_shark_images.html` in your browser.  
   - Right-click each shark and **Save As** `shark1.png`, `shark2.png` into `static/`.  

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
   - View result: **High Risk** (“Yes”) or **Low Risk** (“No”)

---
## 🐞 Troubleshooting

- ❌ _Model load error?_  
  • Check that `model/Global_Shark_Attack.joblib` exists or update `model_path` in `app.py`.  
- ❌ _Missing images?_  
  • Verify `background.jpg`, `shark1.png`, and `shark2.png` are in `static/`.  
- ❌ _Flask crashes?_  
  • Review terminal logs and confirm all Python packages are installed.  

---
## 🎨 Customization

- **Color Scheme**: Edit CSS variables in `static/style.css`.  
- **Animations**: Tweak `@keyframes` in your styles to change shark speed or direction.  
- **Model Features**:  
  – Expand the form in `templates/index.html` and adjust `app.py` to read new inputs.  

---
## 🌐 Deployment

This project is deployed as Docker Image on DockerHub:

> https://hub.docker.com/r/kratuzen/global-shark-attack-project

---
## 📜 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for full details.  
