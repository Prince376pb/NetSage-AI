import os
from datetime import datetime


def generate_report(
    packet_loss,
    interface_status,
    gateway_match,
    ip_match,
    subnet_match,
    router_ip_match,
    diagnosis,
    ml_fault,
    ml_confidence,
    major_factor,
    final_fault,
    final_confidence,
    agreement
):
    report = []

    report.append("==========================================")
    report.append("           NETSAGE AI REPORT")
    report.append("==========================================")

    report.append("")
    report.append(
        "Date and Time: " +
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    report.append("")
    report.append("NETWORK EVIDENCE")
    report.append("------------------------------------------")
    report.append("Packet Loss: " + packet_loss + "%")
    report.append("Router Interface Down: " + interface_status)
    report.append("Gateway Match: " + gateway_match)
    report.append("IP Address Match: " + ip_match)
    report.append("Subnet Mask Match: " + subnet_match)
    report.append("Router Interface IP Match: " + router_ip_match)

    report.append("")
    report.append("RULE-BASED DIAGNOSIS")
    report.append("------------------------------------------")
    report.append("Fault: " + diagnosis["fault"])
    report.append("Confidence: " + str(diagnosis["confidence"]) + "%")

    report.append("")
    report.append("REASON")
    report.append("------------------------------------------")
    report.append(diagnosis["reason"])

    report.append("")
    report.append("RECOMMENDED ACTION")
    report.append("------------------------------------------")
    report.append(diagnosis["recommended_action"])

    report.append("")
    report.append("MACHINE LEARNING PREDICTION")
    report.append("------------------------------------------")
    report.append("Predicted Fault: " + ml_fault)
    report.append("ML Confidence: " + str(ml_confidence) + "%")

    report.append("")
    report.append("AI EXPLANATION")
    report.append("------------------------------------------")
    report.append("Major Contributing Factor: " + str(major_factor))

    report.append("")
    report.append("FINAL NETSAGE DIAGNOSIS")
    report.append("------------------------------------------")
    report.append("Final Fault: " + final_fault)
    report.append("Final Confidence: " + str(final_confidence) + "%")
    report.append("AI/Rule Agreement: " + agreement)

    report.append("")
    report.append("VERIFICATION")
    report.append("------------------------------------------")
    report.append(
        "After applying the recommended fix, "
        "perform a connectivity test and confirm "
        "that packet loss is 0%."
    )

    report.append("")
    report.append("==========================================")

    return "\n".join(report)


def save_report(report, case_id):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{case_id}_{timestamp}_report.txt"

    with open(filename, "w") as file:
        file.write(report)

    print("\nReport saved as:", filename)