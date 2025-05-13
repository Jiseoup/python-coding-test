from collections import deque

# Solution of the problem.
def solution(A, K):
    # Return empty list if A is empty.
    if not A:
        return []

    # Make list as a queue.
    queue = deque(A)

    # Rotate the list for K times.
    for _ in range(K):
        queue.appendleft(queue.pop())

    return list(queue)


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [3, 8, 9, 7, 6],
            'K': 3,
            'answer': [9, 7, 6, 3, 8],
        },
        {
            'A': [0, 0, 0],
            'K': 1,
            'answer': [0, 0, 0],
        },
        {
            'A': [1, 2, 3, 4],
            'K': 4,
            'answer': [1, 2, 3, 4],
        },
        {
            'A': [3, 8, 9, 7, 6],
            'K': 0,
            'answer': [3, 8, 9, 7, 6],
        },
        {
            'A': [-500, -100, 10, 20],
            'K': 3,
            'answer': [-100, 10, 20, -500],
        },
        {
            'A': [],
            'K': 3,
            'answer': [],
        },
        {
            'A': [],
            'K': 0,
            'answer': [],
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('A'), testcase.get('K'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
