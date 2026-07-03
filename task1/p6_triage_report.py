"""
Task 1 — Final Problem: Triage Report

Complete this file without using AI tools.
Use fake/sample data only.

Tip: collections.Counter can make counting by risk label easier, but a
plain dictionary works too — import it yourself if you want to use it.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "risk_score": 72, "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "risk_score": 88, "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "risk_score": 35, "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "risk_score": 91, "active": True},
]


def label_risk(risk_score: int) -> str:
    """Return low, medium, or high based on risk score."""
    # TODO: Define thresholds and return label.
    if risk_score >= 75:
        return "high"
    elif risk_score >= 50:
        return "medium"
    else:
        return "low"


def add_risk_labels(patient_records: list[dict]) -> list[dict]:
    """Return copies of patient records with a risk_label field added."""
    # TODO: Add risk labels without modifying original records.
    patients_with_labels = []

    for i in patient_records:
        p_copy = i.copy()

        risk_label = label_risk(i["risk_score"])

        p_copy["risk_label"] = risk_label

        patients_with_labels.append(p_copy)

    return patients_with_labels


def build_triage_report(patient_records: list[dict]) -> dict:
    """Build a triage report from patient records."""
    # TODO: Build and return final report.

    patients_with_labels = add_risk_labels(patient_records)

    total_patients = len(patients_with_labels)
    active_patients = 0

    high = 0
    medium = 0
    low = 0

    active_high_risk = []

    for i in patients_with_labels:
        if i["active"]:
            active_patients += 1

        if i["risk_label"] == "high":
            high += 1

            if i["active"]:
                active_high_risk.append(i)

        elif i["risk_label"] == "medium":
            medium += 1
        else:
            low += 1

    return {
        "summary": {"total_patients": total_patients, "active_patients": active_patients},
        "risk_counts": {"high": high, "medium": medium, "low": low},
        "active_high_risk_patients": active_high_risk,
    }


if __name__ == "__main__":
    # TODO: Add assertions after implementing the functions.
    report = build_triage_report(patients)
    print(report)

    assert label_risk(91) == "high"
    assert label_risk(72) == "medium"
    assert label_risk(35) == "low"

    print("All assertions passed.")
