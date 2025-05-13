# Solution of the problem.
def solution(A):
    # Define total sum of list A and set minimum difference as infinity.
    total = sum(A)
    min_diff = float('inf')

    first_part = 0
    for i in range(len(A) - 1):
        first_part += A[i]
        second_part = total - first_part
        diff = abs(first_part - second_part)
        min_diff = min(min_diff, diff)

    return min_diff


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [3, 1, 2, 4, 3],
            'answer': 1,
        },
        {
            'A': [-1000, -500, 5, 1],
            'answer': 506,
        },
        {
            'A': [0, 0, 0, 0, 0, 0],
            'answer': 0,
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
