"""
Task 1 — Dictionary Analysis

Practice dictionaries and nested dictionaries.
Complete this file without using AI tools.
"""

patients = {
    1: {
        "name": "Ayesha Khan",
        "age": 32,
        "contact": {"city": "Karachi", "phone": "000-000"},
        "condition": "diabetes",
    },
    2: {
        "name": "Omar Ali",
        "age": 45,
        "contact": {"city": "Lahore", "phone": "111-111"},
        "condition": "hypertension",
    },
}


def get_patient_city(patient_id):
    """Return the city for a given patient ID."""
    p_id = patients.get(patient_id)

    if p_id:
        return p_id["contact"]["city"]

    return None


def update_patient_condition(patient_id, new_condition):
    """Update a patient's condition."""
    p_id = patients.get(patient_id)

    if p_id:
        p_id["condition"] = new_condition
    else:
        return "patient_id not found"


def build_patient_summary():
    """Build and return a summary dictionary."""
    patient_count = 0
    conditions = []
    cities = []
    age = 0

    for i in patients:
        p_id = patients[i]

        patient_count = patient_count + 1
        conditions.append(p_id["condition"])
        cities.append(p_id["contact"]["city"])
        age = age + p_id["age"]

    average_age = age / patient_count

    return {
        "total_patients": patient_count,
        "conditions": conditions,
        "cities": cities,
        "average_age": average_age,
    }


if __name__ == "__main__":
    print("City_of_patient1:", get_patient_city(1))
    print("City_of_patient2:", get_patient_city(2))
    print("City_of_patient3:", get_patient_city(3))

    print()

    update_patient_condition(1, "asthma")
    print("Updated patient 1:", patients[1])

    print()

    print("Patient Summary:")
    print(build_patient_summary())
