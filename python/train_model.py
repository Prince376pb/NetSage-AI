import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


data = pd.read_csv("ml_dataset.csv")

features = [
    "packet_loss",
    "interface_down",
    "gateway_match",
    "ip_match",
    "subnet_match",
    "router_ip_match"
]

X = data[features]
y = data["fault"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)


print("\n======================================")
print("       NETSAGE RANDOM FOREST")
print("======================================")

print("\nTraining examples:", len(X_train))
print("Testing examples:", len(X_test))

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    zero_division=0
))


joblib.dump(model, "netsage_model.pkl")

print("\nModel saved as: netsage_model.pkl")
print("======================================")