"""PCCP 기출문제 / Level 1. 붕대 감기"""


# Solution of the problem.
from collections import deque

def simulate(bandage, health, attacks):
    seconds = 0
    max_health = health
    t, x, y = bandage[0], bandage[1], bandage[2]

    # Loop until all attacks are done.
    while attacks:
        recovery_count = 0
        time, damage = attacks.popleft()

        # Recover health until the next attack time.
        while seconds != time:
            health += x
            seconds += 1
            recovery_count += 1

            # When healed continuously for t seconds.
            if recovery_count % t == 0:
                health += y

            # If health exceeds the maximum.
            if health > max_health:
                health = max_health

        # Take damage to the player.
        health -= damage
        seconds += 1

        # If the player is dead.
        if health <= 0:
            return -1

    return health

def solution(bandage, health, attacks):
    # Make attacks list into queue.
    attacks = deque(attacks)

    answer = simulate(bandage, health, attacks)

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'bandage': [5, 1, 5],
            'health': 30,
            'attacks': [[2, 10], [9, 15], [10, 5], [11, 5]],
        },
        {
            'bandage': [3, 2, 7],
            'health': 20,
            'attacks': [[1, 15], [5, 16], [8, 6]],
        },
        {
            'bandage': [4, 2, 7],
            'health': 20,
            'attacks': [[1, 15], [5, 16], [8, 6]],
        },
        {
            'bandage': [1, 1, 1],
            'health': 5,
            'attacks': [[1, 2], [3, 2]],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('bandage'), testcase.get('health'), testcase.get('attacks'))
        print(answer)


if __name__ == '__main__':
    main()
