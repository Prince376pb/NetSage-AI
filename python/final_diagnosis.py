def get_final_diagnosis(
    rule_result,
    ml_fault,
    ml_confidence,
    major_factor
):
    rule_fault = rule_result["fault"]

    if rule_fault == ml_fault:
        agreement = "Agreed"

        final_fault = ml_fault

        final_confidence = round(
            (rule_result["confidence"] + ml_confidence) / 2,
            2
        )

    else:
        agreement = "Disagreed"

        final_fault = rule_fault
        final_confidence = rule_result["confidence"]

    return {
        "fault": final_fault,
        "confidence": final_confidence,
        "major_factor": major_factor,
        "agreement": agreement
    }