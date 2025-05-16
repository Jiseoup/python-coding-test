# Solution of the problem.
import sys

def solution(A):
    dice = range(1, 7)
    board_size = len(A)

    # Create result list for accumulate maximum value and initialize first value as A[0].
    result = [-sys.maxsize] * board_size
    result[0] = A[0]

    # Accumulate possible maximum board value to the result list for each index.
    for idx in range(1, board_size):
        for value in dice:
            if idx - value >= 0:
                result[idx] = max(result[idx], result[idx - value] + A[idx])

    return result[-1]


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [1, -2, 0, 9, -1, -2],
            'answer': 8,
        },
        {
            'A': [1, -2, -8, -5, -1, -2, -3, 1, 2],
            'answer': 3,
        },
        {
            'A': [-5, -190],
            'answer': -195,
        },
        {
            'A': [1, -2, -2, -2, 100],
            'answer': 101,
        },
        {
            'A': [0, -10, -10, 100, -100, 100, 100],
            'answer': 300,
        },
        {
            'A': [0, -5, -5, -5, -5, -5, -5, 100, 100],
            'answer': 195,
        },
        {
            'A': [0, -100, -100, -100, -100, -100, -50, 100, 100, 100],
            'answer': 250,
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('A'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
