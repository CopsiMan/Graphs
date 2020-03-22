class Directed_Graph_Only_Outbound:
    def __init__(self, file_name):
        self.file_name = file_name
        self.dout = {}
        self.dcost = {}
        self.num_vertices = 0
        self.num_edges = 0
        self.init_dict()

    def init_dict(self):
        with open(self.file_name, "r") as file:
            line = next(file).split()
            # print(line)
            self.num_vertices = int(line[0])
            # print(self.num_vertices, self.num_edges)
            self.num_edges = int(line[1])
            for line in file:
                line = line.split()
                v1 = int(line[0])
                v2 = int(line[1])
                cost = int(line[2])
                if v1 not in self.dout:
                    self.dout[v1] = [v2]
                    self.dcost[v1] = [cost]
                else:
                    self.dout[v1].append(v2)
                    self.dcost[v1].append(cost)

    def check_vertex_validity(self, vertex):
        if vertex not in self.dout.keys():
            return False
        return True

    def out_vertices(self, vertex):
        if self.check_vertex_validity(vertex) == False:
            raise ValueError("Invalid vertex")
        return list(self.dout[vertex])

    def in_vertices(self, vertex1):
        result = []
        for vertex2 in self.dout.keys():
            if vertex1 in self.dout[vertex2]:
                result.append(vertex2)
        return result

        # if self.check_vertex_validity(vertex) == False:
        #     raise ValueError("Invalid vertex")

        # return list(self.dout[vertex])

    @property
    def Vertices(self):
        return list(self.dout.keys())


def test_Directed_Graph_Only_Outbound():
    g = Directed_Graph_Only_Outbound("seminar_graph1k.txt")
    print(g.num_vertices)


# test_Directed_Graph_Only_Outbound()
