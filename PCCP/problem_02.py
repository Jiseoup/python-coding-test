"""PCCP 기출문제 / Level 2. 퍼즐 게임 챌린지"""


# Solution of the problem.
from typing import List, Tuple

def solve(puzzle: List[Tuple[int]], limit: int) -> int:
    """
    Find the minimum level required to solve all puzzles within the time limit using binary search.

    args:
        puzzle (List[Tuple[int]]): A list of tuples, contains diffs and times.
        limit (int): Allowed time to solve all puzzles.

    returns:
        result (int): Minimum level to solve all puzzles.
    """
    min_level = 1
    max_level = max(diff for diff, _ in puzzle)
    result = max_level

    # Loop until the minimum level to solve all puzzles is found.
    while min_level <= max_level:
        time_cur = 0
        time_prev = 0

        # Calculate the middle level in binary search.
        level = (min_level + max_level) // 2

        # Iterate all puzzles.
        for diff, time in puzzle:
            if diff <= level:
                time_cur += time
            else:
                time_cur += (diff - level) * (time + time_prev) + time
            # Store the previous time.
            time_prev = time

        # If all puzzles are solved in the limit.
        if time_cur <= limit:
            max_level = level - 1
            result = level
        else:
            min_level = level + 1

    return result

def solution(diffs, times, limit):
    puzzle = list(zip(diffs, times))
    answer = solve(puzzle, limit)
    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'diffs': [1, 5, 3],
            'times': [2, 4, 7],
            'limit': 30,
        },
        {
            'diffs': [1, 4, 4, 2],
            'times': [6, 3, 8, 2],
            'limit': 59,
        },
        {
            'diffs': [1, 328, 467, 209, 54],
            'times': [2, 7, 1, 4, 3],
            'limit': 1723,
        },
        {
            'diffs': [1, 99999, 100000, 99995],
            'times': [9999, 9001, 9999, 9001],
            'limit': 3456789012,
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('diffs'), testcase.get('times'), testcase.get('limit'))
        print(answer)


if __name__ == '__main__':
    main()
