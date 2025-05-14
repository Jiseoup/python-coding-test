# Solution of the problem.
def triplet(p: int, q: int, r: int) -> bool:
    """Check that the triplet satisfies the triangular.

    Args:
        p (int): First integer value of the triplet.
        q (int): Second integer value of the triplet.
        r (int): Third integer value of the triplet.

    Returns:
        bool: True or False.
    """
    if p + q > r and q + r > p and r + p > q:
        return True
    return False

def solution(A):
    # Sort the list in ascending order.
    A.sort()

    # Check all possible triplet combinations.
    for i in range(len(A) - 2):
        triangular = triplet(A[i], A[i + 1], A[i + 2])
        if triangular:
            return 1
    return 0


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [10, 2, 5, 1, 8, 20],
            'answer': 1,
        },
        {
            'A': [10, 50, 5, 1],
            'answer': 0,
        },
        {
            'A': [],
            'answer': 0,
        },
        {
            'A': [-100, 50, -200, 30, 1],
            'answer': 0,
        },
        {
            'A': [1, 1, 1],
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
