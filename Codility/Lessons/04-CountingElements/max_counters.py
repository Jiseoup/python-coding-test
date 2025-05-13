# Solution of the problem.
def solution(N, A):
    # Initialize the counters.
    counters = [0] * N

    # Variables that defines current max value and latest max counter value.
    curr_max = 0
    max_counter = 0

    for num in A:
        index = num - 1

        # If index == N, set `max counter` as current max value of the list.
        if index == N:
            max_counter = curr_max
        else:
            # If max counter is not applied, apply the max counter value. (Lazy Update)
            if counters[index] < max_counter:
                counters[index] = max_counter
            # Performs `increase` operation and set the current max value of the list.
            counters[index] += 1
            curr_max = max(curr_max, counters[index])

    # Apply max counter to the remain elements. (Lazy Update)
    for i in range(N):
        if counters[i] < max_counter:
            counters[i] = max_counter

    return counters


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'N': 5,
            'A': [3, 4, 4, 6, 1, 4, 4],
            'answer': [3, 2, 2, 4, 2],
        },
        {
            'N': 3,
            'A': [1, 2, 3, 1, 2, 3],
            'answer': [2, 2, 2],
        },
        {
            'N': 4,
            'A': [5, 5, 5],
            'answer': [0, 0, 0, 0],
        },
        {
            'N': 3,
            'A': [4, 1, 2],
            'answer': [1, 1, 0],
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('N'), testcase.get('A'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
