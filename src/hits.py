import numpy as np  # for matrix multiplication
from src.utils import write_file, one_norm
from time import time

def hits01(adj_matrix, vertex_size, epsilon, max_iteration, file_name):
    
    print(f"HITS01----------------------------------")

    # starting time
    time_start = time()

    # initialize hub and authority of each node as 1
    hub = [1 for x in range(vertex_size)]
    authority = [1 for x in range(vertex_size)]

    transpose = [[adj_matrix[j][i] for j in range(len(adj_matrix))] for i in range(len(adj_matrix[0]))]

    iteration = 1
    while True:
        prev_hub = hub.copy()
        prev_authority = authority.copy()
        
        # updated authority
        authority = np.dot(transpose, prev_hub)
        authority = authority.astype(float)

        # updated hub
        hub = np.dot(adj_matrix, prev_authority)
        hub = hub.astype(float)

        # normalization
        authority = one_norm(authority, vertex_size)
        hub = one_norm(hub, vertex_size)

        # # break while loop depending on max iteration
        # if iteration >= max_iteration:
        #     break
        # else:
        #     iteration += 1
        
        # 計算差值
        diff = 0
        for i in range(vertex_size):
            diff += abs(authority[i] - prev_authority[i])
            diff += abs(hub[i] - prev_hub[i])

        # break while loop depending on convergence threshold or max iteration
        if diff < epsilon or iteration >= max_iteration:
            break
        else:
            iteration += 1

    # ending time
    time_end = time()
    print(f"HITS Execution Time: {round(time_end - time_start, 5)}")
    print(f"HITS iteration to converge: {iteration}")

    # write result as txt
    file_name = file_name.strip(".txt").strip("input/")
    write_file(f'results/{file_name}', f'results/{file_name}/{file_name}_HITS_authority.txt', authority)
    write_file(f'results/{file_name}', f'results/{file_name}/{file_name}_HITS_hub.txt', hub)

def hits02(adj_matrix, vertex_size, epsilon, max_iteration, file_name):
    
    print(f"HITS02----------------------------------")

    # starting time
    time_start = time()

    # initialize hub and authority of each node as 1
    hub = [1 for x in range(vertex_size)]
    authority = [1 for x in range(vertex_size)]

    # record the parent/children of each node
    parent_list = []
    children_list = []
    for i in range(vertex_size):
        parent = []
        children = []

        for j in range(vertex_size):
            if adj_matrix[j][i] == 1:
                parent.append(j)
            if adj_matrix[i][j] == 1:
                children.append(j)

        if len(parent) == 0:
            # if the node has no parent, append -1 to parent_list
            parent_list.append([-1])
        else:
            parent_list.append(parent)

        if len(children) == 0:
            children_list.append([-1])
        else:
            children_list.append(children)     

    iteration = 1
    while True:

        prev_authority = authority.copy()
        prev_hub = hub.copy()
        
        for i in range(vertex_size):
            # 計算authority
            if parent_list[i][0] != -1:
                # 若node i有parent
                new_auth = 0
                for j in parent_list[i]:
                    # 把node i的每個parent j前一輪的hub值加總起來
                    new_auth += prev_hub[j]
                authority[i] = new_auth
            else:
                # 若node i沒有parent，就直接0
                authority[i] = 0
            
            # 計算hub
            if children_list[i][0] != -1:
                new_hub = 0
                for j in children_list[i]:
                    new_hub += prev_authority[j]
                hub[i] = new_hub
            else:
                hub[i] = 0

        # normalization
        authority = one_norm(authority, vertex_size)
        hub = one_norm(hub, vertex_size)
        
        # break while loop depending on max iteration
        # if iteration >= max_iteration:
        #     break
        # else:
        #     iteration += 1
        
        # 計算差值
        diff = 0
        for i in range(vertex_size):
            diff += abs(authority[i] - prev_authority[i])
            diff += abs(hub[i] - prev_hub[i])

        # break while loop depending on convergence threshold or max iteration
        if diff < epsilon or iteration >= max_iteration:
            break
        else:
            iteration += 1

    # ending time
    time_end = time()
    print(f"HITS Execution Time: {round(time_end - time_start, 5)}")
    print(f"HITS iteration to converge: {iteration}")

    # write result as txt
    file_name = file_name.strip(".txt").strip("input")
    write_file(f'results/{file_name}', f'results/{file_name}/{file_name}_HITS02_authority.txt', authority)
    write_file(f'results/{file_name}', f'results/{file_name}/{file_name}_HITS02_hub.txt', hub)