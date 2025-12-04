INPUT_FILE = "input.txt"
FORKLIFT = "X"
PAPER_ROLL = "@"
MAX_NEIGHBOURS = 4
DI = [0, 1, 1, 1, 0, -1, -1, -1]
DJ = [-1, -1, 0, 1, 1, 1, 0, -1]


def read_grid(input_file):
    grid = []
    with open(input_file, "r") as f:
        for line in f:
            grid.append([x for x in line.strip()])

    return grid


def is_in_bound(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def get_neighbours(grid, i, j, targets):
    count = 0
    for k in range(len(DI)):
        ii = i + DI[k]
        jj = j + DJ[k]
        if is_in_bound(grid, ii, jj) and grid[ii][jj] in targets:
            count += 1
    
    return count


def solve(input_file):
    grid = read_grid(input_file)
    answer1, answer2, finished = 0, 0, False
    
    while not finished:
        finished = True
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != PAPER_ROLL:
                    continue
                
                ### part 1
                ### check for both PAPER_ROLL and FORKLIFT because part 1 doesn't modify the grid
                ### and we want to count both as PAPER_ROLLs for part 1
                neighbours1 = get_neighbours(grid, i, j, [PAPER_ROLL, FORKLIFT])
                if neighbours1 < MAX_NEIGHBOURS:
                    answer1 += 1
                
                ### part 2
                neighbours2 = get_neighbours(grid, i, j, [PAPER_ROLL])
                if neighbours2 < MAX_NEIGHBOURS:
                    answer2 += 1
                    finished = False
                    grid[i][j] = FORKLIFT
        
    return answer1, answer2


def main():
    answer1, answer2 = solve(INPUT_FILE)
    print(f"Answer #1: {answer1}")
    print(f"Answer #2: {answer2}")


if __name__ == "__main__":
	main()
