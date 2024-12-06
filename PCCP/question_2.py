# NOTE: Not Solved.

diffs = [1, 99999, 100000, 99995]
times = [9999, 9001, 9999, 9001]
limit = 3456789012

def solution(diffs, times, limit):
    level = 0
    solved = False

    # Iterate the function until the puzzle is solved within the time limit.
    while not solved:
        solved = True
        total_limit = limit

        for idx, diff in enumerate(diffs):
            time_cur = times[idx]
            time_prev = times[idx - 1] if idx != 0 else None

            # Solving the current level's puzzle.
            if diff <= level:
                total_limit -= time_cur
            else:
                wrong = diff - level
                if time_prev:
                    total_limit -= ((time_cur + time_prev) * wrong) + time_cur
                else:
                    total_limit -= (time_cur * wrong) + time_cur

            # If the time limit ends.
            if total_limit < 0:
                level += 1
                solved = False
                break

    return level

print(solution(diffs, times, limit))
