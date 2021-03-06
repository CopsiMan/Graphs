from Directed_Graph import Directed_Graph
import random


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
        self.graph = Directed_Graph(read_input(file_name))

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


def main_start():
    print("1. Generate random graph")
    print("2. Read from file")
    while True:
        option = input(" > ")
        if option == "1":
            ui = UI(Directed_Graph(generate_graph()))
            break
        elif option == "2":
            input_file = "graph1k.txt"
            # input_file = "input1kvertices.txt"
            # file = "graph1m.txt"
            ui = UI(Directed_Graph(read_input(input_file)))
            break
        else:
            print("No such option")

    ui.start()


# main_start()
def generate_and_save():
    d = Directed_Graph(generate_graph(10000, 100000))
    d.save_to_file("seminar_graph10k.txt")
    d = Directed_Graph(generate_graph(100000, 1000000))
    d.save_to_file("seminar_graph100k.txt")
    d = Directed_Graph(generate_graph(1000000, 10000000))
    d.save_to_file("seminar_graph1kk.txt")


# generate_and_save()


def generate_graph_v2(num_vertices=None, num_edges=None):
    if num_edges == None or num_vertices == None:
        print("Nu e bine")
        print(num_edges, num_vertices)
        num_vertices = int(input("Number of vertices > "))
        num_edges = int(input("Number of edges > "))

    graph = [num_vertices, num_edges]
    edges = {}
    while len(edges) < num_edges:
        v1 = random.choice(range(num_vertices))
        v2 = random.choice(range(num_vertices))
        cost = random.choice(range(0, 100))
        # edge[(v1,v2)] = cost
        if (v1, v2) not in edges:
            edges[(v1, v2)] = cost
            graph.extend([v1, v2, cost])
            if len(edges) % 100000 == 0:
                print(len(edges), num_edges)

    # for e in edges:
    #     graph.extend([e[0], e[1], e[2]])
    return graph


def generate_graph_v2_test():
    print("Executing test generate_graph_v2_test")
    # d = Directed_Graph(generate_graph_v2(100000, 1000000))
    # d.save_to_file("seminar_graph100k.txt")
    d = Directed_Graph(generate_graph_v2(10000,100000))
    d.save_to_file("seminar_graph10k.txt")


# generate_graph_v2_test()
