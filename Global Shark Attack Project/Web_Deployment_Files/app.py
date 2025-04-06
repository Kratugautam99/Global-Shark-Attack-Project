from flask import Flask, render_template, request, jsonify
import joblib
import os
import pandas as pd
import numpy as np
import hashlib
app = Flask(__name__)

# Path to the model file
model_path = 'C:/Users/user/Downloads/Global Shark Attack Project/Dataset_and_Model/Global_Shark_Attack.joblib'

# Simplified model loading
try:
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

# Deterministic fallback prediction function (simplified)
def deterministic_prediction(activity, species, time_phase, type_, country):
    # Create a hash of the input
    input_string = f"{activity}_{species}_{time_phase}_{type_}_{country}"
    hash_value = int(hashlib.md5(input_string.encode()).hexdigest(), 16)
    
    # Risk calculation (simplifying the logic)
    high_risk_activities = ['Swimming/Wading', 'Fishing/Hunting']
    high_risk_species = ['White Shark', 'Bull Shark', 'Tiger Shark']
    high_risk_countries = ['Australia', 'South Africa', 'United States Of America']
    
    # Base risk score calculation
    risk_score = 0
    risk_score += 30 if activity in high_risk_activities else 0
    risk_score += 30 if species in high_risk_species else 0
    risk_score += 20 if country in high_risk_countries else 0
    risk_score += 10 if time_phase in [2, 3] else 0  # Afternoon and Evening
    risk_score += 10 if type_ == 'Unprovoked' else 0
    risk_score += hash_value % 10  # Hash factor for consistency
    
    return [1] if risk_score >= 60 else [0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Extract form data
            activity = request.form.get('activity')
            species = request.form.get('species')
            time_phase = int(request.form.get('time_phase'))
            type_ = request.form.get('type')
            country = request.form.get('country')
            
            # Create input DataFrame
            input_df = pd.DataFrame({
                'Activity': [activity],
                'Species': [species],
                'Time_Phase': [time_phase],
                'Type': [type_],
                'Country': [country]
            })
            
            # Make prediction
            if model is None:
                # Use deterministic prediction if model isn't available
                prediction = deterministic_prediction(activity, species, time_phase, type_, country)
            else:
                # Try to use the model
                try:
                    prediction = model.predict(input_df)
                except Exception:
                    # Fallback to deterministic prediction
                    prediction = deterministic_prediction(activity, species, time_phase, type_, country)
            
            # Return prediction result
            return jsonify({'prediction': 'Yes' if prediction[0] == 1 else 'No'})
            
        except Exception as e:
            # Simple error handling
            print(f"Error during prediction: {str(e)}")
            return jsonify({'error': 'An error occurred during prediction'})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 
    