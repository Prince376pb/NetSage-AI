import json
import os
from collections import Counter


print("\n==========================================")
print("          NETSAGE AI DASHBOARD")
print("==========================================")


try:
    with open("review_log.json", "r") as file:
        reviews = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    reviews = []


print("\nTotal Cases:", len(reviews))


faults = Counter(
    review["fault"]
    for review in reviews
)


print("\n========== ISSUE TYPES ==========")

for fault, count in faults.items():
    print(f"{fault}: {count}")


approved = sum(
    1 for review in reviews
    if review["human_decision"] == "Approved"
)

rejected = sum(
    1 for review in reviews
    if review["human_decision"] == "Rejected"
)


print("\n========== HUMAN DECISIONS ==========")
print("Approved:", approved)
print("Rejected:", rejected)


print("\n========== VERIFICATION ==========")

successful = sum(
    1 for review in reviews
    if review.get("verification") == "Successful"
)

failed = sum(
    1 for review in reviews
    if review.get("verification") == "Failed"
)

not_recorded = sum(
    1 for review in reviews
    if review.get("verification") not in ["Successful", "Failed"]
)

print("Successful:", successful)
print("Failed:", failed)
print("Not Recorded:", not_recorded)

print("\n========== REPORTS ==========")

if os.path.exists("reports"):
    reports = [
        file for file in os.listdir("reports")
        if file.endswith(".txt")
    ]

    print("Reports Generated:", len(reports))

else:
    print("Reports Generated: 0")


print("\n==========================================")