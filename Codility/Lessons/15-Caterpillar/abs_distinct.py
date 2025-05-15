# Solution of the problem.
def solution(A):
    return len(set(map(abs, A)))


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [-5, -3, -1, 0, 3, 6],
            'answer': 5,
        },
        {
            'A': [-5, -3, 1, 1, 2, 3],
            'answer': 4,
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
