from shap_explainer import explain_prediction


prediction, contributions = explain_prediction(
    "100",
    "no",
    "yes",
    "yes",
    "yes",
    "no"
)


print("\n======================================")
print("          NETSAGE SHAP TEST")
print("======================================")

print("\nPredicted Fault:")
print(prediction)

print("\nFeature Contributions:")

for _, row in contributions.iterrows():
    print(
        row["feature"],
        "→",
        round(row["shap_value"], 4)
    )

print("\nMajor Contributing Factor:")
print(contributions.iloc[0]["feature"])

print("======================================")