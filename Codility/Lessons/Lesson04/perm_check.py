# Solution of the problem.
def solution(A):
    # Sort in ascending order.
    A.sort()

    # Check if all elements are existing in the list.
    if all(a == i + 1 for i, a in enumerate(A)):
        return 1
    return 0


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [4, 1, 3, 2],
            'answer': 1,
        },
        {
            'A': [4, 1, 3],
            'answer': 0,
        },
        {
            'A': [4, 3, 3, 2],
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
