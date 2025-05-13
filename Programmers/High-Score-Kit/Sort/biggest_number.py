"""코딩테스트 고득점 Kit / Level 2. 가장 큰 수"""


# Solution of the problem.
def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x*3, reverse=True)

    answer = ''.join(str_numbers)

    return str(int(answer))


# Test cases for solutions.
def testcases():
    testcase = [
        { 'numbers': [6, 10, 2] },
        { 'numbers': [3, 30, 34, 5, 9] },
        { 'numbers': [0, 0, 0, 0] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('numbers'))
        print(answer)


if __name__ == '__main__':
    main()
