# Solution of the problem.
from math import gcd

def solution(N, M):
    """Best Solution: Using GCD(Greatest Common Divisor)"""
    return N // gcd(N, M)

# def solution(N, M):
#     """My Solution: Timeout Error Occured"""
#     count = 0
#     chocolate = 0
#     eaten = set()

#     # Iterate circular.
#     while chocolate not in eaten:
#         eaten.add(chocolate)
#         count += 1
#         # Prepare next chocolate.
#         chocolate = (chocolate + M) % N

#     return count


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'N': 10,
            'M': 4,
            'answer': 5,
        },
        {
            'N': 30,
            'M': 3,
            'answer': 10,
        },
        {
            'N': 31,
            'M': 3,
            'answer': 31,
        },
        {
            'N': 5,
            'M': 1,
            'answer': 5,
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('N'), testcase.get('M'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
