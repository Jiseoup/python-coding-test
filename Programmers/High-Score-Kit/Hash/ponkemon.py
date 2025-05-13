"""코딩테스트 고득점 Kit / Level 1. 폰켓몬"""


# Solution of the problem.
def solution(nums):
    max_select = len(nums) // 2
    max_species = len(set(nums))

    return min(max_select, max_species)


# Test cases for solutions.
def testcases():
    testcase = [
        { 'nums': [3,1,2,3] },
        { 'nums': [3,3,3,2,2,4] },
        { 'nums': [3,3,3,2,2,2] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('nums'))
        print(answer)


if __name__ == '__main__':
    main()
