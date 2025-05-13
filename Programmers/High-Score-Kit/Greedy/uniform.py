"""코딩테스트 고득점 Kit / Level 1. 체육복"""


# Solution of the problem.
def solution(n, lost, reserve):
    answer = 0
    uniforms = {}

    # Count uniforms per each student.
    for student in range(1, n + 1):
        count = 1
        # If student lost uniform, substract uniform count.
        if student in lost:
            count -= 1
        # If student has reserve uniform, add uniform count.
        if student in reserve:
            count += 1
        uniforms[student] = count

    for student in range(1, n + 1):
        # If student has uniforms.
        if uniforms.get(student) >= 1:
            answer += 1
            continue

        # Store previous and next student in variables.
        prev_student = student - 1
        next_student = student + 1

        # Check if previous or next student has reserve uniforms.
        if prev_student >= 1 and uniforms.get(prev_student, 0) > 1:
            uniforms[prev_student] -= 1
            answer += 1
        elif next_student <= n and uniforms.get(next_student, 0) > 1:
            uniforms[next_student] -= 1
            answer += 1

    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'n': 5,
            'lost': [2, 4],
            'reserve': [1, 3, 5],
        },
        {
            'n': 5,
            'lost': [2, 4],
            'reserve': [3],
        },
        {
            'n': 3,
            'lost': [3],
            'reserve': [1],
        },
        {
            'n': 4,
            'lost': [1, 2],
            'reserve': [1, 3],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('n'), testcase.get('lost'), testcase.get('reserve'))
        print(answer)


if __name__ == '__main__':
    main()
