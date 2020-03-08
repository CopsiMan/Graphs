class Directed_Graph:
    def __init__(self, graph_list):
        self.graph = graph_list
        self.num_verteces = self.graph[0]
        self.num_edges = self.graph[1]
        self.dout = {}
        self.din = {}
        self.dcosts = {}
        self.set_dicts()

    def set_dicts(self):
        for e in range(self.num_verteces):
            self.din[e] = []
            self.dout[e] = []
        for e in range(self.num_edges):
            self.dcosts[(self.graph[2 + 3 * e], self.graph[3 * (e + 1)])] = self.graph[
                4 + 3 * e
            ]
            # print(self.graph[e])
            self.dout[self.graph[2 + 3 * e]].append(self.graph[3 + 3 * e])
            self.din[self.graph[3 + 3 * e]].append(self.graph[2 + 3 * e])


class ExitError(Exception):
    pass


class UI:
    def __init__(self, input_file):
        self.numbers = self.read_input(input_file)
        self.graph = Directed_Graph(self.numbers)

    def read_input(self, file_name):
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

    def print_menu(self):
        print("0. Exit")
        print("1. Number of vertices")
        print("2. Parse vertices")
        print("3. Edge between two vertices")
        print("4. In and out degree of a given vertex")
        print("5. Parse the set of outbound edges of a specified vertex")
        print("6. Parse the set of inbound edges of a specified vertex")
        print("7. Retrieve the information (the integer) attached to a specified edge.")
        print("8. Modify the information (the integer) attached to a specified edge.")

    def num_vertices(self):
        print(self.graph.num_verteces)

    def parse_vertices(self):
        print(list(range(self.graph.num_verteces)))

    def exit(self):
        raise ExitError()

    def edge_between(self):
        print("Edge between")
        x = int(input("x > "))
        y = int(input("y > "))
        # for i in self.graph.dcosts.keys():
        #     print(i, end=" ")
        print((x, y) in self.graph.dcosts.keys())

    def in_out_degree(self):
        vertex = int(input("Vertex > "))
        print("Out degree of vertex", vertex, "is :", len(self.graph.dout[vertex]))
        print("In degree of vertex", vertex, "is :", len(self.graph.din[vertex]))

    def parse_in_edges(self):
        vertex = int(input("Vertex > "))
        print(self.graph.din[vertex])

    def parse_out_edges(self):
        vertex = int(input("Vertex > "))
        print(self.graph.dout[vertex])

    def get_cost(self):
        print("Edge between")
        x = int(input("x > "))
        y = int(input("y > "))
        # for i in self.graph.dcosts.keys():
        #     print(i, end=" ")
        print(self.graph.dcosts[x, y])

    def set_cost(self):
        print("Edge between")
        x = int(input("x > "))
        y = int(input("y > "))
        value = int(input("New value > "))
        # for i in self.graph.dcosts.keys():
        #     print(i, end=" ")
        self.graph.dcosts[x, y] = value

    def start(self):
        commands = {
            "0": self.exit,
            "1": self.num_vertices,
            "2": self.parse_vertices,
            "3": self.edge_between,
            "4": self.in_out_degree,
            "5": self.parse_out_edges,
            "6": self.parse_in_edges,
            "7": self.get_cost,
            "8": self.set_cost,
        }
        while True:
            try:
                self.print_menu()
                cmd = input("Option > ")
                commands[cmd]()
            except ValueError as va:
                print(va)
            except ExitError:
                break


file = "input1kvertices.txt"
# file = "graph1m.txt"
ui = UI(file)
ui.start()
