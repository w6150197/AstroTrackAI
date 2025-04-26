# AstroTrackAI

**Name:** [Annette Bazan]  
**Track Chosen:** Implementation Track

## Project Description
AstroTrackAI is an AI prototype that predicts asteroid movements using machine learning and alerts if an asteroid is at risk of approaching Earth.

## How to Run
1. Clone this repo
2. Install dependencies:
Python 3.11
Scikit-learn (for simple AI models)
Pandas (data handling)
Matplotlib (simple plots)
Maybe TensorFlow/PyTorch 
asteroid_tracker.py
Load data
Train a basic model
Predict asteroid paths
Alert if close to Earth
utils.py
Functions to load/save data
Basic math helpers if needed
3. Run the tracker:
python asteroid_tracker.py

## Files
- asteroid_tracker.py — Main script
- utils.py — Helper functions
- requirements.txt — Project dependencies
- docs/ — Full documentation
- slides/ — Project presentation slides

# Testing Plan
Create fake asteroid paths (simple coordinates over time)
Test if the model can predict future positions within an acceptable margin
Trigger an "alert" if distance to (0,0,0) Earth center is too small (< 10,000 km)
