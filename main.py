from src.utils import read_file, construct_adj_matrix
from src.hits import hits01, hits02
from src.pagerank import pagerank
from src.simrank import simrank, simrank02

def main():

    '''Parameters Setting'''
    epsilon = 1e-10         # threshold for convergence
    max_iteration = 30
    damping_factor = 0.1
    decay_factor = 0.7

    '''Read Graph & Record Its Nodes and Edges'''
    # file_name = 'input/ibm-5000.txt'
    file_name = 'input/graph_1.txt'
    print(f"--------------------File: {file_name}--------------------")
    from_node, to_node, vertex_size = read_file(file_name)
    
    '''Construct Adjacency Matrix'''
    adj_matrix = construct_adj_matrix(from_node, to_node, vertex_size)

    '''Execute HITS'''
    print("\nHITS----------------------------------------")
    hits01(adj_matrix, vertex_size, epsilon, max_iteration, file_name)
    hits02(adj_matrix, vertex_size, epsilon, max_iteration, file_name)
    # hits02 is a faster implementation of HITS comparing to hits01
    # for more information, please refer to p.29 of my report

    '''Execute PageRank'''
    print("\nPageRank----------------------------------------")
    pagerank(file_name, adj_matrix, vertex_size, damping_factor, max_iteration, epsilon)

    '''Execute SimRank'''
    print("\nSimRank----------------------------------------")
    simrank(adj_matrix, vertex_size, decay_factor, max_iteration, file_name, epsilon)


if __name__ == '__main__':
    main()