import pandas as pd
import matplotlib.pyplot as plt

# Load hydroponic sensor data
data = pd.read_csv("data/sample_sensor_data.csv")

# Display latest sensor reading
latest = data.iloc[-1]

print("=" * 50)
print("AI-IoT SMART HYDROPONIC MONITORING SYSTEM")
print("=" * 50)

print(f"Temperature   : {latest['temperature_c']} °C")
print(f"Humidity      : {latest['humidity_percent']} %")
print(f"pH            : {latest['ph']}")
print(f"Nutrient Level: {latest['nutrient_level']}")

# Simple condition assessment
if (
    20 <= latest["temperature_c"] <= 28
    and 55 <= latest["humidity_percent"] <= 75
    and 5.5 <= latest["ph"] <= 6.8
    and 500 <= latest["nutrient_level"] <= 900
):
    print("\nAI Status: Suitable growing conditions")
else:
    print("\nAI Status: Conditions require attention")

# Plot sensor parameters
plt.figure(figsize=(10, 6))

plt.plot(data["temperature_c"], label="Temperature (°C)")
plt.plot(data["humidity_percent"], label="Humidity (%)")
plt.plot(data["ph"], label="pH")
plt.plot(data["nutrient_level"], label="Nutrient Level")

plt.title("Hydroponic Sensor Monitoring")
plt.xlabel("Sensor Reading")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
