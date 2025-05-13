"""[PCCE 기출문제] 7번 / 버스"""


# Solution of the problem.
def func1(num):
    if 0 > num:
        return 0
    else:
        return num

def func2(num):
    if num > 0:
        return 0
    else:
        return num

def func3(station):
    num = 0
    for people in station:
        if people == "Off":
            num += 1
    return num

def func4(station):
    num = 0
    for people in station:
        if people == "On":
            num += 1
    return num

def solution(seat, passengers):
    num_passenger = 0
    for station in passengers:
        num_passenger += func4(station)
        num_passenger -= func3(station)
    answer = func1(seat - num_passenger)
    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'seat': 5,
            'passengers': [
                ['On', 'On', 'On'],
                ['Off', 'On', '-'],
                ['Off', '-', '-'],
            ],
        },
        {
            'seat': 10,
            'passengers': [
                ['On', 'On', 'On', 'On', 'On', 'On', 'On', 'On', '-', '-'],
                ['On', 'On', 'Off', 'Off', 'Off', 'On', 'On', '-', '-', '-'],
                ['On', 'On', 'On', 'Off', 'On', 'On', 'On', 'Off', 'Off', 'Off'],
                ['On', 'On', 'Off', '-', '-', '-', '-', '-', '-', '-'],
            ],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('seat'), testcase.get('passengers'))
        print(answer)


if __name__ == '__main__':
    main()
