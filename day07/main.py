INPUT_FILE = "input.txt"
START = "S"
SPLITTER = "^"
BEAM = "|"
EMPTY = "."


def solve(input_file):
    answer1, answer2 = 0, 0
    
    grid = []
    pascal = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            grid.append([x for x in line.strip()])
            pascal.append([0 for _ in line.strip()])
    
    start = grid[0].index(START)
    grid[1][start] = BEAM
    pascal[1][start] = 1
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if grid[i - 1][j] != BEAM:
                continue
            
            if grid[i][j] == EMPTY:
                grid[i][j] = BEAM
            
            if grid[i][j] == BEAM:
                pascal[i][j] += pascal[i - 1][j]
            
            if grid[i][j] == SPLITTER:
                splitted = False
                if grid[i][j - 1] == EMPTY:
                    grid[i][j - 1] = BEAM
                    splitted = True
                if grid[i][j + 1] == EMPTY:
                    grid[i][j + 1] = BEAM
                    splitted = True
                answer1 += int(splitted)
            
                pascal[i][j - 1] += pascal[i - 1][j]
                pascal[i][j + 1] += pascal[i - 1][j]
    
    answer2 = sum(pascal[-1])
    
    return answer1, answer2


def main():
    answer1, answer2 = solve(INPUT_FILE)
    print(f"Answer #1: {answer1}")
    print(f"Answer #2: {answer2}")


if __name__ == "__main__":
	main()
