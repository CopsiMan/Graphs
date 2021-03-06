import numpy as np

inf = float("inf")


class Directed_Graph:
    def __init__(self, graph_list):
        """
        input: list of edges with costs in the form : <vertex 1> <vertex 2> <value associated with the edge>
        """
        self.graph = graph_list
        self.num_vertices = self.graph[0]
        self.num_edges = self.graph[1]
        # print(len(self.graph))
        # print(self.graph[16600000])
        # print(self.graph[30000000])
        # print(self.graph[16877219])
        self.dout = {}
        self.din = {}
        self.dcosts = {}
        self.set_dicts()

    def check_vertex_validity(self, vertex):
        """
        input: vertex of a graph 
        out: true if the vertex is valid
        """
        if vertex not in self.dout.keys():
            return False
        return True

    def save_to_file(self, file_name):
        """
        input: name of file to save tha graph
        """
        with open(file_name, "w") as f:
            f.write(str(self.num_vertices) + " " + str(self.num_edges))
            for e in self.dcosts.keys():
                f.write("\n" + str(e[0]) + " " + str(e[1]) + " " + str(self.dcosts[e]))

    def check_edge_validity(self, vertex1, vertex2):
        """
        pre: valid vertices 
        input: 2 vertices
        out: true if there is an edge between vertex1 and vertex2
        """
        if (vertex1, vertex2) not in self.dcosts.keys():
            return False
        return True

    def set_dicts(self):
        """
        Initialize the dictionaries
        """
        for e in range(self.num_vertices):
            self.din[e] = []
            self.dout[e] = []

        for e in range(self.num_edges):
            # if (4 + 3 * e) % 100000 == 0 or (4 + 3 * e) > 16600000:
            #     print(4 + 3 * e)
            self.dcosts[(self.graph[2 + 3 * e], self.graph[3 * (e + 1)])] = self.graph[
                4 + 3 * e
            ]
            # print(self.graph[e])
            self.dout[self.graph[2 + 3 * e]].append(self.graph[3 + 3 * e])
            self.din[self.graph[3 + 3 * e]].append(self.graph[2 + 3 * e])

    def add_vertex(self, vertex):
        """
        pre: vertex not already in graph
        input: vertex to add
        """
        if self.check_vertex_validity(vertex) == True:
            raise ValueError("Vertex already in graph")
        self.num_vertices += 1
        self.dout[vertex] = []
        self.din[vertex] = []

    def get_cost(self, vertex1, vertex2):
        """
        pre: vertex1 and vertex2 are valid
        input: two vertices
        out: the cost associated with the edge between vertex1 and vertex2
        """
        if self.check_edge_validity(vertex1, vertex2) == False:
            raise ValueError("Invalid edge")

        return self.dcosts[(vertex1, vertex2)]

    def set_cost(self, vertex1, vertex2, cost):
        """
        pre: vertex1 and vertex2 are valid and there exists and edge between them
        input: two vertices and a cost
        """
        if self.check_edge_validity(vertex1, vertex2) == False:
            raise ValueError("Invalid edge")
        # for i in self.graph.dcosts.keys():
        #     print(i, end=" ")
        self.dcosts[(vertex1, vertex2)] = cost
        self.dcosts[(vertex2, vertex1)] = cost

    def remove_vertex(self, vertex):
        """
        pre: vertex1 is valid
        input: vertex to remove 
        """
        if self.check_vertex_validity(vertex) == False:
            raise ValueError("Vertex doesn't exist")

        for v in self.din[vertex]:
            if v != vertex:
                del self.dcosts[v, vertex]
                self.dout[v].remove(vertex)
                self.num_edges -= 1

        for v in self.dout[vertex]:
            del self.dcosts[vertex, v]
            self.num_edges -= 1
            self.din[v].remove(vertex)

        del self.dout[vertex]
        del self.din[vertex]

        self.num_vertices -= 1

    def remove_edge(self, vertex1, vertex2):
        """
        pre: vertex1 and vertex2 are valid and there exists and edge between them
        input: two vertices
        """
        if self.check_edge_validity(vertex1, vertex2) == False:
            raise ValueError("Edge doesn't exist")

        del self.dcosts[(vertex1, vertex2)]
        self.dout[vertex1].remove(vertex2)
        self.din[vertex2].remove(vertex1)

        self.num_edges -= 1

    def add_edge(self, vertex1, vertex2, cost):
        """
        pre: vertex1 and vertex2 are valid and there does not exists and edge between them
        input: two vertices and a cost
        """
        if self.check_vertex_validity(vertex1) == False:
            raise ValueError("Vertex " + str(vertex1) + " doesn't exist")

        if self.check_vertex_validity(vertex2) == False:
            raise ValueError("Vertex  " + str(vertex2) + "doesn't exist")

        if self.check_edge_validity(vertex1, vertex2):
            raise ValueError("Edge already exists")

        self.dcosts[(vertex1, vertex2)] = cost
        self.dout[vertex1].append(vertex2)
        self.din[vertex2].append(vertex1)

        self.num_edges += 1

    def edge_between(self, vertex1, vertex2):
        """
        pre: vertex1 and vertex2 are valid
        input: two vertices
        out: True if there is an edge between the vertices
        """
        return (vertex1, vertex2) in self.dcosts.keys()

    def out_degree(self, vertex):
        """
        pre: vertex is valid
        input: vertex
        out: the outbound degree of the given vertex
        """
        if self.check_vertex_validity(vertex) == False:
            raise ValueError("Invalid vertex")
        return self.dout[vertex]

    def in_degree(self, vertex):
        """
        pre: vertex is valid
        input: vertex
        out: the inbound degree of the given vertex
        """
        if self.check_vertex_validity(vertex) == False:
            raise ValueError("Invalid vertex")
        return self.din[vertex]

    def out_vertices(self, vertex):
        """
        pre: vertex is valid
        input: vertex
        out: the outbound vertices of the given vertex
        """
        if self.check_vertex_validity(vertex) == False:
            raise ValueError("Invalid vertex")
        return list(self.dout[vertex])[:]

    def in_vertices(self, vertex):
        """
        pre: vertex is valid
        input: vertex
        out: the inbound vertices of the given vertex
        """
        if self.check_vertex_validity(vertex) == False:
            raise ValueError("Invalid vertex")
        return list(self.din[vertex])[:]

    def copy_Graph(self):
        """
        out: Returns a copy of the graph
        """
        return Directed_Graph(self.graph)

    def __str__(self):
        res = ""
        for i in self.dcosts.keys():
            res += str(i[0]) + " " + str(i[1]) + " " + str(self.dcosts[i]) + "\n"
        return res

    @property
    def Number_of_vertices(self):
        """
        Returns the number of vertices
        """
        return self.num_vertices

    @property
    def Number_of_edges(self):
        """
        Returns the number of edges
        """
        return self.num_edges

    @property
    def Vertices(self):
        """
        out: the list of vertices
        """
        return list(self.dout.keys())[:]

    def reverseList(self, aList):
        result = []
        length = len(aList)
        for i in range(length):
            i = i
            result.append(aList.pop())
        return result

    def Floyd_Warshall(self, startV, endV):
        """
            Calculates the lowest lenght path between all vertices accesible from one another and
            also stores their parents so we can reconstruct the path.
            Returns the matrices distances and parents, and also the path between the starting vertex and the final vertex 
        """
        n = self.Number_of_vertices
        distances = [[-1 for i in range(n)] for j in range(n)]
        parents = [[-1 for i in range(n)] for j in range(n)]

        # m = distances
        # for l in m:
        #     for e in l:
        #        print(e, end=' ')
        #     print()
        # print()

        for i in range(n):
            for j in range(n):
                if i == j:
                    distances[i][j] = 0
                    parents[i][j] = -1
                elif (i, j) in self.dcosts.keys():
                    distances[i][j] = self.dcosts[(i, j)]
                    parents[i][j] = i
                else:
                    distances[i][j] = inf
                    parents[i][j] = -1

        # print_matrix(distances)
        # print_matrix(parents)
        # print(distances , '\n\n', parents, '\n')

        for k in range(n):
            for i in range(n):
                # print(k,i)
                for j in range(n):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
                        parents[i][j] = parents[k][j]

                        # print(distances , '\n\n', parents, '\n')

            # print_matrix(distances)
            # print_matrix(parents)
            # print("-" * 25)

        u = endV
        path = [u]
        while u != startV:
            u = parents[startV][u]
            path.append(u)

        # reversing the path to normal
        path = self.reverseList(path)
        
        return distances, parents, path

    def shortest_path_bfs(self, vertex1, vertex2):
        """
            pre: vertex1 and vertex2 are valid
            input: vertex1, vertex2
            out: the shortest path between vertex1 and vertex2 using breath-first-search
        """
        if not self.check_vertex_validity(vertex1):
            raise ValueError("Vertex 1 doesn't exist")
        if not self.check_vertex_validity(vertex2):
            raise ValueError("Vertex 2 doesn't exist")

        # BFS starts here

        parents = {}
        visited = set()
        queue = [vertex1]
        visited.add(vertex1)
        parents[vertex1] = vertex1
        while len(queue):
            currentVertex = queue[0]
            queue = queue[1:]
            for nextVertex in self.out_vertices(currentVertex):
                if nextVertex not in visited:
                    visited.add(nextVertex)
                    parents[nextVertex] = currentVertex
                    queue.append(nextVertex)
            if vertex2 in visited:
                break
        if vertex2 not in parents:
            raise ValueError("Path not found!")
        parent = parents[vertex2]
        # print(parent)
        path = [vertex2, parent]
        while parent != vertex1:
            parent = parents[parent]
            path.append(parent)

        # reversing the path to normal
        path = self.reverseList(path)

        return path


def print_matrix(m):
    # for l in m:
    #     for e in l:
    #         print(e, end=' ')
    #     print()
    # print()
    print(np.matrix(m))
    print()
