from Directed_Graph import Directed_Graph


class ExitError(Exception):
    pass


class UI:
    def __init__(self, input_file):
        graph_input = self.read_input(input_file)
        self.graph = Directed_Graph(graph_input)

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
        print(self.graph.num_vertices)

    def parse_vertices(self):
        print(list(self.graph.dout.keys()))

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
        if self.graph.check_vertex_validity(vertex) == False:
            raise ValueError("Invalid vertex")
        print("Out degree of vertex", vertex, "is :", len(self.graph.dout[vertex]))
        print("In degree of vertex", vertex, "is :", len(self.graph.din[vertex]))

    def parse_in_edges(self):
        vertex = int(input("Vertex > "))
        if self.graph.check_vertex_validity(vertex) == False:
            raise ValueError("Invalid vertex")
        print(self.graph.din[vertex])

    def parse_out_edges(self):
        vertex = int(input("Vertex > "))
        if self.graph.check_vertex_validity(vertex) == False:
            raise ValueError("Invalid vertex")
        print(self.graph.dout[vertex])

    def get_cost(self):
        print("Edge between")
        x = int(input("x > "))
        y = int(input("y > "))
        if self.graph.check_edge_validity(x, y) == False:
            raise ValueError("Invalid edge")
        # for i in self.graph.dcosts.keys():
        #     print(i, end=" ")
        print(self.graph.dcosts[x, y])

    def set_cost(self):
        print("Edge between")
        x = int(input("x > "))
        y = int(input("y > "))
        if self.graph.check_edge_validity(x, y) == False:
            raise ValueError("Invalid edge")
        value = int(input("New value > "))
        # for i in self.graph.dcosts.keys():
        #     print(i, end=" ")
        self.graph.dcosts[x, y] = value

    def save_to_file(self):
        file_name = input("File name > ")
        self.graph.save_to_file(file_name)

    def read_new_graph(self):
        file_name = input("Graph file name > ")
        self.graph = Directed_Graph(self.read_input(file_name))

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
            "5": self.parse_out_edges,
            "6": self.parse_in_edges,
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


input_file = "input.txt"
# input_file = "input1kvertices.txt"
# file = "graph1m.txt"
ui = UI(input_file)
ui.start()
