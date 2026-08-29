import joblib
import shap
import pandas as pd


model = joblib.load("netsage_model.pkl")

features = [
    "packet_loss",
    "interface_down",
    "gateway_match",
    "ip_match",
    "subnet_match",
    "router_ip_match"
]


def explain_prediction(
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

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(data)

    prediction = model.predict(data)[0]

    class_index = list(model.classes_).index(prediction)

    values = shap_values[:, :, class_index][0]

    contributions = pd.DataFrame({
        "feature": features,
        "shap_value": values
    })

    contributions["absolute_value"] = contributions["shap_value"].abs()

    contributions = contributions.sort_values(
        "absolute_value",
        ascending=False
    )

    return prediction, contributions