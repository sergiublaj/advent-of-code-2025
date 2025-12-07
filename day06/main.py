INPUT_FILE = "input.txt"


def read_grid_part1(input_file):
    grid = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            grid.append([x for x in line.split()])
            
    return grid


def read_grid_part2(input_file):
    grid = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            grid.append([x for x in line])
            
    return grid


def solve_grid_part1(grid):
    answer = 0
    for j in range(len(grid[0])):
        nums = [int(row[j]) for row in grid[:-1]]
        operator = grid[-1][j]
        answer += eval(f" {operator} ".join(map(str, nums))) 
        
    return answer


def solve_grid_part2(grid):
    answer, numbers = 0, []
    for j in range(len(grid[0]) - 2, -1, -1):
        number = "".join(str(grid[i][j]) for i in range(len(grid) - 1)).strip()
        numbers.append(int(number) if number else 0)
    operators = [x for x in "".join(grid[-1]).split()]
    start, stop = 0, -1
    for crt_operator_idx in range(len(operators)):
        start = stop + 1
        stop = numbers.index(0, start) if 0 in numbers[start:] else len(numbers)
        nums = " ".join(map(str, numbers[start:stop]))
        operator = operators[len(operators) - crt_operator_idx - 1]
        answer += eval(f" {operator} ".join(map(str, nums.split())))
        
    return answer

def solve(input_file):
    grid1 = read_grid_part1(input_file)
    answer1 = solve_grid_part1(grid1)
    
    grid2 = read_grid_part2(input_file)
    answer2 = solve_grid_part2(grid2)
        
    return answer1, answer2


def main():
    answer1, answer2 = solve(INPUT_FILE)
    print(f"Answer #1: {answer1}")
    print(f"Answer #2: {answer2}")


if __name__ == "__main__":
	main()
