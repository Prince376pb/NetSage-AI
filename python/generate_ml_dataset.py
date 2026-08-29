import csv
import random

random.seed(42)

rows = []

fault_patterns = {
    "Interface Down": {
        "interface_down": 1,
        "gateway_match": 1,
        "ip_match": 1,
        "subnet_match": 1,
        "router_ip_match": 1
    },
    "Wrong Gateway": {
        "interface_down": 0,
        "gateway_match": 0,
        "ip_match": 1,
        "subnet_match": 1,
        "router_ip_match": 1
    },
    "Wrong IP Address": {
        "interface_down": 0,
        "gateway_match": 1,
        "ip_match": 0,
        "subnet_match": 1,
        "router_ip_match": 1
    },
    "Wrong Subnet Mask": {
        "interface_down": 0,
        "gateway_match": 1,
        "ip_match": 1,
        "subnet_match": 0,
        "router_ip_match": 1
    },
    "Wrong Router Interface IP": {
        "interface_down": 0,
        "gateway_match": 1,
        "ip_match": 1,
        "subnet_match": 1,
        "router_ip_match": 0
    }
}

for fault, pattern in fault_patterns.items():

    for _ in range(100):

        packet_loss = random.choice([90, 95, 98, 99, 100])

        row = {
            "packet_loss": packet_loss,
            "interface_down": pattern["interface_down"],
            "gateway_match": pattern["gateway_match"],
            "ip_match": pattern["ip_match"],
            "subnet_match": pattern["subnet_match"],
            "router_ip_match": pattern["router_ip_match"],
            "fault": fault
        }

        rows.append(row)


random.shuffle(rows)

with open("ml_dataset.csv", "w", newline="") as file:

    fieldnames = [
        "packet_loss",
        "interface_down",
        "gateway_match",
        "ip_match",
        "subnet_match",
        "router_ip_match",
        "fault"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print("ML dataset created successfully.")
print("Total training examples:", len(rows))
print("Fault classes:", len(fault_patterns))
print("File saved as: ml_dataset.csv")