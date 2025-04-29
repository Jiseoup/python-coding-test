"""코딩테스트 고득점 Kit / Level 1. 완주하지 못한 선수"""


from collections import Counter


# Solution of the problem.
def solution(participant, completion):
    """ My Solution """
    participant_dict = {}

    for p in participant:
        participant_dict[p] = participant_dict.get(p, 0) + 1

    for c in completion:
        participant_dict[c] = participant_dict.get(c) - 1

    for key, value in participant_dict.items():
        if value > 0:
            return key

    # """ Other Solution 1 - Using collections.Counter """
    # answer = Counter(participant) - Counter(completion)
    # return list(answer.keys())[0]

    # """ Other Solution 2 - Using hash() """
    # temp_hash = 0
    # participant_dict = {}

    # for p in participant:
    #     participant_dict[hash(p)] = p
    #     temp_hash += hash(p)

    # for c in completion:
    #     temp_hash -= hash(c)

    # answer = participant_dict.get(temp_hash)

    # return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'participant': ['leo', 'kiki', 'eden'],
            'completion': ['eden', 'kiki'],
        },
        {
            'participant': ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
            'completion': ['josipa', 'filipa', 'marina', 'nikola'],
        },
        {
            'participant': ['mislav', 'stanko', 'mislav', 'ana'],
            'completion': ['stanko', 'ana', 'mislav'],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('participant'), testcase.get('completion'))
        print(answer)


if __name__ == '__main__':
    main()
