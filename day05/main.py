INPUT_FILE = "input.txt"


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    
    if value[1] < root.value[0]:
        root.left = insert_node(root.left, value)
    elif value[0] > root.value[1]:
        root.right = insert_node(root.right, value)
    else:
        root.value = (min(root.value[0], value[0]), max(root.value[1], value[1]))

    return root


def build_tree(ranges):
    mid = sorted(ranges, key=lambda x: (x[0], x[1]))[len(ranges) // 2]
    ranges.remove(mid)
    
    tree = TreeNode(mid)
    for range in ranges:
        tree = insert_node(tree, range)
        
    return tree


def inorder_traversal(node):
    if node is None:
        return []
    
    traversal = []
    traversal.extend(inorder_traversal(node.left))
    traversal.append(node.value)
    traversal.extend(inorder_traversal(node.right))
    
    return traversal


def solve(input_file):
    answer1, answer2 = 0, 0

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        separator_idx = lines.index("")
        fresh_ranges = [(int(x), int(y)) for x, y in (r.split("-") for r in lines[:separator_idx])]
        ids = [int(x) for x in lines[separator_idx + 1:]]
        tree = build_tree(fresh_ranges)
        inorder = inorder_traversal(tree)
        
        ### part 1
        for id in ids:
            for node in inorder:
                if node[0] <= id <= node[1]:
                    answer1 += 1
                    break
        
        ### part 2
        for node in inorder:
            answer2 += (node[1] - node[0] + 1)
        # remove overlaps
        for i in range(len(inorder) - 1):
            if inorder[i][1] >= inorder[i + 1][0]:
                answer2 -= (inorder[i][1] - inorder[i + 1][0] + 1)
            
    return answer1, answer2


def main():
    answer1, answer2 = solve(INPUT_FILE)
    print(f"Answer #1: {answer1}")
    print(f"Answer #2: {answer2}")


if __name__ == "__main__":
	main()
