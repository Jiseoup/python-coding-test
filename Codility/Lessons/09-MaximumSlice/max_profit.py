# Solution of the problem.
import sys

def solution(A):
    max_profit = 0
    min_price = sys.maxsize

    for price in A:
        # Set the minimum price.
        min_price = min(min_price, price)

        # If profit is positive number, set the maximum profit.
        profit = price - min_price
        if profit > 0:
            max_profit = max(max_profit, profit)

    return max_profit


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'A': [23171, 21011, 21123, 21366, 21013, 21367],
            'answer': 356,
        },
        {
            'A': [0, 0, 0, 0],
            'answer': 0,
        },
        {
            'A': [5, 4, 3, 2, 1],
            'answer': 0,
        },
        {
            'A': [],
            'answer': 0,
        },
        {
            'A': [5, 4, 1, 2, 3, 0],
            'answer': 2,
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('A'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
