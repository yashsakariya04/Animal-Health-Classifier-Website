# 🐾 AniHealth AI - Animal Health Detection System

## Overview

AniHealth AI is an intelligent web-based application that leverages machine learning to assess and classify animal health conditions based on vital signs and symptoms. Built as part of the Experiential Learning - AIML Internship Program, this project demonstrates the practical application of AI/ML in veterinary healthcare.

## 🌟 Key Features

### 🤖 AI-Powered Health Assessment
- **Multi-Species Support**: Comprehensive coverage for 17+ animal types including domestic pets (Dogs, Cats), livestock (Cows, Goats, Sheep, Pigs), poultry (Chickens, Ducks, Turkeys), and exotic animals (Lions, Elephants, Parrots)
- **Symptom-Based Analysis**: Advanced symptom rating system (0-10 scale) across multiple health categories:
  - 🧠 Blood-Brain Symptoms
  - 👁️ Appearance Symptoms  
  - 🦠 General Disease Symptoms
  - 🫁 Lung Symptoms
  - 🩸 Abdominal Symptoms

### 🎯 Intelligent Classification
- **Three-Tier Health Status**: Precise classification into:
  - 🟢 **Stable**: Healthy animals with minimal health concerns
  - 🟡 **Critical**: Animals requiring immediate veterinary attention
  - 🟢 **Recovered**: Animals in recovery phase with improving conditions

### 💻 Modern Web Interface
- **Responsive Design**: Beautiful, mobile-friendly interface with glass morphism effects
- **Dynamic UI**: Sky blue gradient theme with smooth animations and hover effects
- **User-Friendly Input**: Dropdown-based symptom rating system for easy data entry
- **Real-time Results**: Instant health assessment with detailed status reports

## 🛠️ Technical Stack

### Backend
- **Python 3.x**: Core programming language
- **Flask**: Lightweight web framework for API endpoints
- **Scikit-learn**: Machine learning model training and inference
- **NumPy**: Numerical computations and array operations
- **Pickle**: Model serialization and loading

### Frontend
- **HTML5**: Semantic markup structure
- **CSS3**: Advanced styling with gradients, animations, and responsive design
- **JavaScript**: Interactive elements and dynamic content
- **Bootstrap-inspired**: Custom CSS framework for consistent design

### Machine Learning
- **Random Forest Classifier**: Primary ML algorithm for health classification
- **Feature Engineering**: Comprehensive input encoding for categorical and numerical data
- **Model Persistence**: Trained model saved as `rfc.pkl` for production deployment

## 📊 Data Processing

### Input Encoding
```python
# Animal Name Mapping
ANIMAL_MAP = {
    "Cow": 0, "Dog": 1, "Goat": 2, "Cat": 3, "Horse": 4,
    "Pig": 5, "Sheep": 6, "Chicken": 7, "Duck": 8, "Turkey": 9,
    "Lion": 10, "Parrot": 11, "Rabbit": 12, "Buffaloes": 13,
    "Elephant": 14, "Cattle": 15, "Mammal": 16
}

# Symptom Rating: 0-10 scale for each health category
# 0 = No symptoms, 10 = Severe symptoms
```

### Model Architecture
- **Input Features**: 6-dimensional feature vector
  - Animal Type (encoded categorical)
  - 5 Symptom Categories (0-10 numerical ratings)
- **Output**: Health status classification (0, 1, 2)
- **Training Data**: Comprehensive dataset with diverse animal health scenarios

## 🚀 Installation & Setup

### Prerequisites
```bash
# Python 3.7+ required
python --version

# Install required packages
pip install flask numpy scikit-learn
```

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/anihealth-ai.git
cd anihealth-ai

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Access the application
# Open http://localhost:5000 in your browser
```

### Project Structure
```
anihealth-ai/
├── app.py                 # Main Flask application
├── rfc.pkl               # Trained machine learning model
├── animal_health_data_detailed.csv  # Training dataset
├── test_model.py         # Model testing script
├── requirements.txt       # Python dependencies
├── Templates/
│   ├── index.html        # Main input form
│   └── output.html       # Results display page
└── README.md            # Project documentation
```

## 🎨 User Interface Features

### Design Highlights
- **Glass Morphism**: Modern translucent design elements
- **Gradient Backgrounds**: Dynamic sky blue color scheme
- **Smooth Animations**: Hover effects and transitions
- **Responsive Layout**: Optimized for all device sizes
- **Custom Dropdowns**: Enhanced select elements with custom styling

### Navigation & Branding
- **Company Integration**: Credits to internship partners (NASSCOM, SMARTBRIDGE, FUTURESKILLS PRIME)
- **Professional Branding**: Consistent logo and color scheme
- **Intuitive Navigation**: Clear menu structure and user flow

## 🔬 Model Performance

### Training Data
- **Dataset**: Comprehensive animal health records
- **Features**: Multi-dimensional symptom analysis
- **Validation**: Cross-validated model performance
- **Accuracy**: High classification accuracy across animal types

### Prediction Logic
```python
# Model predicts numerical values (0, 1, 2)
# Mapping to health status:
pred_map = {
    0: "Stable - The animal appears to be in good health condition.",
    1: "Critical - Immediate veterinary attention is required.",
    2: "Recovered - The animal is showing signs of recovery."
}
```

## 🌐 Deployment

### Local Development
```bash
# Development server
python app.py
# Server runs on http://localhost:5000
```

### Production Deployment
- **Cloud Platforms**: Compatible with Render, Heroku, AWS
- **Containerization**: Docker support for easy deployment
- **Environment Variables**: Configurable settings for production

## 🤝 Contributing

### Development Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards
- **Python**: PEP 8 compliance
- **HTML/CSS**: Semantic markup and responsive design
- **Documentation**: Comprehensive inline comments

## 📈 Future Enhancements

### Planned Features
- **Image Upload**: Photo-based symptom analysis
- **Historical Data**: Health trend tracking over time
- **Multi-language Support**: International veterinary terminology
- **Mobile App**: Native iOS/Android applications
- **API Integration**: Third-party veterinary database connections

### Technical Improvements
- **Deep Learning**: CNN-based image analysis
- **Real-time Monitoring**: IoT sensor integration
- **Predictive Analytics**: Early disease detection algorithms
- **Cloud AI**: Integration with cloud-based ML services

## 🏆 Project Credits

### Development Team
- **Yash and Madhavi** - Lead Developers

### Internship Partners
- **NASSCOM** - Industry guidance and support
- **SMARTBRIDGE** - Technical mentorship
- **FUTURESKILLS PRIME** - Educational framework

### Special Thanks
- Veterinary experts for domain knowledge
- Open-source community for tools and libraries
- Educational institutions for academic support

## 📄 License

This project is developed as part of the Experiential Learning - AIML Internship Program. All rights reserved.

## 📞 Support

For technical support or questions about the project:
- **Issues**: Use GitHub Issues for bug reports
- **Documentation**: Check the inline code comments
- **Contact**: Reach out to the development team

---

**Built with ❤️ for animal healthcare and AI education**

*This project demonstrates the practical application of machine learning in veterinary medicine, showcasing how AI can assist in early disease detection and health monitoring for various animal species.* 