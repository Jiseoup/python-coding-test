"""[PCCE 기출문제] 5번 / 심폐소생술"""


# Solution of the problem.
def solution(cpr):
    answer = []
    basic_order = ['check', 'call', 'pressure', 'respiration', 'repeat']
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i + 1)
    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        { 'cpr': ['call', 'respiration', 'repeat', 'check', 'pressure'] },
        { 'cpr': ['respiration', 'repeat', 'check', 'pressure', 'call'] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('cpr'))
        print(answer)


if __name__ == '__main__':
    main()
