"""코딩테스트 고득점 Kit / Level 2. 전화번호 목록"""


# Solution of the problem.
def solution(phone_book):
    """ My Solution """
    # Sort in ascending order to make the string of prefix relationships adjacent.
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True

    # """ Other Solution - Using Hash """
    # # Initialize the hash map.
    # hash_map = {}
    # for phone_number in phone_book:
    #     hash_map[phone_number] = 0

    # for phone_number in phone_book:
    #     temp = ''
    #     for number in phone_number:
    #         temp += number
    #         if temp in hash_map and temp != phone_number:
    #             return False

    # return True


# Test cases for solutions.
def testcases():
    testcase = [
        { 'phone_book': ['119', '97674223', '1195524421'] },
        { 'phone_book': ['123','456','789'] },
        { 'phone_book': ['12','123','1235','567','88'] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('phone_book'))
        print(answer)


if __name__ == '__main__':
    main()
