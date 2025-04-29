"""[PCCE 기출문제] 10번 / 공원"""


from typing import List


# Solution of the problem.
X_RANGE = 0
Y_RANGE = 0

def can_place(
    mat: int, park: List[List[int]], i: int, j: int
) -> bool:
    # Prevent index out of range error.
    if i + mat > X_RANGE or j + mat > Y_RANGE:
        return False

    # Check the range of the mat.
    for x in range(i, i + mat):
        for y in range(j, j + mat):
            if park[x][y] != '-1':
                return False

    return True

def solution(mats, park):
    global X_RANGE, Y_RANGE
    X_RANGE = len(park)
    Y_RANGE = len(park[0])

    # Sort in descending order to inspect larger mats.
    for mat in sorted(mats, reverse=True):
        for i in range(X_RANGE):
            for j in range(Y_RANGE):
                if can_place(mat, park, i, j):
                    return mat

    return -1


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'mats': [5, 3, 2],
            'park': [
                ['A', 'A', '-1', 'B', 'B', 'B', 'B', '-1'],
                ['A', 'A', '-1', 'B', 'B', 'B', 'B', '-1'],
                ['-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1'],
                ['D', 'D', '-1', '-1', '-1', '-1', 'E', '-1'],
                ['D', 'D', '-1', '-1', '-1', '-1', '-1', 'F'],
                ['D', 'D', '-1', '-1', '-1', '-1', 'E', '-1']
            ],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('mats'), testcase.get('park'))
        print(answer)


if __name__ == '__main__':
    main()
