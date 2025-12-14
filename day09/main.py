INPUT_FILE = "input.txt"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []

    def get_area(self, point):
        return (abs(self.x - point.x) + 1) * (abs(self.y - point.y) + 1)


def build_neighbors(sorted_points, equality_attr):
    for i in range(len(sorted_points) - 1):
        for j in range(i + 1, len(sorted_points)):
            if getattr(sorted_points[i], equality_attr) == getattr(sorted_points[j], equality_attr):
                sorted_points[i].neighbors.append(sorted_points[j])
                sorted_points[j].neighbors.append(sorted_points[i])


def build_limits(sorted_points, limit_builder):
    limits = []
    for i in range(0, len(sorted_points), 2):
        limits.append(limit_builder(sorted_points[i], sorted_points[i + 1]))
        
    return limits


def is_rectangle_valid(p1, p2, limits_x, limits_y):
    top_left = Point(min(p1.x, p2.x), min(p1.y, p2.y))
    bottom_right = Point(max(p1.x, p2.x), max(p1.y, p2.y))
    
    for x, y_start, y_stop in limits_x:
        if top_left.x < x < bottom_right.x and top_left.y < y_stop and y_start < bottom_right.y:
            return False
    
    for y, x_start, x_stop in limits_y:
        if top_left.y < y < bottom_right.y and top_left.x < x_stop and x_start < bottom_right.x:
            return False
    
    return True
    

def solve(input_file):
    answer1, answer2 = 0, 0
    points = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            x, y = map(int, line.strip().split(","))
            points.append(Point(x, y))

    sorted_by_x = sorted(points, key=lambda p: (p.x, p.y))
    sorted_by_y = sorted(points, key=lambda p: (p.y, p.x))
    
    build_neighbors(sorted_by_x, 'y')
    build_neighbors(sorted_by_y, 'x')
    
    limits_x = build_limits(sorted_by_x, lambda p1, p2: (p1.x, p1.y, p2.y))
    limits_y = build_limits(sorted_by_y, lambda p1, p2: (p1.y, p1.x, p2.x))
        
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            area = points[i].get_area(points[j])
            
            ### part 1
            answer1 = max(answer1, area)
            
            ### part 2
            if is_rectangle_valid(points[i], points[j], limits_x, limits_y):
                answer2 = max(answer2, area)
                
    return answer1, answer2


def main():
    answer1, answer2 = solve(INPUT_FILE)
    print(f"Answer #1: {answer1}")
    print(f"Answer #2: {answer2}")


if __name__ == "__main__":
	main()
