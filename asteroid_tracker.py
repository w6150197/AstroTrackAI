# asteroid_tracker.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# --- Load Data ---
def load_asteroid_data(file_path=None):
    if file_path:
        data = pd.read_csv(file_path)
    else:
        # Simulate fake asteroid data
        np.random.seed(42)
        time = np.arange(0, 100, 1)
        distance = 50000 - (time * np.random.uniform(400, 600)) + np.random.normal(0, 5000, size=time.shape)
        data = pd.DataFrame({'time': time, 'distance_km': distance})
    return data

# --- Train Model ---
def train_model(data):
    X = data[['time']]
    y = data['distance_km']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# --- Predict and Alert ---
def predict_and_alert(model, future_times):
    predictions = model.predict(future_times)
    for t, d in zip(future_times.flatten(), predictions):
        print(f"Time {t:.0f}: Predicted Distance = {d:.2f} km")
        if d < 10000:
            print("⚠️ ALERT: Asteroid dangerously close to Earth! ⚠️\n")

# --- Plot Results ---
def plot_data(data, model):
    plt.scatter(data['time'], data['distance_km'], color='blue', label='Observed Data')
    future_time = np.linspace(0, 120, 200).reshape(-1, 1)
    future_distance = model.predict(future_time)
    plt.plot(future_time, future_distance, color='red', label='Predicted Path')
    plt.xlabel('Time')
    plt.ylabel('Distance to Earth (km)')
    plt.title('Asteroid Distance Prediction')
    plt.legend()
    plt.grid(True)
    plt.show()

# --- Main ---
if __name__ == "__main__":
    data = load_asteroid_data()
    model = train_model(data)
    future_times = np.array([[100], [105], [110], [115], [120]])
    predict_and_alert(model, future_times)
    plot_data(data, model)
except Exception as e:
    print(f\"An error occurred: {e}\")
