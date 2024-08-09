# Water falls on a 2D grid evenly
# given a 2D map of elevation return a 2D grid
# indicator how many units of water has pooled in each cell

# Water moves to the adjacent cell with the steepest elevation
# tie breaks in any way (there's a few options for tie breaks leave up to interviewer to decide)

# Example
test_cases = [
    ([[2, 5, 1]], [[1, 0, 2]]),
    ([[1, 5, 2]], [[2, 0, 1]]),
    (
        [
            [9, 8, 4, 0],
            [4, 8, 5, 2],
            [2, 3, 8, 4],
            [1, 2, 5, 10]
        ],
        [
            [0, 0, 0, 7],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [9, 0, 0, 0],
        ]

    )
]


def sol(input):
    n, m = len(input), len(input[0])
    ans = [[1 for _ in range(m)] for _ in range(n)]
    visited = set()

    for i in range(n):
        for j in range(m):
            if (i, j) in visited:
                continue
            find_path(input, i, j, visited, ans)
    return ans

def find_path(input, i, j, visited, ans):
    n, m = len(input), len(input[0])
    visited.add((i, j))
    curr_elevation = input[i][j]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for (dx, dy) in directions:
        if i + dy < 0 or i + dy >= n or j + dx < 0 or j + dx >= m:
            continue

        neighbour = input[i + dy][j + dx]
        steepness = neighbour - curr_elevation

        if steepness > 0:
            is_steepest = check_steepest(input, i + dy, j + dx, steepness)
            if is_steepest:
                find_path(input, i + dy, j + dx, visited, ans)
                ans[i][j] += ans[i + dy][j + dx]
                ans[i + dy][j + dx] = 0



def check_steepest(input, i, j, steepness):
    n, m = len(input), len(input[0])
    # we want to check if the any neighbours have a 
    # steepness greater than `steepness`
    # 2 -> 5 -> 1 ==> returns False 5 - 1 > 5 - 2
    # 2 -> 5 -> 3 ==> returns True 5 - 3 < 5 - 2
    # steepness = 
    curr_elevation = input[i][j]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for (dx, dy) in directions:
        if i + dy < 0 or i + dy >= n or j + dx < 0 or j + dx >= m:
            continue
        neighbour_elevation = input[i + dy][j + dx]
        neighbour_steepness = curr_elevation - neighbour_elevation # notice the order is swapped
        if neighbour_steepness > steepness:
            return False
    return True


for case in test_cases:
    input = case[0]
    expected = case[1]
    actual = sol(input)
    if actual != expected:
        print('Failed: ===============')
        print(f'    Actual = {actual}')
        print(f'    Expected = {expected}')
    else:
        print(f'Passed for input={input}')




