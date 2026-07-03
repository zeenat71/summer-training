"""
Task 1 — Slicing and Loops

Practice slicing, loops, enumerate, zip, and comprehensions.
Complete this file without using AI tools.
"""

patient_ids = [101, 102, 103, 104, 105, 106, 107]
patient_names = ["Ayesha", "Omar", "Sara", "Bilal", "Hina", "Usman", "Maha"]


def slicing_examples():
    """Return examples of list slicing."""
    # TODO: Return first three IDs, last three IDs, and reversed IDs.
    return (patient_ids[:3], patient_ids[-3:], patient_ids[::-1])


def loop_examples():
    """Practice range, enumerate, and zip."""
    # TODO: Use enumerate to print numbered patient names.
    # TODO: Use zip to pair IDs with names.
    for z, p_names in enumerate(patient_names):
        print(z, p_names)

    for i, p_name in zip(patient_ids, patient_names):
        print(i, p_name)


def comprehension_examples():
    """Return values created using comprehensions."""
    # TODO: Create a list of even patient IDs.
    # TODO: Create uppercase patient names.

    list_of_even_id_patients = [i for i in patient_ids if i % 2 == 0]

    upper_patient_names = [name.upper() for name in patient_names]

    return list_of_even_id_patients, upper_patient_names


if __name__ == "__main__":
    print(slicing_examples())
    loop_examples()
    print(comprehension_examples())
