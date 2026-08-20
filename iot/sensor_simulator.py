import random
import csv
from datetime import datetime

OUTPUT_FILE = "../data/sample_sensor_data.csv"

def generate_sensor_data(samples=100):
    data = []

    for _ in range(samples):
        temperature = round(random.uniform(20, 35), 2)
        humidity = round(random.uniform(45, 85), 2)
        ph = round(random.uniform(5.0, 7.5), 2)
        nutrient_level = round(random.uniform(300, 1200), 2)

        data.append([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            temperature,
            humidity,
            ph,
            nutrient_level
        ])

    return data


def save_data(data):
    with open(OUTPUT_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "temperature_c",
            "humidity_percent",
            "ph",
            "nutrient_level"
        ])

        writer.writerows(data)


if __name__ == "__main__":
    sensor_data = generate_sensor_data(100)
    save_data(sensor_data)

    print("Sensor data generated successfully.")
    print(f"Number of samples: {len(sensor_data)}")
