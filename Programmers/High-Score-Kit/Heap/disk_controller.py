"""코딩테스트 고득점 Kit / Level 3. 디스크 컨트롤러"""


from heapq import heappush, heappop


# Solution of the problem.
def solution(jobs):
    # Create a list for waiting jobs. (Heap Queue)
    waitings = []

    job_length = len(jobs)
    # Add index to each job and rebuild the jobs.
    jobs = [(dur, req, idx) for idx, (req, dur) in enumerate(jobs)]
    # Sort jobs in descending order of request time.
    jobs.sort(key=lambda x: x[1], reverse=True)

    total = 0
    finished = 0
    current_time = 0
    while finished < job_length:
        # Push jobs into the heap queue if their request time has passed.
        while jobs and current_time >= jobs[-1][1]:
            # Priority: job(duration, request time, index).
            heappush(waitings, jobs.pop())

        # If the heap queue contains any waiting jobs.
        if waitings:
            job = heappop(waitings)
            # Increses current time and total response time.
            current_time += job[0]
            total += current_time - job[1]
            finished += 1
        # Jump to the next job's request time if no jobs are waiting.
        else:
            current_time = jobs[-1][1]

    answer = total // job_length

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        { 'jobs': [[0, 3], [1, 9], [2, 6]] },
        { 'jobs': [[0, 3], [1, 9], [3, 5]] },
        { 'jobs': [[0, 6], [2, 8], [3, 7], [7, 1], [11, 11], [19, 25], [30, 15], [32, 6], [40, 3]] },
        { 'jobs': [[0, 10], [4, 10], [5, 11], [15, 2]] },
        { 'jobs': [[0, 3], [8, 9], [5, 2]] },
        { 'jobs': [[0, 3], [0, 3], [1, 2]] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('jobs'))
        print(answer)


if __name__ == '__main__':
    main()
