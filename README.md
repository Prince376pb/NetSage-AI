# NetSage-AI

## AI-Assisted Network Troubleshooting System

NetSage-AI is an AI-assisted network troubleshooting system designed to help identify and analyze common networking problems in Cisco Packet Tracer scenarios.

The system combines Packet Tracer evidence, AI-based diagnosis, Python rule-based validation, Machine Learning, SHAP explainability, and human review. The AI provides a recommendation, but the final decision remains with the human reviewer.

---

## Problem Statement

Network troubleshooting can take time because a network issue may have multiple possible causes. Students and network users may also find it difficult to identify the exact configuration mistake from symptoms alone.

NetSage-AI aims to assist in this process by analyzing the available network evidence and suggesting the most likely fault.

The system is designed around the following approach:

**Network Fault → Evidence Collection → AI Diagnosis → Python Rule Check → Compare Findings → Human Review → Fix → Verification**

---

## Solution

NetSage-AI does not automatically make the final network decision.

Instead, it follows a human-in-the-loop approach:

1. A networking fault is created in Cisco Packet Tracer.
2. The symptoms and network evidence are collected.
3. NetSage-AI analyzes the case and suggests a possible fault.
4. Python-based rules independently check common configuration errors.
5. AI and Python findings are compared.
6. A human reviews the recommendation.
7. The recommendation can be accepted, edited, or rejected.
8. The required network fix is applied.
9. The network is verified after the fix.
10. The result can be recorded for reporting and analysis.

---

## Key Features

- AI-assisted network fault diagnosis
- Cisco Packet Tracer based troubleshooting cases
- Python rule-based validation
- Machine Learning based fault prediction
- Random Forest model
- SHAP-based feature explainability
- Identification of major contributing factors
- Human review and decision tracking
- Verification result tracking
- Automatic report generation
- Dashboard for case and issue statistics

---

## Implemented Cases

The current project implementation contains **5 representative network troubleshooting cases**, as instructed for the project evaluation.

The implemented fault categories include:

1. Wrong Router Interface IP
2. Wrong Subnet Mask
3. Interface Down
4. Wrong Gateway
5. Wrong IP Address

The original problem statement describes a larger set of cases. This project prototype focuses on 5 cases as the assigned implementation scope.

---

## System Workflow

```text
Cisco Packet Tracer Case
          ↓
Symptoms + Network Evidence
          ↓
      AI Diagnosis
          ↓
   Python Rule Check
          ↓
   Compare Findings
          ↓
      Human Review
          ↓
 Accepted / Edited / Rejected
          ↓
       Apply Fix
          ↓
       Verification
          ↓
      Report / Dashboard
