"""코딩테스트 고득점 Kit / Level 1. 최소 직사각형"""


# Solution of the problem.
def solution(sizes):
    width = 0
    height = 0

    for w, h in sizes:
        width = max(w, h) if max(w, h) > width else width
        height = min(w, h) if min(w, h) > height else height

    return width * height



# Test cases for solutions.
def testcases():
    testcase = [
        { 'sizes': [[60, 50], [30, 70], [60, 30], [80, 40]] },
        { 'sizes': [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]] },
        { 'sizes': [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('sizes'))
        print(answer)


if __name__ == '__main__':
    main()
