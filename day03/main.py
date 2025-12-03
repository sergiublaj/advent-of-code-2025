INPUT_FILE = "input.txt"


def get_maxes(digits, max_digits):
    maxs = digits[len(digits) - max_digits:]
    positions = [x for x in range(len(digits) - max_digits, len(digits))]
    limit = 0
    
    for j in range(max_digits):
        i = positions[j]
        while i >= limit:
            if digits[i] >= maxs[j]:
                maxs[j] = digits[i]
                positions[j] = i
            i -= 1
        
        limit = positions[j] + 1
    
    return int("".join([str(x) for x in maxs[:max_digits]]))
    

def solve(input_file):
    answer1, answer2 = 0, 0
    
    with open(input_file, "r") as f:
        for line in f:
            digits = [int(x) for x in line.strip()]
            answer1 += get_maxes(digits, 2)
            answer2 += get_maxes(digits, 12)
                
    return answer1, answer2


def main():
    answer1, answer2 = solve(INPUT_FILE)
    print(f"Answer #1: {answer1}")
    print(f"Answer #2: {answer2}")


if __name__ == "__main__":
	main()
