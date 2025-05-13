# Solution of the problem.
def solution(N):
    binary = bin(N)[2:]
    binary_gaps = binary.split('1')

    max_gap = 0
    # Slice the list to exclude last binary gap.
    for gap in binary_gaps[:-1]:
        max_gap = max(len(gap), max_gap)

    return max_gap


# Test cases for solutions.
def testcases():
    testcase = [
        { 'N': 1041, 'answer': 5 },
        { 'N': 15, 'answer': 0 },
        { 'N': 32, 'answer': 0 },
        { 'N': 1, 'answer': 0 },
        { 'N': 9999, 'answer': 4 },
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
