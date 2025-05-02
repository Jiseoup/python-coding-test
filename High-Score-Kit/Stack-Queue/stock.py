"""코딩테스트 고득점 Kit / Level 2. 주식 가격"""


from collections import deque


# Solution of the problem.
def solution(prices):
    # """ Solution 1: Using Queue """
    # answer = []

    # # Make prices as a queue.
    # prices = deque(prices)

    # # Loop until prices queue is empty.
    # while prices:
    #     stock = prices.popleft()
    #     seconds = 0

    #     # Check if there is a stock with a lower price.
    #     for price in prices:
    #         seconds += 1
    #         if stock > price:
    #             break

    #     answer.append(seconds)

    # return answer

    """ Solution 2: Using Stack """
    length = len(prices)

    # Store the maximum seconds for each stock.
    answer = [seconds for seconds in range(length - 1, -1, -1)]

    stack = []
    for idx in range(length):
        # While Loop: Execute when the stock price drops.
        while stack and prices[stack[-1]] > prices[idx]:
            prev_idx = stack.pop()
            answer[prev_idx] = idx - prev_idx
        stack.append(idx)

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        { 'prices': [1, 2, 3, 2, 3] },
        { 'prices': [1, 2, 3, 2, 3, 1] },
        { 'prices': [5, 6, 4, 1] },
        { 'prices': [3, 3, 3, 2, 1] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('prices'))
        print(answer)


if __name__ == '__main__':
    main()
