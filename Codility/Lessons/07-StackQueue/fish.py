# Solution of the problem.
from collections import deque

def solution(A, B):
    fishes = deque(zip(A, B))
    alive = len(fishes)

    # Define a empty list to stack downstream fishes.
    downstream = []

    while fishes:
        # Popleft current fish's size and directions from the queue.
        fish_size, fish_dir = fishes.popleft()

        # If the fish flows downstream, stack it.
        if fish_dir == 1:
            downstream.append((fish_size, fish_dir))
            continue

        # Loop while the current fish(upstream) is bigger than downstream fish.
        while downstream and fish_size > downstream[-1][0]:
            # Current fish(upstream) eats downstream fishes.
            downstream.pop()
            alive -= 1

        # If downstream fish exists, this means the current fish(upstream) is dead.
        if downstream:
            alive -= 1

    return alive


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [4, 3, 2, 1, 5],
            'B': [0, 1, 0, 0, 0],
            'answer': 2,
        },
        {
            'A': [4, 3, 2, 1, 5],
            'B': [1, 1, 0, 0, 0],
            'answer': 1,
        },
        {
            'A': [6, 4, 3, 2, 1],
            'B': [1, 1, 1, 0, 0],
            'answer': 3,
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
