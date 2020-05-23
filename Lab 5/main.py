from Directed_Graph import Directed_Graph, print_matrix
from Undirected_Graph import UndirectedGraph
import random
import sys
sys.setrecursionlimit(15000)


class ExitError(Exception):
    pass


class UI:
    def __init__(self, graph):
        self.graph = graph

    def print_menu(self):
        print()
        print("0. Exit")
        print("1. Number of vertices")
        print("2. Parse vertices")
        print("3. Edge between two vertices")
        print("4. In and out degree of a given vertex")
        print("5. Parse the set of outbound edges of a specified vertex")
        print("6. Parse the set of inbound edges of a specified vertex")
        print("7. Retrieve the information (the integer) attached to a specified edge.")
        print("8. Modify the information (the integer) attached to a specified edge.")
        print("9. Save graph to file.")
        print("10. Read graph from file.")
        print("11. Add vertex.")
        print("12. Remove vertex.")
        print("13. Add edge.")
        print("14. Remove edge.")
        print("15. Lowest length path between two vertices. (bfs)")
        print("16. Lowest length path between all vertices. (Floyd-Warshall)")
        print("17. Minimum spannig tree using Kruskal's algorithm")
        print("18. Hamiltonian cycle of low cost")

    def num_vertices(self):
        print(self.graph.Number_of_vertices)

    def parse_vertices(self):
        print(list(self.graph.Vertices))

    def exit(self):
        raise ExitError()

    def edge_between(self):
        print("Edge between")
        x = int(input("x > "))
        y = int(input("y > "))
        # for i in self.graph.dcosts.keys():
        #     print(i, end=" ")
        print(self.graph.edge_between(x, y))

    def in_out_degree(self):
        vertex = int(input("Vertex > "))
        print(
            "Out degree of vertex", vertex, "is :", len(self.graph.out_degree(vertex))
        )
        print("In degree of vertex", vertex, "is :", len(self.graph.in_degree(vertex)))

    def parse_in_vertices(self):
        vertex = int(input("Vertex > "))
        print(self.graph.in_vertices(vertex))

    def parse_out_vertices(self):
        vertex = int(input("Vertex > "))
        print(self.graph.out_vertices(vertex))

    def get_cost(self):
        print("Edge between")
        x = int(input("x > "))
        y = int(input("y > "))
        # for i in self.graph.dcosts.keys():
        #     print(i, end=" ")
        print(self.graph.get_cost(x, y))

    def set_cost(self):
        print("Edge between")
        x = int(input("x > "))
        y = int(input("y > "))
        value = int(input("New value > "))
        self.graph.set_cost(x, y, value)

    def save_to_file(self):
        file_name = input("File name > ")
        self.graph.save_to_file(file_name)

    def read_new_graph(self):
        file_name = input("Graph file name > ")
        self.graph = UndirectedGraph(read_input(file_name))

    def add_vertex(self):
        vertex = int(input("New vertex > "))
        self.graph.add_vertex(vertex)

    def remove_vertex(self):
        vertex = int(input("Delete vertex > "))
        self.graph.remove_vertex(vertex)

    def add_edge(self):
        print("New edge between")
        vertex1 = int(input("x > "))
        vertex2 = int(input("y > "))
        cost = int(input("cost > "))
        self.graph.add_edge(vertex1, vertex2, cost)

    def remove_edge(self):
        print("Remove edge between")
        vertex1 = int(input("x > "))
        vertex2 = int(input("y > "))
        self.graph.remove_edge(vertex1, vertex2)

    def print_path(self, path):
        for i in range(len(path)):
            if i < len(path) - 1:
                print(path[i], end=" -> ")
            else:
                print(path[i])
        print("Length:", len(path) - 1)

    def shortest_path_bfs(self):
        print("Search path between vertices")
        vertex1 = int(input("x > "))
        vertex2 = int(input("y > "))
        path = self.graph.shortest_path_bfs(vertex1, vertex2)
        self.print_path(path)

    def shortest_path_floyd_warshall(self):
        print("Search path between vertices")
        startV = int(input("x > "))
        endV = int(input("y > "))
        distances, parents, path = self.graph.Floyd_Warshall(startV, endV)
        print_matrix(distances)
        print_matrix(parents)
        self.print_path(path)
        print("Cost:", distances[startV][endV])

    def kruskal(self):
        tree, weigth = self.graph.kruskal()
        print(tree)
        print("The weight of the minimum spannig tree is:", weigth)

    def HamiltonianCycle(self):
        graph, weigth, path = self.graph.hamiltonianCycleOfLowCost()
        print(graph)
        print("Weigth:", weigth)
        self.print_path(path)

    def start(self):
        commands = {
            "0": self.exit,
            "1": self.num_vertices,
            "2": self.parse_vertices,
            "3": self.edge_between,
            "4": self.in_out_degree,
            "5": self.parse_out_vertices,
            "6": self.parse_in_vertices,
            "7": self.get_cost,
            "8": self.set_cost,
            "9": self.save_to_file,
            "10": self.read_new_graph,
            "11": self.add_vertex,
            "12": self.remove_vertex,
            "13": self.add_edge,
            "14": self.remove_edge,
            "15": self.shortest_path_bfs,
            "16": self.shortest_path_floyd_warshall,
            "17": self.kruskal,
            "18": self.HamiltonianCycle,
        }
        while True:
            try:
                self.print_menu()
                cmd = input("Option > ")
                if cmd not in commands.keys():
                    raise ValueError("No such option available")
                commands[cmd]()
            except ValueError as va:
                print(va)
            except ExitError:
                break


def read_input(file_name):
    with open(file_name, "r") as f:
        text = f.read()
        text = text.split("\n")
        numbers = []
        for t in text:
            t = t.split(" ")
            # print(t[0])
            if t == [""] or t[0] == "//":
                # print(t, "naspa")
                pass
            else:
                numbers.extend(t)
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        # print(numbers)
        return numbers


def generate_graph(num_vertices=None, num_edges=None):
    if num_edges == None or num_vertices == None:
        num_vertices = int(input("Number of vertices > "))
        num_edges = int(input("Number of edges > "))

    graph = [num_vertices, num_edges]
    edges = []
    while len(edges) < num_edges:
        v1 = random.choice(range(num_vertices))
        v2 = random.choice(range(num_vertices))
        cost = random.choice(range(0, 100))
        edge = (v1, v2, cost)
        if edge not in (edges):
            print(len(edges), num_edges)
            edges.append(edge)

    for e in edges:
        graph.extend([e[0], e[1], e[2]])
    return graph


def generate_and_save():
    d = Directed_Graph(generate_graph(10000, 100000))
    d.save_to_file("seminar_graph10k.txt")
    d = Directed_Graph(generate_graph(100000, 1000000))
    d.save_to_file("seminar_graph100k.txt")
    d = Directed_Graph(generate_graph(1000000, 10000000))
    d.save_to_file("seminar_graph1kk.txt")


# generate_and_save()


def generate_graph_v2(num_vertices=None, num_edges=None):

    while True:
        if num_edges == None or num_vertices == None:
            # print("Nu e bine")
            # print(num_edges, num_vertices)
            num_vertices = int(input("Number of vertices > "))
            num_edges = int(input("Number of edges > "))

        if num_edges > (num_vertices * (num_vertices + 1)) / 2:
            print("Cannot generate such a graph.")
            num_edges = None
            num_vertices = None
        else:
            break

    graph = [num_vertices, num_edges]
    edges = {}
    while len(edges) < num_edges:
        v1 = random.choice(range(num_vertices))
        v2 = random.choice(range(num_vertices))
        cost = random.choice(range(0, 10))
        # edge[(v1,v2)] = cost

        if v1 != v2:
            if (v1, v2) not in edges:
                edges[(v1, v2)] = cost
                graph.extend([v1, v2, cost])
                # if len(edges) % 100000 == 0:
                # print(len(edges), num_edges)

    # for e in edges:
    #     graph.extend([e[0], e[1], e[2]])
    return graph


def generate_graph_v2_test():
    print("Executing test generate_graph_v2_test")
    # d = Directed_Graph(generate_graph_v2(100000, 1000000))
    # d.save_to_file("seminar_graph100k.txt")
    d = Directed_Graph(generate_graph_v2(10000, 100000))
    d.save_to_file("seminar_graph10k.txt")
    

# generate_graph_v2_test()


def main_start():
    print("1. Generate random graph")
    print("2. Read from file")
    while True:
        option = input(" > ")
        # option = "2"
        if option == "1":
            ui = UI(UndirectedGraph(generate_graph_v2()))
            break
        elif option == "2":
            input_file = "small_graph.txt"
            # input_file = "input1kvertices.txt"
            # file = "graph1m.txt"
            ui = UI(UndirectedGraph(read_input(input_file)))
            # ui.HamiltonianCycle()
            break
        else:
            print("No such option")

    ui.start()


def random_example():
    ui = UI(Directed_Graph(generate_graph_v2(8, 17)))
    graph = ui.graph
    # print(graph.dout)
    # print(graph.din)
    # print(graph.dcosts)
    graph.dout = {
        0: [1],
        1: [7, 0, 4, 3],
        2: [2],
        3: [1],
        4: [4],
        5: [0, 6, 7, 2],
        6: [0, 2, 6, 7],
        7: [4],
    }
    graph.din = {
        0: [5, 1, 6],
        1: [0, 3],
        2: [6, 5, 2],
        3: [1],
        4: [1, 4, 7],
        5: [],
        6: [6, 5],
        7: [1, 5, 6],
    }
    graph.dcosts = {
        (0, 1): 0,
        (1, 7): 67,
        (5, 0): 12,
        (1, 0): 87,
        (3, 1): 21,
        (6, 0): 15,
        (1, 4): 64,
        (6, 2): 17,
        (6, 6): 47,
        (4, 4): 62,
        (5, 6): 4,
        (1, 3): 22,
        (5, 7): 38,
        (5, 2): 41,
        (2, 2): 65,
        (6, 7): 9,
        (7, 4): 48,
    }
    graph.save_to_file("repres_ex.txt")


# random_example()
if __name__ == "__main__":
    main_start()
