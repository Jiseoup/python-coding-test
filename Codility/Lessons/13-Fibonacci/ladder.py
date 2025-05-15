# Solution of the problem.
def solution(A, B):
    answer = []

    # Define the maximum possible rung and modulo values.
    max_rung = max(A)
    max_modulo = 2 ** max(B)

    # Create fibonacci numbers dict.
    fibonacci = dict()
    for i in range(1, max_rung + 1):
        # Apply modulo with max_modulo to minimize fibonacci number.
        fibonacci[i] = (fibonacci.get(i - 1, 0) + fibonacci.get(i - 2, 1)) % max_modulo

    # Define ladders with tuple(rungs, 2^n).
    ladders = list(zip(A, [2 ** n for n in B]))

    for rung, modulo in ladders:
        answer.append(fibonacci.get(rung) % modulo)

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [4, 4, 5, 5, 1],
            'B': [3, 2, 4, 3, 1],
            'answer': [5, 1, 8, 0, 1],
        },
        {
            'A': [4, 4, 5, 5, 1],
            'B': [1, 1, 1, 1, 1],
            'answer': [1, 1, 0, 0, 1],
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('A'), testcase.get('B'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
