# Solution of the problem.
def solution(A):
    answer = 0
    total = sum(A)

    for car in A:
        # Return -1 if the number of pairs of passing cars exceeds 1,000,000,000.
        if answer > 1000000000:
            return -1

        if car == 0:
            answer += total
        else:
            total -= 1

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [0, 1, 0, 1, 1],
            'answer': 5,
        },
        {
            'A': [0, 1, 1],
            'answer': 2,
        },
        {
            'A': [0, 1, 0, 1],
            'answer': 3,
        },
        {
            'A': [0, 0, 1, 1],
            'answer': 4,
        },
        {
            'A': [0, 0, 0],
            'answer': 0,
        },
        {
            'A': [1, 1, 1],
            'answer': 0,
        },
        {
            'A': [1, 0, 1],
            'answer': 1,
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
