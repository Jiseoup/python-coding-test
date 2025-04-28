"""[PCCE 기출문제] 9번 / 지폐 접기"""


# Solution of the problem.
def solution(wallet, bill):
    answer = 0

    # Define wallet width/height.
    wallet_width = wallet[0]
    wallet_height = wallet[1]

    # Define bill width/height.
    bill_width = bill[0]
    bill_height = bill[1]

    # Determine how many times to fold. 
    while True:
        if (
            (bill_width <= wallet_width and bill_height <= wallet_height)
            or (bill_width <= wallet_height and bill_height <= wallet_width)
        ):
            break

        if bill_width >= bill_height:
            bill_width //= 2
        else:
            bill_height //= 2

        answer += 1

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'wallet': [30, 15],
            'bill': [26, 17],
        },
        {
            'wallet': [50, 50],
            'bill': [100, 241],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('wallet'), testcase.get('bill'))
        print(answer)


if __name__ == '__main__':
    main()
