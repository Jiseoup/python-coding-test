"""코딩테스트 고득점 Kit / Level 2. 카펫"""


# Solution of the problem.
def solution(brown, yellow):
    answer = []
    carpet = brown + yellow

    # Iterate through possible heights of the carpet. (minimum height = 3: brown >= 8, yellow >= 1)
    for height in range(3, int(carpet ** 0.5) + 1):
        # Skip if height is not a factor of the carpet size.
        if carpet % height != 0:
            continue
        width = carpet // height

        # Check if the current width and height satisfy the conditions. (subtract 2 to account for the brown border)
        if (width - 2) * (height - 2) == yellow:
            answer.append(max(width, height))
            answer.append(min(width, height))
            break

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'brown': 10,
            'yellow': 2,
        },
        {
            'brown': 8,
            'yellow': 1,
        },
        {
            'brown': 24,
            'yellow': 24,
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('brown'), testcase.get('yellow'))
        print(answer)


if __name__ == '__main__':
    main()
