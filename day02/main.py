INPUT_FILE = "input.txt"


def solve(input_file):
    answer1, answer2 = 0, 0
    
    with open(input_file, "r") as f:
        products = f.readline().strip().split(",")
        ids = [(int(a), int(b)) for a, b in (product.split("-") for product in products)]
        
        for pair in ids:
            for id in range(pair[0], pair[1] + 1):
                id_str = str(id)
                digits_count = len(id_str)
                
                ### part 1
                if digits_count % 2 == 0:
                    mid = digits_count // 2
                    left, right = id_str[:mid], id_str[mid:]
                    if left == right:
                        answer1 += id
                    
                ### part 2
                for i in range(1, digits_count // 2 + 1):
                    pattern_count = id_str.count(id_str[:i])
                    if pattern_count * i == digits_count:
                        answer2 += id
                        break
            
    return answer1, answer2


def main():
    answer1, answer2 = solve(INPUT_FILE)
    print(f"Answer #1: {answer1}")
    print(f"Answer #2: {answer2}")


if __name__ == "__main__":
	main()
