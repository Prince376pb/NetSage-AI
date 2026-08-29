import joblib
import pandas as pd

model = joblib.load("netsage_model.pkl")

test_cases = pd.DataFrame([
    [100, 0, 1, 1, 0, 1],
    [100, 1, 1, 1, 1, 1],
    [100, 0, 0, 1, 1, 1],
    [100, 0, 1, 0, 1, 1],
    [100, 0, 1, 1, 1, 0]
], columns=[
    "packet_loss",
    "interface_down",
    "gateway_match",
    "ip_match",
    "subnet_match",
    "router_ip_match"
])

expected = [
    "Wrong Subnet Mask",
    "Interface Down",
    "Wrong Gateway",
    "Wrong IP Address",
    "Wrong Router Interface IP"
]

predictions = model.predict(test_cases)

print("\n======================================")
print("       NETSAGE ML CASE TEST")
print("======================================")

for i in range(len(predictions)):
    print("\nCASE0" + str(i + 1))
    print("Expected :", expected[i])
    print("Predicted:", predictions[i])

print("\n======================================")