import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load sensor data
data = pd.read_csv("../data/sample_sensor_data.csv")

# Create labels based on suitable hydroponic conditions.
# This is a demonstration rule used to generate training labels.
def classify_condition(row):
    if (
        20 <= row["temperature_c"] <= 28
        and 55 <= row["humidity_percent"] <= 75
        and 5.5 <= row["ph"] <= 6.8
        and 500 <= row["nutrient_level"] <= 900
    ):
        return 1
    return 0


data["plant_health"] = data.apply(classify_condition, axis=1)

features = [
    "temperature_c",
    "humidity_percent",
    "ph",
    "nutrient_level"
]

X = data[features]
y = data["plant_health"]

# Train the machine-learning model
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("AI Hydroponic Plant Health Prediction")
print("--------------------------------------")
print(f"Model accuracy: {accuracy:.2f}")

# Test a new sensor reading
new_reading = pd.DataFrame([{
    "temperature_c": 25.0,
    "humidity_percent": 65.0,
    "ph": 6.2,
    "nutrient_level": 750
}])

prediction = model.predict(new_reading)[0]

if prediction == 1:
    print("Prediction: Suitable plant-growth conditions")
else:
    print("Prediction: Conditions require attention")
