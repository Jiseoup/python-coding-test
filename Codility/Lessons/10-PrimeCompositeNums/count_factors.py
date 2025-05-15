# Solution of the problem.
def solution(N):
    count = 0
    int_sqrt = int(N ** 0.5)

    for factor in range(1, int_sqrt + 1):
        # If factor is square root of the number, add 1 count.
        if factor ** 2 == N:
            count += 1
            continue

        # If number is divisible with the factor, add 2 count.
        if N % factor == 0:
            count += 2

    return count


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'N': 24,
            'answer': 8,
        },
        {
            'N': 7,
            'answer': 2,
        },
        {
            'N': 16,
            'answer': 5,
        },
        {
            'N': 2,
            'answer': 2,
        },
        {
            'N': 1,
            'answer': 1,
        },
        {
            'N': 4,
            'answer': 3,
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('N'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
