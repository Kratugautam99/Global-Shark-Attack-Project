PROJECT NO.1
# Global Shark Attack Warner

This web application predicts the risk of shark attacks based on user input such as activity, shark species, time of day, attack type, and country.

## Setup Instructions

1. **Install Required Libraries**:
   ```bash
   pip install flask joblib numpy pandas scikit-learn
   ```

2. **Prepare Background Image**:
   - Save a beach image as `background.jpg` in the `static` folder.
   - The image should have a beach scene preferably with an ocean view.

3. **Create Shark Images**:
   - Open `static/create_shark_images.html` in a web browser.
   - Right-click on each shark image and select "Save Image As...".
   - Save them as `shark1.png` and `shark2.png` in the `static` folder.

4. **Set Up the Model**:
   - Ensure your trained model is saved as `Global_Shark_Attack.joblib` in a folder named `model` at the same level as the `Web_Deployment_Files` folder.
   - Alternatively, update the `model_path` in `app.py` to point to your model file.

## Running the Application

1. Navigate to the Web_Deployment_Files directory:
   ```bash
   cd Web_Deployment_Files
   ```

2. Start the Flask application:
   ```bash
   python app.py
   ```

3. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Using the Application

1. Select values from each dropdown:
   - Attack Type (Provoked/Unprovoked)
   - Activity (Boating/Boarding, Swimming/Wading, etc.)
   - Country
   - Time of Day
   - Shark Species

2. Click the "Predict Risk" button to see if there's a risk of a shark attack based on your selections.

3. The result will be displayed as "Yes" (high risk) or "No" (low risk).

## Troubleshooting

- If you encounter an error loading the model, ensure the path is correct in `app.py`.
- If the animations or styling doesn't appear correctly, check that all static files are in the correct location.
- For any Flask errors, check the terminal for error messages.

## Customization

- To change the color scheme, edit the CSS variables in `static/style.css`.
- To modify the shark animations, adjust the animation parameters in the CSS.
- To add more features to the prediction model, update both the HTML form and the Flask application accordingly. 
