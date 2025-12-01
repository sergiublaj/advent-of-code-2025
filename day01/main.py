INPUT_FILE = "input.txt"
MAX_NUMBERS = 100
STARTING_POSITION = 50


def solve(input_file):
    new_position, position = STARTING_POSITION, STARTING_POSITION
    answer1, answer2 = 0, 0
    
    with open(input_file, "r") as f:
        for line in f:
            direction = -1 if line[0] == "L" else 1
            rotations = int(line[1:])
            
            new_position = (position + direction * rotations) % MAX_NUMBERS 
            
            ### part 1
            answer1 += 1 if new_position == 0 else 0
            
            ### part 2
            if direction == 1:
                answer2 += (position + direction * rotations) // MAX_NUMBERS
            else:
                answer2 += ((MAX_NUMBERS - position) % MAX_NUMBERS - direction * rotations) // MAX_NUMBERS
                
            position = new_position
            
    return answer1, answer2


def main():
    answer1, answer2 = solve(INPUT_FILE)
    print(f"Answer #1: {answer1}")
    print(f"Answer #2: {answer2}")


if __name__ == "__main__":
	main()
