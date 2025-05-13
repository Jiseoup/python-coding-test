# Solution of the problem.
def solution(A, B, K):
    # Number of integers divisible by K, in range from 1 to B.
    all_count = B // K
    # Number of integers divisible by K, in range from 1 to A - 1.
    part_count = (A - 1) // K

    return all_count - part_count


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': 6,
            'B': 11,
            'K': 2,
            'answer': 3,
        },
        {
            'A': 1,
            'B': 5,
            'K': 1,
            'answer': 5,
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('A'), testcase.get('B'), testcase.get('K'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
