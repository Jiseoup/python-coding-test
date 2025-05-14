# Solution of the problem.
def solution(H):
    walls = []
    count = 0

    for height in H:
        # Loop while the height of current wall is lower than the previous wall.
        while walls and walls[-1] > height:
            walls.pop()

        # Build a stone wall.
        if not walls or walls[-1] < height:
            walls.append(height)
            count += 1

    return count


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'H': [8, 8, 5, 7, 9, 8, 7, 4, 8],
            'answer': 7,
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('H'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
