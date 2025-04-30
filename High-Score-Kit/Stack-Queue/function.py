"""코딩테스트 고득점 Kit / Level 2. 기능 개발"""


from collections import deque


# Solution of the problem.
def solution(progresses, speeds):
    """ My Solution : Using deque() """
    answer = []

    # Make progresses and speeds into deque.
    queue = deque(zip(progresses, speeds))

    # Loop until queue is empty.
    while (queue):
        # Add speed to the progress.
        queue = deque([(progress + speed, speed) for progress, speed in queue])

        count = 0
        while (queue and queue[0][0] >= 100):
            queue.popleft()
            count += 1

        if count > 0:
            answer.append(count)

    return answer

    # """ My Solution : Using list() """
    # answer = []

    # # Loop until list is empty.
    # while (progresses and speeds):
    #     # Add speed to the progress.
    #     for i in range(len(progresses)):
    #         progresses[i] += speeds[i]

    #     count = 0
    #     while (progresses and progresses[0] >= 100):
    #         progresses.pop(0)
    #         speeds.pop(0)
    #         count += 1

    #     if count > 0:
    #         answer.append(count)

    # return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'progresses': [93, 30, 55],
            'speeds': [1, 30, 5],
        },
        {
            'progresses': [95, 90, 99, 99, 80, 99],
            'speeds': [1, 1, 1, 1, 1, 1],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('progresses'), testcase.get('speeds'))
        print(answer)


if __name__ == '__main__':
    main()
