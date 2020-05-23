from main import read_input,generate_graph_v2
from Directed_Graph import Directed_Graph, print_matrix


def print_path(path):
    for i in range(len(path)):
        if i < len(path) - 1:
            print(path[i], end=" -> ")
        else:
            print(path[i])


def test_BFS():
    input_file = "graph10k.txt"
    graph = Directed_Graph(read_input(input_file))
    print_path(graph.shortest_path_bfs(4, 3))
    try:
        print(graph.shortest_path_bfs(4, 10000))
    except ValueError as va:
        print(va)


def test_Floyd_Warshall():
    graph = Directed_Graph(generate_graph_v2(10,15))
    # graph = Directed_Graph(read_input("graph1k.txt"))
    print(graph)
    d , p = graph.Floyd_Warshall()
    print_matrix(d)
    print_matrix(p)

    # graph = Directed_Graph(read_input("example_graph.txt"))
    # print(graph)
    # d , p = graph.Floyd_Warshall()
    # print_matrix(d)
    # print_matrix(p)

# test_BFS()
test_Floyd_Warshall()