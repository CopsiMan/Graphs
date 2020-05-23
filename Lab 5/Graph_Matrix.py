class Graph_Matrix:
    def __init__(self, file_name):
        self.file_name = file_name
        self.num_vertices = 0
        self.num_edges = 0
        self.matrix = []
        self.create_matrix()

    def create_matrix(self):
        with open(self.file_name, "r") as file:
            line = next(file).split()
            # print(line)
            self.num_vertices = int(line[0])
            # print(self.num_vertices, self.num_edges)
            self.num_edges = int(line[1])

            # init matrix with -1
            for i in range(self.num_vertices):
                self.matrix.append([])
                for j in range(self.num_vertices):
                    self.matrix[i].append(-1)

            for line in file:
                line = line.split()
                v1 = int(line[0])
                v2 = int(line[1])
                cost = int(line[2])
                self.matrix[v1][v2] = cost

    def print_matrix(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                print(self.matrix[i][j], end=' ')
            print()

    def check_vertex_validity(self, vertex):
        if vertex not in range(0, self.num_vertices):
            return False
        return True

    def in_vertices(self, vertex):
        result = []
        for i in range(self.num_vertices):
            if self.matrix[i][vertex] != -1:
                result.append(i)
        return result

    def out_vertices(self, vertex):
        result = []
        for i in range(self.num_vertices):
            if self.matrix[vertex][i] != -1:
                result.append(i)
        return result

    @property
    def Vertices(self):
        return list(range(self.num_vertices))
