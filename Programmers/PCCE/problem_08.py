"""[PCCE 기출문제] 8번 / 닉네임 규칙"""


# Solution of the problem.
def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    while len(answer) < 4:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        { 'nickname': 'WORLDworld' },
        { 'nickname': 'GO' },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('nickname'))
        print(answer)


if __name__ == '__main__':
    main()
