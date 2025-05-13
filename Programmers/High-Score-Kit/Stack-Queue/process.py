"""코딩테스트 고득점 Kit / Level 2. 프로세스"""


from collections import deque


# Solution of the problem.
def solution(priorities, location):
    count = 0

    # Create a queue that stores indexes and priorities in pairs.
    processes = deque([(idx, priority) for idx, priority in enumerate(priorities)])

    while processes:
        idx, process = processes.popleft()

        # If the higher priority exists in the queue.
        if any(process < priority for _, priority in processes):
            processes.append((idx, process))
        else:
            count += 1
            if idx == location:
                break

    return count


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'priorities': [2, 1, 3, 2],
            'location': 2,
        },
        {
            'priorities': [1, 1, 9, 1, 1, 1],
            'location': 0,
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('priorities'), testcase.get('location'))
        print(answer)


if __name__ == '__main__':
    main()
