"""
Task 1 — Collection Operations

Practice lists, tuples, and sets.
Complete this file without using AI tools.
"""

# Sample data — do not edit.
sample_conditions = ["diabetes", "asthma", "hypertension"]
primary_conditions = {"diabetes", "asthma", "hypertension"}
follow_up_conditions = {"asthma", "cardiac", "diabetes"}


def list_operations(conditions: list[str]) -> list[str]:
    """Return a new, sorted list after adding and removing a condition.

    Steps:
    - Work on a copy so the input list is not modified.
    - Add "cardiac".
    - Remove "asthma".
    - Return the list sorted alphabetically.
    """
    copy_of_conditions = []

    for i in conditions:
        copy_of_conditions.append(i)

    copy_of_conditions.append("cardiac")
    copy_of_conditions.remove("asthma")

    sorted_list = sorted(copy_of_conditions)
    return sorted_list


def set_operations(primary: set[str], follow_up: set[str]) -> dict[str, set[str]]:
    """Return common, all-unique, and primary-only conditions."""
    common_conditions = primary.intersection(follow_up)

    unique_conditions = primary.union(follow_up)

    primary_only_conditions = primary.difference(follow_up)

    """ Return a dictionary with these keys:
    - "common": conditions in both sets
    - "all_unique": every condition across both sets
    - "only_primary": conditions in primary but not in follow_up
    """

    dic_of_conditions = {
        "common": common_conditions,
        "all_unique": unique_conditions,
        "only_primary": primary_only_conditions,
    }

    return dic_of_conditions


if __name__ == "__main__":
    print(list_operations(sample_conditions))
    print(set_operations(primary_conditions, follow_up_conditions))
