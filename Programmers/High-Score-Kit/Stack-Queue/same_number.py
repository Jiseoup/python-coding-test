"""코딩테스트 고득점 Kit / Level 1. 같은 숫자는 싫어"""


# Solution of the problem.
def solution(arr):
    stack = []

    for a in arr:
        if not stack or stack[-1] != a:
            stack.append(a)

    return stack


# Test cases for solutions.
def testcases():
    testcase = [
        { 'arr': [1,1,3,3,0,1,1] },
        { 'arr': [4,4,4,3,3] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('arr'))
        print(answer)


if __name__ == '__main__':
    main()
