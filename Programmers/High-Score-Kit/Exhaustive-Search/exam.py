"""코딩테스트 고득점 Kit / Level 1. 모의고사"""


# Solution of the problem.
def solution(answers):
    """ My First Solution """
    # Define students and their answer patterns.
    students = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }

    # Compare answers and count their scores.
    for _id, student in students.items():
        count = 0
        for idx, answer in enumerate(answers):
            student_answer = student[idx % len(student)]
            if answer == student_answer:
                count += 1
        students[_id] = count

    answer = []
    max_score = max(students.values())
    # If student's score equals to max score, append student index to the list.
    for _id, score in students.items():
        if score == max_score:
            answer.append(_id)

    return answer

    # """ My Second Solution """
    # # Initialize scores and define student patterns.
    # scores = [0, 0, 0]
    # student_1 = [1, 2, 3, 4, 5]
    # student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # # Compare answers and student patterns.
    # for idx, answer in enumerate(answers):
    #     if answer == student_1[idx % len(student_1)]:
    #         scores[0] += 1
    #     if answer == student_2[idx % len(student_2)]:
    #         scores[1] += 1
    #     if answer == student_3[idx % len(student_3)]:
    #         scores[2] += 1

    # answer = []
    # max_score = max(scores)
    # # If student's score equals to max score, append student index to the list.
    # for idx, score in enumerate(scores):
    #     if score == max_score:
    #         answer.append(idx + 1)

    # return answer


# Test cases for solutions.
def testcases():
    testcase = [
        { 'answers': [1, 2, 3, 4, 5] },
        { 'answers': [1, 3, 2, 4, 2] },
        { 'answers': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('answers'))
        print(answer)


if __name__ == '__main__':
    main()
