# Solution of the problem.
def solution(A, B):
    # Sort segments by their end positions.
    segments = sorted(zip(A, B), key=lambda x: x[1])

    count = 0
    last_end = -1

    # Greedily select non-overlapping segments.
    for start, end in segments:
        if start > last_end:
            count += 1
            last_end = end

    return count


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [1, 3, 7, 9, 9],
            'B': [5, 6, 8, 9, 10],
            'answer': 3,
        },
        {
            'A': [0, 3, 4],
            'B': [5, 5, 5],
            'answer': 1,
        },
        {
            'A': [0, 3, 1],
            'B': [1, 5, 3],
            'answer': 2,
        },
        {
            'A': [0, 1, 2, 3, 4],
            'B': [9, 1, 2, 3, 4],
            'answer': 4,
        },
        {
            'A': [1, 3, 7, 9, 9],
            'B': [5, 8, 8, 10, 10],
            'answer': 3,
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('A'), testcase.get('B'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
