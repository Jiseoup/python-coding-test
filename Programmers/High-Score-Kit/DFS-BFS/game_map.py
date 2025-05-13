"""코딩테스트 고득점 Kit / Level 2. 게임 맵 최단거리"""


# Solution of the problem.
""" Solution 1 : Using BFS (Best method) """
from collections import deque

def solution(maps):
    MAX_X_POS = len(maps)
    MAX_Y_POS = len(maps[0])

    # Define default position and count. (x pos, y pos, count)
    position = deque([(0, 0, 1)])

    # Create a visited list of the same size as maps list.
    visited = [[False] * MAX_Y_POS for _ in range(MAX_X_POS)]
    visited[0][0] = True

    while position:
        x, y, count = position.popleft()

        # If reached the opponent team's zone.
        if x == MAX_X_POS - 1 and y == MAX_Y_POS - 1:
            return count

        # Move up, down, left, right.
        for moving_x, moving_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x = x + moving_x
            new_y = y + moving_y

            # If index out of range, skip it.
            if new_x < 0 or new_x >= MAX_X_POS or new_y < 0 or new_y >= MAX_Y_POS:
                continue

            # If the new position is movable and not visited yet.
            if maps[new_x][new_y] == 1 and visited[new_x][new_y] is False:
                position.append((new_x, new_y, count + 1))
                visited[new_x][new_y] = True

    return -1

# """ Solution 2 : Using DFS (Cannot pass efficiency test) """
# from typing import List

# # Global variables for store map size.
# MAX_X_POS = 0
# MAX_Y_POS = 0

# # Global variable for store moving counts.
# movings = []

# def move(
#     x: int,
#     y: int,
#     moving: int,
#     maps: List[List[int]],
#     visited: List[List[bool]]
# ) -> None:
#     # If index out of range.
#     if x < 0 or x >= MAX_X_POS or y < 0 or y >= MAX_Y_POS:
#         return None

#     # If the position is not movable or has already been visited.
#     if maps[x][y] == 0 or visited[x][y]:
#         return None

#     # If reached the opponent team's zone.
#     if x == MAX_X_POS - 1 and y == MAX_Y_POS - 1:
#         # Append moving counts to the list.
#         global movings
#         movings.append(moving)
#         return None

#     # Set the current position as visited.
#     visited[x][y] = True

#     # Move up, down, left, right.
#     move(x - 1, y, moving + 1, maps, visited)
#     move(x + 1, y, moving + 1, maps, visited)
#     move(x, y - 1, moving + 1, maps, visited)
#     move(x, y + 1, moving + 1, maps, visited)

#     # After all movings, set the current position as not visited for backtracking.
#     visited[x][y] = False

#     return None

# def solution(maps):
#     global MAX_X_POS, MAX_Y_POS, movings

#     # Set max x, y positions.
#     MAX_X_POS = len(maps)
#     MAX_Y_POS = len(maps[0])

#     # Create a visited list of the same size as maps list.
#     visited = [[False] * MAX_Y_POS for _ in range(MAX_X_POS)]

#     # Start moving from the starting position (0, 0).
#     move(0, 0, 1, maps, visited)

#     return min(movings) if movings else -1


# Test cases for solutions.
def testcases():
    testcase = [
        { 'maps': [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]] },
        { 'maps': [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]] },
        { 'maps': [[1, 1]] },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('maps'))
        print(answer)


if __name__ == '__main__':
    main()
