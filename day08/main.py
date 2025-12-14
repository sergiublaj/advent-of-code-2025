INPUT_FILE = "input.txt"
MAX_STEPS = 1000
INFINITE = 10**12


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def get_distance(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2


class Edge:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.weight = start.get_distance(stop)


class Graph:
    def __init__(self):
        self.edges = []
        self.nodes = set()
    
    def add_edge(self, edge):
        self.edges.append(edge)
        self.nodes.update((edge.start, edge.stop))
        
    def sort_edges(self):
        self.edges = sorted(self.edges, key=lambda edge: edge.weight)


def read_points(input_file):
    points = []
    with open(input_file, "r") as f:
        for line in f:
            x, y, z = map(int, line.strip().split(","))
            points.append(Point(x, y, z))
            
    return points


def build_graph(points):
    graph = Graph()
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            graph.add_edge(Edge(points[i], points[j]))
            
    return graph


def find_component_index(node, components):
    for idx, component in enumerate(components):
        if node in component:
            return idx
    
    return None


def kruskal(graph, max_steps=INFINITE):
    components = [{node} for node in graph.nodes]
    mst = []
    last_edge = None
    steps = 0

    for edge in graph.edges:
        steps += 1
        if steps >= max_steps or len(mst) == len(graph.nodes) - 1:
            break

        start_component = find_component_index(edge.start, components)
        stop_component = find_component_index(edge.stop, components)
        if start_component is None or stop_component is None or start_component == stop_component:
            continue

        mst.append(edge)
        last_edge = edge
        
        components[start_component] = components[start_component].union(components[stop_component])
        components.pop(stop_component)

    return components, last_edge
    

def solve(input_file):
    points = read_points(input_file)
    graph = build_graph(points)
    graph.sort_edges()
    
    ### part 1
    components, _ = kruskal(graph, MAX_STEPS)
    components_sizes = sorted([len(component) for component in components])[::-1]
    answer1 = eval("*".join(map(str, components_sizes[:3])))
    
    ### part 2
    _, last_edge = kruskal(graph)
    answer2 = last_edge.start.x * last_edge.stop.x
        
    return answer1, answer2


def main():
    answer1, answer2 = solve(INPUT_FILE)
    print(f"Answer #1: {answer1}")
    print(f"Answer #2: {answer2}")


if __name__ == "__main__":
	main()
