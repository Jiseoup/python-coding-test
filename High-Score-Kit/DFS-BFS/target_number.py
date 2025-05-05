"""코딩테스트 고득점 Kit / Level 2. 타겟 넘버"""


# Solution of the problem.
""" Solution 1 : Using DFS """
from typing import List

def dfs(idx: int, total: int, numbers: List[int], target: int):
    results = 0

    # Check if all numbers are used.
    if idx == len(numbers):
        # If total matches the target, return 1.
        if total == target:
            return 1
        else:
            return 0

    # Recursively explore both `plus` and `minus` choices, and sum the valid cases as a results.
    results += dfs(idx + 1, total + numbers[idx], numbers, target)
    results += dfs(idx + 1, total - numbers[idx], numbers, target)

    return results

def solution(numbers, target):
    answer = dfs(0, 0, numbers, target)
    return answer

# """ Solution 2 : Using BFS """
# def solution(numbers, target):
#     answer = 0
#     nodes = [0]

#     # Store all possible calculation results in the `nodes` list.
#     for number in numbers:
#         step = []

#         for node in nodes:
#             step.append(node + number)
#             step.append(node - number)

#         # Store all possible calculation results for the next iteration.
#         nodes = step

#     # Count how many results match the target value.
#     for node in nodes:
#         if node == target:
#             answer += 1

#     return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'numbers': [1, 1, 1, 1, 1],
            'target': 3,
        },
        {
            'numbers': [4, 1, 2, 1],
            'target': 4,
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('numbers'), testcase.get('target'))
        print(answer)


if __name__ == '__main__':
    main()
