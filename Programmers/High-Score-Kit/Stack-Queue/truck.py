"""코딩테스트 고득점 Kit / Level 2. 다리를 지나는 트럭"""


from collections import deque


# Solution of the problem.
def solution(bridge_length, weight, truck_weights):
    seconds = 0

    # Create queues for trucks and the bridge.
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)

    # Loop until waiting trucks are empty.
    while trucks:
        weight += bridge.popleft()

        # If a truck can get on the bridge.
        if weight >= trucks[0]:
            truck = trucks.popleft()
            bridge.append(truck)
            weight -= truck
        else:
            bridge.append(0)

        seconds += 1

    # Add `bridge_length` seconds for last truck.
    seconds += bridge_length

    return seconds


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'bridge_length': 2,
            'weight': 10,
            'truck_weights': [7, 4, 5, 6],
        },
        {
            'bridge_length': 100,
            'weight': 100,
            'truck_weights': [10],
        },
        {
            'bridge_length': 100,
            'weight': 100,
            'truck_weights': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        },
        {
            'bridge_length': 2,
            'weight': 10,
            'truck_weights': [3, 3, 3, 3],
        },
        {
            'bridge_length': 100,
            'weight': 100,
            'truck_weights': [100, 100, 90, 10],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('bridge_length'), testcase.get('weight'), testcase.get('truck_weights'))
        print(answer)


if __name__ == '__main__':
    main()
