from datetime import datetime, timedelta

def skip_opening(start, end, pos):
    return end if start <= pos <= end else pos

def solution(video_len, pos, op_start, op_end, commands):
    # Convert to datetime object.
    t_video_len = datetime.strptime(video_len, '%M:%S')
    t_pos = datetime.strptime(pos, '%M:%S')
    t_op_start = datetime.strptime(op_start, '%M:%S')
    t_op_end = datetime.strptime(op_end, '%M:%S')

    for command in commands:
        # Skip opening.
        t_pos = skip_opening(t_op_start, t_op_end, t_pos)

        # Perform commands.
        if command == 'prev':
            t_pos = max(t_pos - timedelta(seconds=10), datetime(1900, 1, 1, 0, 0, 0))
        elif command == 'next':
            t_pos = min(t_pos + timedelta(seconds=10), t_video_len)
        else:
            raise Exception("Unknown Commands")

    # Skip opening at the end of function.
    t_pos = skip_opening(t_op_start, t_op_end, t_pos)

    return t_pos.strftime('%M:%S')
