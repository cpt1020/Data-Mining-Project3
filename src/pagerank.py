from src.utils import write_file, one_norm
from time import time
import numpy as np

def pagerank(file_name, adj_matrix, vertex_size, damping_factor, max_iteration, epsilon):

    # starting time
    time_start = time()

    # initialize the page rank of each vertex to (1/vertex_size)
    page_rank = [(1/vertex_size) for x in range(vertex_size)]

    # record the out-degree of each vertex
    outdegree_list = []
    for i in range(vertex_size):
        sum = 0
        for j in range(vertex_size):
            sum += adj_matrix[i][j]
        outdegree_list.append(sum)

    # record the parent of each vertex
    parent_list = []
    for i in range(vertex_size):
        parent = []
        for j in range(vertex_size):
            if adj_matrix[j][i] == 1:
                parent.append(j)
        if len(parent) == 0:
            parent_list.append([-1])
        else:
            parent_list.append(parent)

    iteration = 1
    while True:
        
        prev_page_rank = page_rank.copy()

        for i in range(vertex_size):
        # update the page rank of node i
            new_page_rank_sum = 0

            # find the parent of node i
            for j in parent_list[i]:
                if j != -1:
                    new_page_rank_sum += (prev_page_rank[j]/outdegree_list[j])
            page_rank[i] = ((damping_factor/vertex_size) + (1-damping_factor)*new_page_rank_sum)

        page_rank = one_norm(page_rank, vertex_size)

        # 依照threshold或Max iteration決定是否break
        if iteration >= max_iteration or np.allclose(prev_page_rank, page_rank, atol = epsilon):
            break
        else:
            iteration += 1

        # 僅依照max iterattion決定是否break
        # if iteration >= max_iteration:
        #     break
        # else:
        #     iteration += 1

    # ending time
    time_end = time()
    print(f"PageRank Execution Time: {round(time_end - time_start, 5)}")
    print(f"PageRank iteration to converge: {iteration}")

    # write result as txt
    file_name = file_name.strip(".txt").strip("input/")
    write_file(f'results/{file_name}/{file_name}_PageRank.txt', page_rank)
