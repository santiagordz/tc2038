def is_valid_move(labyrinth, x, y, sol):
    if (
        0 <= x < len(labyrinth)
        and 0 <= y < len(labyrinth[0])
        and labyrinth[x][y] == 1
        and sol[x][y] == 0
    ):
        return True
    return False


def solve_maze(labyrinth):
    if not labyrinth:
        return []

    M = len(labyrinth)
    N = len(labyrinth[0])
    sol = [[0] * N for _ in range(M)]

    if solve_maze_util(labyrinth, 0, 0, sol):
        return sol
    else:
        return []


def solve_maze_util(labyrinth, x, y, sol):
    if x == len(labyrinth) - 1 and y == len(labyrinth[0]) - 1:
        sol[x][y] = 1
        return True

    if is_valid_move(labyrinth, x, y, sol):
        sol[x][y] = 1

        if solve_maze_util(labyrinth, x, y + 1, sol):
            return True

        if solve_maze_util(labyrinth, x + 1, y, sol):
            return True

        # If neither right nor down is a solution, backtrack and unmark the cell
        sol[x][y] = 0
        return False

    return False


# CASOS PRUEBA
# 1.
M = 4
N = 4
maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [0, 1, 1, 1]]

solution = solve_maze(maze)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists.")
# 2.
print()
M = 4
N = 5
maze = [[1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1]]
# print maze

solution = solve_maze(maze)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists.")
# 3.
print()
M = 6
N = 6
maze = [
    [1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1],
]
# print maze

solution = solve_maze(maze)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists.")

# 4.
print()
M = 4
N = 4
maze = [[1, 0, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 1]]
# print maze

solution = solve_maze(maze)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists.")

# 5.
print()
M = 7
N = 9
maze = [
    [1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1],
]
# print maze

solution = solve_maze(maze)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists.")
