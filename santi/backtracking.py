def solve_maze_backtracking(M, N, maze):
    visited = set()

    def is_valid(x, y):
        return 0 <= x < M and 0 <= y < N and (x, y) not in visited and maze[x][y] == 1

    def backtrack(x, y):
        if x == M - 1 and y == N - 1:
            solution[x][y] = 1
            return True

        if is_valid(x, y):
            solution[x][y] = 1
            visited.add((x, y))

            if (
                backtrack(x + 1, y)
                or backtrack(x, y + 1)
                or backtrack(x - 1, y)
                or backtrack(x, y - 1)
            ):
                return True

            solution[x][y] = 0

        return False

    solution = [[0] * N for _ in range(M)]
    if backtrack(0, 0):
        return solution
    else:
        return None


# CASOS PRUEBA
# 1.
M = 4
N = 4
maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [0, 1, 1, 1]]

solution = solve_maze_backtracking(M, N, maze)
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

solution = solve_maze_backtracking(M, N, maze)
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

solution = solve_maze_backtracking(M, N, maze)
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

solution = solve_maze_backtracking(M, N, maze)
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

solution = solve_maze_backtracking(M, N, maze)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists.")
