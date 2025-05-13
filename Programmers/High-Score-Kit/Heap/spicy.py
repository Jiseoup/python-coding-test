"""코딩테스트 고득점 Kit / Level 2. 더 맵게"""


from heapq import heapify, heappush, heappop


# Solution of the problem.
def solution(scoville, K):
    answer = 0
    
    # Make scoville list to heap.
    heapify(scoville)

    # Loop while minimum scoville is lower than K.
    while scoville[0] < K:
        # If cannot mix more foods.
        if len(scoville) < 2:
            answer = -1
            break

        # Mix foods and create new food which has a new scoville.
        new_scoville = heappop(scoville) + (heappop(scoville) * 2)
        heappush(scoville, new_scoville)
        answer += 1

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'scoville': [1, 2, 3, 9, 10, 12],
            'K': 7,
        },
        {
            'scoville': [1, 2, 3, 4, 5],
            'K': 15,
        },
        {
            'scoville': [0, 0, 0],
            'K': 0,
        },
        {
            'scoville': [0, 0, 0],
            'K': 1,
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('scoville'), testcase.get('K'))
        print(answer)


if __name__ == '__main__':
    main()
