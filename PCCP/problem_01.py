"""PCCP 기출문제 / Level 1. 동영상 재생기"""


# Solution of the problem.
# """ My First Solution : Using datetime modules """
# from datetime import datetime, timedelta

# def skip_opening(start, end, pos):
#     return end if start <= pos <= end else pos

# def solution(video_len, pos, op_start, op_end, commands):
#     # Convert to datetime object.
#     t_video_len = datetime.strptime(video_len, '%M:%S')
#     t_pos = datetime.strptime(pos, '%M:%S')
#     t_op_start = datetime.strptime(op_start, '%M:%S')
#     t_op_end = datetime.strptime(op_end, '%M:%S')

#     for command in commands:
#         # Skip opening.
#         t_pos = skip_opening(t_op_start, t_op_end, t_pos)

#         # Perform commands.
#         if command == 'prev':
#             t_pos = max(t_pos - timedelta(seconds=10), datetime(1900, 1, 1, 0, 0, 0))
#         elif command == 'next':
#             t_pos = min(t_pos + timedelta(seconds=10), t_video_len)
#         else:
#             raise Exception("Unknown Commands.")

#     # Skip opening at the end of function.
#     t_pos = skip_opening(t_op_start, t_op_end, t_pos)

#     return t_pos.strftime('%M:%S')

""" My Second Solution : Not using modules """
def to_seconds(time: str) -> int:
    minutes, seconds = map(int, time.split(':'))
    return (minutes * 60) + seconds

def to_str_time(time: int) -> str:
    minutes = str(time // 60).zfill(2)
    seconds = str(time % 60).zfill(2)
    return f'{minutes}:{seconds}'

def skip_opening(pos: int, start: int, end: int) -> int:
    if start <= pos <= end:
        return end
    return pos

def solution(video_len, pos, op_start, op_end, commands):
    # Convert type from `str` to `int`.
    s_video_len = to_seconds(video_len)
    s_pos = to_seconds(pos)
    s_op_start = to_seconds(op_start)
    s_op_end = to_seconds(op_end)

    for command in commands:
        # Check if skip opening.
        s_pos = skip_opening(s_pos, s_op_start, s_op_end)

        # Update the current position based on the given command.
        if command == 'prev':
            s_pos = max(s_pos - 10, 0)
        elif command == 'next':
            s_pos = min(s_pos + 10, s_video_len)
        else:
            raise Exception('Unknown Commands.')

    # Check if skip opening at the end of the function.
    s_pos = skip_opening(s_pos, s_op_start, s_op_end)

    answer = to_str_time(s_pos)
    return answer


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'video_len': '34:33',
            'pos': '13:00',
            'op_start': '00:55',
            'op_end': '02:55',
            'commands': ['next', 'prev'],
        },
        {
            'video_len': '10:55',
            'pos': '00:05',
            'op_start': '00:15',
            'op_end': '06:55',
            'commands': ['prev', 'next', 'next'],
        },
        {
            'video_len': '07:22',
            'pos': '04:05',
            'op_start': '00:15',
            'op_end': '04:07',
            'commands': ['next'],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(
            testcase.get('video_len'), testcase.get('pos'),
            testcase.get('op_start'), testcase.get('op_end'), testcase.get('commands')
        )
        print(answer)


if __name__ == '__main__':
    main()
