"""[PCCE 기출문제] 6번 / 물 부족"""


# Solution of the problem.
def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage += usage * change[i]/100
        total_usage += usage
        if total_usage > storage:
            return i

    return -1


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'storage': 5141,
            'usage': 500,
            'change': [10, -10, 10, -10, 10, -10, 10, -10, 10, -10],
        },
        {
            'storage': 1000,
            'usage': 2000,
            'change': [-10, 25, -33],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(
            testcase.get('storage'), testcase.get('usage'), testcase.get('change')
        )
        print(answer)


if __name__ == '__main__':
    main()
