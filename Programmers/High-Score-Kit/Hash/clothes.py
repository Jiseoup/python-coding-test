"""코딩테스트 고득점 Kit / Level 2. 의상"""


# Solution of the problem.
def solution(clothes):
    # Store clothes name group by its type.
    clothes_dict = {}
    for c_name, c_type in clothes:
        if c_type not in clothes_dict:
            clothes_dict[c_type] = set()
        clothes_dict[c_type].add(c_name)

    # Sum of products of all subsets: (N+1)(M+1)...
    answer = 1
    for value in clothes_dict.values():
        answer *= (len(value) + 1)

    # Return `answer -1` to exclude empty set.
    return answer - 1


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'clothes': [
                ['yellow_hat', 'headgear'],
                ['blue_sunglasses', 'eyewear'],
                ['green_turban', 'headgear']
            ]
        },
        {
            'clothes': [
                ['crow_mask', 'face'],
                ['blue_sunglasses', 'face'],
                ['smoky_makeup', 'face']
            ]
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('clothes'))
        print(answer)


if __name__ == '__main__':
    main()
