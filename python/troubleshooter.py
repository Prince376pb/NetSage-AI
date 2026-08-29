import json
from report_generator import generate_report, save_report
from ml_predictor import predict_fault
from shap_explainer import explain_prediction
from final_diagnosis import get_final_diagnosis
def save_review(case_id, fault, confidence, decision, verification):
    review = {
        "case_id": case_id,
        "fault": fault,
        "confidence": confidence,
        "human_decision": decision,
        "verification": verification
    }

    try:
        with open("review_log.json", "r") as file:
            reviews = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        reviews = []

    reviews.append(review)

    with open("review_log.json", "w") as file:
        json.dump(reviews, file, indent=4)

    print("\nHuman review and verification saved to review_log.json")
# Load case data
with open("cases.json", "r") as file:
    cases = json.load(file)


def diagnose_evidence(packet_loss, interface_status, gateway_match, ip_match, subnet_match):
    possible_faults = []

    if subnet_match == "no":
        possible_faults.append({
            "fault": "Wrong Subnet Mask",
            "confidence": 95,
            "reason": "The Server0 subnet mask does not match the expected network configuration.",
            "recommended_action": "Set Server0 subnet mask to 255.255.255.0."
        })

    elif interface_status == "yes":
        possible_faults.append({
            "fault": "Interface Down",
            "confidence": 95,
            "reason": "The router interface is administratively down.",
            "recommended_action": "Enable the affected router interface using the no shutdown command."
        })

    elif gateway_match == "no":
        possible_faults.append({
            "fault": "Wrong Gateway",
            "confidence": 95,
            "reason": "The configured default gateway does not match the router gateway.",
            "recommended_action": "Correct the device default gateway so that it matches the router gateway."
        })

    elif ip_match == "no":
        possible_faults.append({
            "fault": "Wrong IP Address",
            "confidence": 90,
            "reason": "The device IP address does not match the expected network configuration.",
            "recommended_action": "Correct the device IP address according to the expected network configuration."
        })

    elif packet_loss == "100" and gateway_match == "yes" and ip_match == "yes" and subnet_match == "yes":
        possible_faults.append({
            "fault": "Wrong Router Interface IP",
            "confidence": 90,
            "reason": "The device configuration appears correct, but complete packet loss indicates a possible mismatch in the router interface IP configuration.",
            "recommended_action": "Check the router interface IP address and restore it to the expected gateway address."
        })

    elif packet_loss == "100":
        possible_faults.append({
            "fault": "Unknown Connectivity Problem",
            "confidence": 50,
            "reason": "Complete packet loss was detected, but the available evidence does not identify a specific fault.",
            "recommended_action": "Collect additional network evidence such as interface status, IP configuration, gateway configuration, and routing information."
        })

    return possible_faults


print("\n==========================================")
print("          NETSAGE AI TROUBLESHOOTER")
print("==========================================")
case_id = input(
    "\nEnter Case ID (CASE01-CASE05): "
).strip().upper()
# Find the selected case in cases.json
selected_case = None

for case in cases:
    if case["case_id"] == case_id:
        selected_case = case
        break

if selected_case is None:
    print("\nInvalid Case ID.")
    print("Please enter CASE01, CASE02, CASE03, CASE04, or CASE05.")
    exit()

print("\n========== CASE INFORMATION ==========")
print("Device:", selected_case["device"])
print("Expected Fault:", selected_case["fault_type"])
print("Expected Symptom:", selected_case["symptom"])
print("Expected Packet Loss:", selected_case["packet_loss"])
print("Recommended Action:", selected_case["correct_action"])
# Collect network evidence
packet_loss = input(
    "\nEnter packet loss percentage: "
).strip()
# Validate packet loss against the selected case
expected_packet_loss = selected_case["packet_loss"].replace("%", "")

if packet_loss != expected_packet_loss:
    print("\nWARNING: Packet loss does not match the selected case.")
    print("Expected:", expected_packet_loss + "%")
    print("Entered:", packet_loss + "%")

interface_status = input(
    "Is the router interface down? (yes/no): "
).strip().lower()


gateway_match = input(
    "Does the device gateway match the router gateway? (yes/no): "
).strip().lower()


ip_match = input(
    "Does the device IP match the expected IP? (yes/no): "
).strip().lower()
subnet_match = input(
    "Does the device subnet mask match the expected subnet mask? (yes/no): "
).strip().lower()
router_ip_match = input(
    "Does the router interface IP match the expected IP? (yes/no): "
).strip().lower()
# Validate evidence against the selected case
# Validate evidence against the selected case
expected = selected_case["expected_evidence"]

if (
    interface_status != expected["interface"]
    or gateway_match != expected["gateway"]
    or ip_match != expected["ip"]
    or subnet_match != expected["subnet"]
):
    print("\nWARNING: Network evidence does not fully match the selected case.")

    if interface_status != expected["interface"]:
        print("Interface evidence mismatch.")

    if gateway_match != expected["gateway"]:
        print("Gateway evidence mismatch.")

    if ip_match != expected["ip"]:
        print("IP address evidence mismatch.")

    if subnet_match != expected["subnet"]:
        print("Subnet mask evidence mismatch.")
# Run diagnosis
results = diagnose_evidence(
    packet_loss,
    interface_status,
    gateway_match,
    ip_match,
    subnet_match
)
ml_fault, ml_confidence = predict_fault(
    packet_loss,
    interface_status,
    gateway_match,
    ip_match,
    subnet_match,
    router_ip_match
)
print("\n========== ML PREDICTION ==========")
print("Predicted Fault:", ml_fault)
print("ML Confidence:", str(ml_confidence) + "%")
shap_fault, shap_contributions = explain_prediction(
    packet_loss,
    interface_status,
    gateway_match,
    ip_match,
    subnet_match,
    router_ip_match
)

print("\n========== AI EXPLANATION ==========")
print("Major Contributing Factor:", shap_contributions.iloc[0]["feature"])
final_result = get_final_diagnosis(
    results[0],
    ml_fault,
    ml_confidence,
    shap_contributions.iloc[0]["feature"]
)

print("\n========== FINAL NETSAGE DIAGNOSIS ==========")
print("Final Fault:", final_result["fault"])
print("Final Confidence:", str(final_result["confidence"]) + "%")
print("AI/Rule Agreement:", final_result["agreement"])
print("Major Contributing Factor:", final_result["major_factor"])
# Display diagnosis
print("\n============== DIAGNOSIS ==============")

if results:

    for result in results:

        print("\nPossible Fault:")
        print(result["fault"])

        print("\nConfidence:")
        print(str(result["confidence"]) + "%")

        print("\nReason:")
        print(result["reason"])

        print("\nRecommended Action:")
        print(result["recommended_action"])

else:

    print("No specific fault detected.")

if results:
    
    report = generate_report(
        packet_loss,
        interface_status,
        gateway_match,
        ip_match,
        subnet_match,
        router_ip_match,
        results[0],
        ml_fault,
        ml_confidence,
        shap_contributions.iloc[0]["feature"],
        final_result["fault"],
        final_result["confidence"],
        final_result["agreement"]
    )

    save_report(report, case_id)

    print("\n========== HUMAN REVIEW ==========")

    approval = input(
        "Do you approve this recommended action? (yes/no): "
    ).strip().lower()

    if approval == "yes":

        print("\nAction approved by human reviewer.")
        print("Please apply the recommended fix manually.")
        print("After applying the fix, perform the verification test.")
        verification = input(
            "Was the problem fixed and verified? (yes/no): "
        ).strip().lower()

        if verification == "yes":
            verification_result = "Successful"

        elif verification == "no":
            verification_result = "Failed"

        else:
            verification_result = "Not Recorded"

        save_review(
            case_id,
            results[0]["fault"],
            results[0]["confidence"],
            "Approved",
            verification_result
        )

       

    elif approval == "no":

        print("\nAction rejected by human reviewer.")
        print("No corrective action should be applied.")

        save_review(
            case_id,
            results[0]["fault"],
            results[0]["confidence"],
            "Rejected",
            "Not Performed"
        )

    else:

        print("\nInvalid response. Please enter yes or no.")
else:
    print("No specific fault detected.")
print("\n========================================")
print("             END OF ANALYSIS")
print("========================================")