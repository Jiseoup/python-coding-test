# Solution of the problem.
def solution(A):
    answer = []
    length = len(A)

    # Initialize dict with each number counts.
    num_counts = dict()
    for num in A:
        num_counts[num] = num_counts.get(num, 0) + 1

    # Define empty dict to store numbers that have been already calculated.
    calculated = dict()

    for num in A:
        # If the number is already calculated, just append stored counts.
        if num in calculated:
            answer.append(calculated.get(num))
            continue

        total = length
        sq_root = int(num ** 0.5)
        for i in range(1, sq_root + 1):
            # Substract divisible counts from total.
            if num % i == 0:
                if i == num // i:
                    total -= num_counts.get(i, 0)
                else:
                    total -= num_counts.get(i, 0) + num_counts.get(num // i, 0)
        answer.append(total)
        calculated[num] = total

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [3, 1, 2, 3, 6],
            'answer': [2, 4, 3, 2, 0],
        },
        {
            'A': [2],
            'answer': [0],
        },
        {
            'A': [1, 1],
            'answer': [0, 0],
        },
        {
            'A': [3, 4, 3, 4],
            'answer': [2, 2, 2, 2],
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('A'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
