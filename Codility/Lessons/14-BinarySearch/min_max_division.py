# Solution of the problem.
def check_valid(value: int, numbers: list, max_block_size: int) -> bool:
    total = 0
    blocks = 1

    for num in numbers:
        # If can create a block.
        if num + total > value:
            total = num
            blocks += 1
            # If current block size is greater than maximum block size.
            if blocks > max_block_size:
                return False
        else:
            total += num

    return True

def solution(K, M, A):
    # Define minimum and maximum sum of blocks.
    min_block_sum = max(A)
    max_block_sum = sum(A)

    # If maximum block size is 1.
    if K == 1:
        return max_block_sum
    # If maximum block size is greater than or equal to list size.
    if K >= len(A):
        return min_block_sum

    answer = max_block_sum
    # Binary Search.
    while min_block_sum <= max_block_sum:
        mid = (min_block_sum + max_block_sum) // 2

        # Check if `mid` can be made in max blocks limit.
        if check_valid(mid, A, K):
            answer = mid
            max_block_sum = mid - 1
        else:
            min_block_sum = mid + 1

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'K': 3,
            'M': 5,
            'A': [2, 1, 5, 1, 2, 2, 2],
            'answer': 6,
        },
        {
            'K': 3,
            'M': 5,
            'A': [0, 0, 0, 0],
            'answer': 0,
        },
    ]
    return testcase


def main():
    for idx, testcase in enumerate(testcases()):
        my_answer = solution(testcase.get('K'), testcase.get('M'), testcase.get('A'))
        answer = testcase.get('answer')

        print(f'[Test case {idx + 1}]', end=' - ')
        if my_answer == answer:
            print(f'✅ (Correct) Answer: {answer}, My Answer: {my_answer}')
        else:
            print(f'❌ (Wrong) Answer: {answer}, My Answer: {my_answer}')


if __name__ == '__main__':
    main()
