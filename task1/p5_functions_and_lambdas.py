"""
Task 1 — Functions and Lambda Functions

Practice reusable functions, type hints, and lambda functions.
Complete this file without using AI tools.
"""

patients = [
    {"name": "ayesha khan", "height_m": 1.65, "weight_kg": 68, "active": True},
    {"name": "omar ali", "height_m": 1.78, "weight_kg": 82, "active": False},
    {"name": "sara ahmed", "height_m": 1.60, "weight_kg": 54, "active": True},
]


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI."""
    # TODO: Implement BMI formula.
    BMI = weight_kg / (height_m * height_m)
    return BMI


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    # TODO: Return underweight, normal, overweight, or obese.
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


def format_name(name: str) -> str:
    """Convert a name to title case."""
    # TODO: Format name.
    words = name.split()
    List_of_title_case = []

    for w in words:
        List_of_title_case.append(w[0].upper() + w[1:].lower())

    return " ".join(List_of_title_case)


def get_active_patients(patient_records: list[dict]) -> list[dict]:
    """Return active patients only."""
    # TODO: Filter active patients.
    list_of_active_patients = []

    for i in patient_records:
        if i["active"]:
            list_of_active_patients.append(i)

    return list_of_active_patients


def sort_patients_by_weight(patient_records: list[dict]) -> list[dict]:
    """Return patients sorted by weight using a lambda."""

    # TODO: Sort patients by weight_kg.
    def get_weight(x):
        return x["weight_kg"]

    return sorted(patient_records, key=get_weight)


if __name__ == "__main__":
    # TODO: Call your functions and print useful output.

    print("-- BMI + Catergory --")
    for p in patients:
        BMI = calculate_bmi(p["weight_kg"], p["height_m"])
        category = classify_bmi(BMI)
        print(p["name"], "->", BMI, "->", category)

    print("-- Active Patients --")
    print(get_active_patients(patients))

    print()

    print("-- Sorted by Weight --")
    print(sort_patients_by_weight(patients))
