import pickle
import numpy as np

# Load the model
try:
    model = pickle.load(open("rfc.pkl", "rb"))
    print("✅ Model loaded successfully")
except Exception as e:
    print(f"❌ Model loading failed: {e}")
    exit(1)

# Test cases with different input combinations
test_cases = [
    # Test Case 1: All zeros (should be healthy/stable)
    {"name": "All Zeros (0,0,0,0,0)", "animal": "Cow", "symptoms": [0, 0, 0, 0, 0]},
    
    # Test Case 2: All ones (should be mild symptoms)
    {"name": "All Ones (1,1,1,1,1)", "animal": "Cow", "symptoms": [1, 1, 1, 1, 1]},
    
    # Test Case 3: All fives (moderate symptoms)
    {"name": "All Fives (5,5,5,5,5)", "animal": "Cow", "symptoms": [5, 5, 5, 5, 5]},
    
    # Test Case 4: All tens (severe symptoms)
    {"name": "All Tens (10,10,10,10,10)", "animal": "Cow", "symptoms": [10, 10, 10, 10, 10]},
    
    # Test Case 5: Mixed symptoms
    {"name": "Mixed (0,5,10,2,8)", "animal": "Cow", "symptoms": [0, 5, 10, 2, 8]},
    
    # Test Case 6: Different animal (Dog)
    {"name": "Dog - All Zeros", "animal": "Dog", "symptoms": [0, 0, 0, 0, 0]},
    
    # Test Case 7: Dog with severe symptoms
    {"name": "Dog - All Tens", "animal": "Dog", "symptoms": [10, 10, 10, 10, 10]},
]

# Animal mapping
ANIMAL_MAP = {
    "Cow": 0, "Dog": 1, "Goat": 2, "Cat": 3, "Horse": 4, "Pig": 5,
    "Sheep": 6, "Chicken": 7, "Duck": 8, "Turkey": 9, "Lion": 10,
    "Parrot": 11, "Rabbit": 12, "Buffaloes": 13, "Elephant": 14,
    "Cattle": 15, "Mammal": 16
}

print("\n🧪 Testing Model Predictions:")
print("=" * 60)

for i, test_case in enumerate(test_cases, 1):
    animal_name = test_case["animal"]
    symptoms = test_case["symptoms"]
    animal_encoded = ANIMAL_MAP[animal_name]
    
    # Create feature array: [animal_encoded, blood_brain, appearance, general, lung, abdomen]
    features = [animal_encoded] + symptoms
    
    # Make prediction
    pred = model.predict([features])[0]
    
    print(f"\n📋 Test Case {i}: {test_case['name']}")
    print(f"   Animal: {animal_name} (encoded: {animal_encoded})")
    print(f"   Symptoms: {symptoms}")
    print(f"   Features: {features}")
    print(f"   Prediction: {pred} (type: {type(pred)})")
    
    # Try different mappings
    mappings = {
        "Mapping 1 (0=Stable, 1=Critical, 2=Recovered)": {
            0: "STABLE", 1: "CRITICAL", 2: "RECOVERED"
        },
        "Mapping 2 (0=Recovered, 1=Stable, 2=Critical)": {
            0: "RECOVERED", 1: "STABLE", 2: "CRITICAL"
        },
        "Mapping 3 (0=Critical, 1=Stable, 2=Recovered)": {
            0: "CRITICAL", 1: "STABLE", 2: "RECOVERED"
        }
    }
    
    for mapping_name, mapping in mappings.items():
        status = mapping.get(pred, f"UNKNOWN({pred})")
        print(f"   {mapping_name}: {status}")

print("\n" + "=" * 60)
print("🎯 Analysis:")
print("- All zeros should typically result in STABLE/HEALTHY")
print("- All tens should typically result in CRITICAL")
print("- Mixed values should give varied results")
print("=" * 60) 