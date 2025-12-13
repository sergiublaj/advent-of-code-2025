INPUT_FILE = "input.txt"
START_NODE = "you"
STOP_NODE = "out"
SVR_NODE = "svr"
DAC_NODE = "dac"
FFT_NODE = "fft"


class Node:
    def __init__(self, value, neighbors=[]):
        self.value = value
        self.neighbors = neighbors


def read_node(line):
    key, value = line.strip().split(":", 1)
    key = key.strip()
    value = value.strip().split(" ")
    
    return Node(key, [v for v in value])


def fix_nodes(nodes):
    node_map = {node.value: node for node in nodes}
    node_map[STOP_NODE] = Node(STOP_NODE, [])
    
    for node in nodes:
        node.neighbors = [node_map[n] for n in node.neighbors]
    
    return nodes


def get_node(nodes, value):
    return list(filter(lambda n: n.value == value, nodes))[0]


def count_paths(node, required=frozenset(), state={}):
    key = (node.value, required)
    if key in state:
        return state[key]
    if node.value == STOP_NODE:
        return 1 if not required else 0
    
    paths_count = 0
    for neighbor in node.neighbors:
        paths_count += count_paths(neighbor, required - {node.value}, state)
    state[key] = paths_count
    
    return paths_count


def solve(input_file):
    nodes = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            nodes.append(read_node(line))
    
    nodes = fix_nodes(nodes)

    answer1 = count_paths(get_node(nodes, START_NODE))
    answer2 = count_paths(get_node(nodes, SVR_NODE), frozenset({DAC_NODE, FFT_NODE}))
    
    return answer1, answer2


def main():
    answer1, answer2 = solve(INPUT_FILE)
    print(f"Answer #1: {answer1}")
    print(f"Answer #2: {answer2}")


if __name__ == "__main__":
	main()
