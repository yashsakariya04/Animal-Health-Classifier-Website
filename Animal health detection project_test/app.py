from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# --- Model loading ---
try:
    model = pickle.load(open("rfc.pkl", "rb"))
except Exception as e:
    model = None
    print(f"Model loading failed: {e}")

# --- Helper: Encoding mappings ---
ANIMAL_MAP = {
    "Cow": 0,
    "Dog": 1,
    "Goat": 2,
    "Cat": 3,
    "Horse": 4,
    "Pig": 5,
    "Sheep": 6,
    "Chicken": 7,
    "Duck": 8,
    "Turkey": 9,
    "Lion": 10,
    "Parrot": 11,
    "Rabbit": 12,
    "Buffaloes": 13,
    "Elephant": 14,
    "Cattle": 15,
    "Mammal": 16
}

# --- Home page: Show input form ---
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction=None)

# --- Prediction route: Handle form submission ---
@app.route("/predict", methods=["POST"])
def predict():
    if not model:
        return render_template("index.html", prediction="⚠️ Model not loaded.")
    try:
        # Get form data
        animal_name = request.form.get("animal_name")
        blood_brain = int(request.form.get("blood_brain_disease"))
        appearance = int(request.form.get("appearance_disease"))
        general = int(request.form.get("general_disease"))
        lung = int(request.form.get("lung_disease"))
        abdomen = int(request.form.get("abdominal_disease"))

        # Validate numeric inputs (0-10 range)
        symptoms = [blood_brain, appearance, general, lung, abdomen]
        for i, symptom in enumerate(symptoms):
            if not (0 <= symptom <= 10):
                raise ValueError(f"Symptom rating must be between 0-10. Got: {symptom}")

        # Encode animal name
        animal_encoded = ANIMAL_MAP.get(animal_name, -1)
        if animal_encoded == -1:
            raise ValueError("Invalid animal name selected.")

        # Create feature array: [animal_encoded, blood_brain, appearance, general, lung, abdomen]
        features = [animal_encoded] + symptoms

        # Predict
        pred = model.predict([features])[0]
        
        # Debug: Print the actual prediction value
        print(f"Model prediction: {pred} (type: {type(pred)})")
        
        # Try different prediction mappings based on the actual model output
        # The issue might be that the mapping is reversed or different
        pred_map = {
            0: f"✅ {animal_name} is in STABLE condition. The animal shows normal health indicators and requires routine monitoring.",
            1: f"⚠️ {animal_name} is in CRITICAL condition! Immediate veterinary attention is required. The animal shows severe symptoms that need urgent medical intervention.",
            2: f"🔄 {animal_name} is in RECOVERY phase. The animal is showing signs of improvement and is responding well to treatment."
        }
        
        # Alternative mapping (in case the model outputs are different)
        alt_pred_map = {
            0: f"🔄 {animal_name} is in RECOVERY phase. The animal is showing signs of improvement and is responding well to treatment.",
            1: f"✅ {animal_name} is in STABLE condition. The animal shows normal health indicators and requires routine monitoring.",
            2: f"⚠️ {animal_name} is in CRITICAL condition! Immediate veterinary attention is required. The animal shows severe symptoms that need urgent medical intervention."
        }
        
        # If the prediction is not in our map, show the raw value for debugging
        if pred not in pred_map:
            result = f"🔍 DEBUG: {animal_name} - Raw prediction value: {pred} (Type: {type(pred)})"
        else:
            result = pred_map.get(pred, f"❓ Unknown health status for {animal_name}: {pred}")

        return render_template("index.html", prediction=result)
    except ValueError as e:
        return render_template("index.html", prediction=f"⚠️ Input Error: {str(e)}")
    except Exception as e:
        return render_template("index.html", prediction=f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)