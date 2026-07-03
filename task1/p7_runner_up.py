"""
Task 1 — Problem 7 (Easy): Find the Runner-Up Score

HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Adapted as a function so it can be tested automatically.
"""

sample_scores = [2, 3, 6, 6, 5]


def find_runner_up(scores: list[int]) -> int:
    """Return the runner-up score: the second highest *distinct* value.

    Example: [2, 3, 6, 6, 5] -> 5 (6 is the highest, 5 is the runner-up).
    """
    # TODO: Remove duplicate scores, then return the second largest value.
    unique_scores = []

    # 1. Remove duplicates manually.
    for score in scores:
        if score not in unique_scores:
            unique_scores.append(score)

    if len(unique_scores) < 2:
        raise ValueError("At least two distinct scores are required.")        

    # 2. Find the largest score.
    max_score = unique_scores[0]

    for unique_score in unique_scores:
        if unique_score > max_score:
            max_score = unique_score

    # 3. Remove the largest score.
    unique_scores.remove(max_score)

    # 4. Find the second largest score.
    runner_up = unique_scores[0]

    for unique_score in unique_scores:
        if unique_score > runner_up:
            runner_up = unique_score

    return runner_up


if __name__ == "__main__":
    print(find_runner_up(sample_scores))
