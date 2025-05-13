"""코딩테스트 고득점 Kit / Level 1. K번째수"""


# Solution of the problem.
def solution(array, commands):
    answer = []

    for i, j, k in commands:
        filtered_array = sorted(array[i-1:j])
        answer.append(filtered_array[k - 1])

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'array': [1, 5, 2, 6, 3, 7, 4],
            'commands': [[2, 5, 3], [4, 4, 1], [1, 7, 3]],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('array'), testcase.get('commands'))
        print(answer)


if __name__ == '__main__':
    main()
