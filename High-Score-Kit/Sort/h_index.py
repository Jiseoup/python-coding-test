"""코딩테스트 고득점 Kit / Level 2. H-Index"""


# Solution of the problem.
def solution(citations):
    """ My First Solution """
    set_hindex = set()
    max_hindex = len(citations)

    # Sort in descending order to check bigger number first.
    citations.sort(reverse=True)

    # Check hindex in descending order: reversed(range(max_hindex + 1))
    for hindex in range(max_hindex, -1, -1):
        count = 0

        # Compare citations with hindex.
        for citation in citations:
            if citation < hindex:
                break
            count += 1

        # If the number of citations is greater than or equal to hindex.
        if count >= hindex:
            set_hindex.add(hindex)

    return max(set_hindex)

    # """ My Second Solution (Better than First Solution) """
    # # Sort in descending order to check bigger number first.
    # citations.sort(reverse=True)

    # h_index = 0
    # for c in citations:
    #     if c > h_index:
    #         h_index += 1

    # return h_index


# Test cases for solutions.
def testcases():
    testcase = [
        { 'citations': [3, 0, 6, 1, 5] },
        { 'citations': [0, 0, 0, 0, 6, 5] },
        { 'citations': [5, 5, 5, 5, 5] },
        { 'citations': [0, 0, 0, 0] },
        { 'citations': [1, 2, 3, 4] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('citations'))
        print(answer)


if __name__ == '__main__':
    main()
