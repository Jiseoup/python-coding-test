"""코딩테스트 고득점 Kit / Level 2. 소수 찾기"""


from itertools import permutations


# Solution of the problem.
def is_prime(number: int) -> bool:
    # If the number lower than 2, return False. (0, 1)
    if number < 2:
        return False

    # Check if the number is prime: from 2 to sqrt(number).
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

def solution(numbers):
    # Define answer as set() to avoid duplication.
    answer = set()

    # Combine numbers to create permutations for all cases.
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            number = int(''.join(perm))

            # Check if the number is prime.
            if is_prime(number):
                answer.add(number)

    return len(answer)



# Test cases for solutions.
def testcases():
    testcase = [
        { 'numbers': '17' },
        { 'numbers': '011' },
        { 'numbers': '000' },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('numbers'))
        print(answer)


if __name__ == '__main__':
    main()
