"""코딩테스트 고득점 Kit / Level 2. 올바른 괄호"""


# Solution of the problem.
def solution(s):
    stack = []

    for parentheses in s:
        stack.append(parentheses)

        # If stack length lower than 2, skip it.
        if len(stack) < 2:
            continue

        # Compare the top two elements of the stack.
        if stack[-1] == ')' and stack[-2] == '(':
            stack.pop()
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


# Test cases for solutions.
def testcases():
    testcase = [
        { 's': '()()' },
        { 's': '(())()' },
        { 's': ')()(' },
        { 's': '(()(' },
        { 's': '())(()' },
        { 's': '()(())' },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('s'))
        print(answer)


if __name__ == '__main__':
    main()
