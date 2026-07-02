"""
Task 1 — Patient Summary

Complete this file without using AI tools.
Use fake/sample data only.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "condition": "diabetes", "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "condition": "hypertension", "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "condition": "asthma", "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "condition": "diabetes", "active": True},
]


def total_patients(patient_records):
    """Return the total number of patients."""
    patient_count = 0
    for i in patient_records:
        patient_count = patient_count + 1
    return patient_count


def average_age(patient_records):
    """Return the average patient age."""
    total_patients = 0
    age = 0
    for i in patient_records:
        total_patients = total_patients + 1
        age = age + i["age"]
    average_age = age / total_patients
    return average_age


def count_active_patients(patient_records):
    """Return the number of active patients."""
    total_active = 0
    for i in patient_records:
        if i["active"]:
            total_active = total_active + 1
    return total_active


def unique_conditions(patient_records):
    """Return a sorted list of unique conditions."""
    conditions = set()

    for patient in patient_records:
        conditions.add(patient["condition"])

    return sorted(conditions)


def count_by_condition(patient_records):
    """Return a dictionary containing patient count by condition."""
    # total unique conditions
    conditions = []

    for i in patient_records:
        if i["condition"] not in conditions:
            conditions.append(i["condition"])

    sorted_list = sorted(conditions)

    # loop on each condition for patient count
    result = {}

    for i in sorted_list:
        count_of_patients = 0

        for j in patient_records:
            if j["condition"] == i:
                count_of_patients += 1

        result[i] = count_of_patients

    return result


if __name__ == "__main__":
    print("Total patients:", total_patients(patients))
    print("Average age:", average_age(patients))
    print("Active patients:", count_active_patients(patients))
    print("Unique conditions:", unique_conditions(patients))
    print("Count by condition:", count_by_condition(patients))
