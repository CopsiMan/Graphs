# TO-DO implement the 3 representations and test the rrun time for 1000, 100000, etc

from timeit import default_timer as timer
from texttable import Texttable
import time

from Directed_Graph import Directed_Graph
from Directed_Graph_Only_Outbound import Directed_Graph_Only_Outbound
from Graph_Matrix import Graph_Matrix
from main import UI, read_input, generate_graph, main_start


def start_timing():

    # Time needed for both collections, inbound and outbound
    # print("Graph with inbound and outbound representation : ")
    # test_graph_1k_inbound_and_outbound()
    # test_graph_10k_inbound_and_outbound()
    # test_graph_100k_inbound_and_outbound()
    # # test_graph_1kk_inbound_and_outbound()
    # print("Graph with only outbound representation : ")
    # test_graph_1k_inbound()
    # test_graph_10k_inbound()
    # test_graph_100k_inbound()
    print("Graph with adjacency matrix : ")
    test_graph_1k_matrix()
    test_graph_10k_matrix()
    test_graph_100k_matrix()
    # test_graph_1kk_matrix()
    # vertices_number = 100
    # graph_list = generate_graph(vertices_number, vertices_number * 10)


def test_graph_1k_matrix():
    file_name = "seminar_graph1k.txt"
    directed_graph = Graph_Matrix(file_name)
    # directed_graph.print_matrix()

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 1k vertices:", time_end - time_start)


def test_graph_10k_matrix():
    file_name = "seminar_graph10k.txt"
    directed_graph = Graph_Matrix(file_name)
    # directed_graph.print_matrix()

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 10k vertices:", time_end - time_start)


def test_graph_100k_matrix():
    file_name = "seminar_graph100k.txt"
    directed_graph = Graph_Matrix(file_name)
    # directed_graph.print_matrix()

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 100k vertices:", time_end - time_start)


def test_graph_1k_inbound():
    file_name = "seminar_graph1k.txt"
    directed_graph = Directed_Graph_Only_Outbound(file_name)

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 1k vertices:", time_end - time_start)


def test_graph_10k_inbound():
    file_name = "seminar_graph10k.txt"
    directed_graph = Directed_Graph_Only_Outbound(file_name)

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 10k vertices:", time_end - time_start)


def test_graph_100k_inbound():
    file_name = "seminar_graph100k.txt"
    directed_graph = Directed_Graph_Only_Outbound(file_name)

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 100k vertices:", time_end - time_start)


def test_graph_1kk_inbound():
    file_name = "seminar_graph1kk.txt"
    directed_graph = Directed_Graph_Only_Outbound(file_name)

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 1kk vertices:", time_end - time_start)


def test_graph_1k_inbound_and_outbound():
    file_name = "seminar_graph1k.txt"
    graph_list = read_input(file_name)
    directed_graph = Directed_Graph(graph_list)

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 1k vertices:", time_end - time_start)


def test_graph_10k_inbound_and_outbound():
    file_name = "seminar_graph10k.txt"
    graph_list = read_input(file_name)
    directed_graph = Directed_Graph(graph_list)

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 10k vertices:", time_end - time_start)


def test_graph_100k_inbound_and_outbound():
    file_name = "seminar_graph100k.txt"
    graph_list = read_input(file_name)
    directed_graph = Directed_Graph(graph_list)

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 100k vertices:", time_end - time_start)


def test_graph_1kk_inbound_and_outbound():
    file_name = "seminar_graph1kk.txt"
    graph_list = read_input(file_name)
    directed_graph = Directed_Graph(graph_list)

    time_start = timer()

    for vertex in directed_graph.Vertices:
        directed_graph.out_vertices(vertex)
        directed_graph.in_vertices(vertex)
        # print(directed_graph.out_vertices(vertex))
        # print(directed_graph.in_vertices(vertex))

    # time.sleep(3)

    time_end = timer()

    print("Time for 1kk vertices:", time_end - time_start)


start_timing()
