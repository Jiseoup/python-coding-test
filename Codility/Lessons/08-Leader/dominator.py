# Solution of the problem.
def solution(A):
    candidates = {}

    for idx, num in enumerate(A):
        candidates[num] = candidates.get(num, 0) + 1

        # If dominator exists, return index.
        if candidates.get(num, 0) > len(A) / 2:
            return idx

    return -1


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [3, 4, 3, 2, 3, -1, 3, 3],
            'answer': [0, 2, 4, 6, 7],
        },
        {
            'A': [3, 4, 3, 2],
            'answer': [-1],
        },
        {
            'A': [],
            'answer': [-1],
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('A'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer in answer:
            print(f'✅ (Correct) Answer: One of element in {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: One of element in {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
