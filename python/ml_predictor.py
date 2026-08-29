import joblib
import pandas as pd


model = joblib.load("netsage_model.pkl")


def predict_fault(
    packet_loss,
    interface_status,
    gateway_match,
    ip_match,
    subnet_match,
    router_ip_match
):
    data = pd.DataFrame([{
        "packet_loss": int(packet_loss),
        "interface_down": 1 if interface_status == "yes" else 0,
        "gateway_match": 1 if gateway_match == "yes" else 0,
        "ip_match": 1 if ip_match == "yes" else 0,
        "subnet_match": 1 if subnet_match == "yes" else 0,
        "router_ip_match": 1 if router_ip_match == "yes" else 0
    }])

    prediction = model.predict(data)[0]

    probabilities = model.predict_proba(data)[0]

    confidence = max(probabilities) * 100

    return prediction, round(confidence, 2)