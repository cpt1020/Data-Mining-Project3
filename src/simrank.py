from src.utils import write_file
import numpy as np
from time import time
import os

def simrank(adj_matrix, vertex_size, decay_factor, max_iteration, file_name, epsilon):

    # starting time
    time_start = time()

    # initialize sim to 0
    sim = [[0 for x in range(vertex_size)] for y in range(vertex_size)]
    
    # initialize sim(i,i) to 1
    for i in range(vertex_size):
        sim[i][i] = 1

    # record the number in-neighbor of each node
    in_neighbors_num = []
    for i in range(vertex_size):
        sum = 0
        for j in range(vertex_size):
            sum += adj_matrix[j][i]
        in_neighbors_num.append(sum)

    # record the in-neighbor of each node
    in_neighbor = []
    for i in range(vertex_size):
        parent = []
        for j in range(vertex_size):
            if adj_matrix[j][i] == 1:
                parent.append(j)
        in_neighbor.append(parent)

    iteration = 1
    while True:

        # copy the Sim from previous iteration as last_sim
        last_sim = []
        for list in sim:
            copy = list.copy()
            last_sim.append(copy)

        for i in range(vertex_size):
            for j in range(vertex_size):
                if i != j:

                    sim_sum = 0

                    if in_neighbors_num[i] != 0 and in_neighbors_num[j] != 0:
                    # if node i has parent AND node j has parent as well

                        for k in in_neighbor[i]:
                        # parent k of node i

                            for l in in_neighbor[j]:
                            # parent l of node j

                                # use Sim from last iteration to accumulate Sim(k,l)
                                sim_sum += last_sim[k][l]
                        
                        # update Sim(i,j) by formulat
                        sim[i][j] = (decay_factor/(in_neighbors_num[i]*in_neighbors_num[j])) * sim_sum
                
                else:
                    # Sim(i,i)=1
                    sim[i][j] = 1

        # break while loop depending on convergence threshold or max iteration
        if iteration >= max_iteration or np.allclose(last_sim, sim, atol= epsilon):
            break
        else:
            iteration += 1

        # # break while loop depending on max iteration
        # if iteration >= max_iteration:
        #     break
        # else:
        #     iteration += 1

    # ending time
    time_end = time()
    print(f"SimRank Execution Time: {round(time_end - time_start, 5)}")

    # iteration that reach convergence
    print(f"SimRank iteration to converge: {iteration}")

    # write result as txt
    file_name = file_name.strip(".txt").strip("input/")
    os.makedirs(f'results/{file_name}', exist_ok=True)
    np.savetxt(f'results/{file_name}/{file_name}_SimRank.txt', sim, fmt='%.6f', newline='\n')

    # write result as csv
    # np.savetxt(f'{file_name}_SimRank_csv.csv', sim, fmt='%f', delimiter = ",", newline='\n')

def simrank02(adj_matrix, vertex_size, decay_factor, max_iteration, file_name, epsilon):

    # 紀錄起始時間
    time_start = time()

    # 先初始化sim
    sim = [[0 for x in range(vertex_size)] for y in range(vertex_size)]
    
    # 將sim的對角線初始化成1
    for i in range(vertex_size):
        sim[i][i] = 1

    # 記錄每個點的in-neighbors數量
    in_neighbors_num = []
    for i in range(vertex_size):
        sum = 0
        for j in range(vertex_size):
            sum += adj_matrix[j][i]
        in_neighbors_num.append(sum)

    # 記錄每個點的in neighbor有誰
    in_neighbor = []
    for i in range(vertex_size):
        # 開始記錄node i的parent有誰
        parent = []
        for j in range(vertex_size):
            if adj_matrix[j][i] == 1:
                parent.append(j)
        
        if len(parent) == 0:
            # 若該node沒有parent，則存[-1]
            in_neighbor.append([-1])
        else:
            in_neighbor.append(parent)

    iteration = 1
    while True:
        last_sim = []
        for list in sim:
            copy = list.copy()
            last_sim.append(copy)

        for i in range(vertex_size):
            for j in range(vertex_size):
                if i != j:
                    sim_sum = 0
                    if in_neighbors_num[i] != 0 and in_neighbors_num[j] != 0:
                    # 若i有parent，j也有parent
                        # if in_neighbor[i][0] != -1 and in_neighbor[j][0] != -1:
                        for k in in_neighbor[i]:
                        # i的每個parent k
                            for l in in_neighbor[j]:
                            # j的每個parent l
                                sim_sum += last_sim[k][l]
                        sim[i][j] = (decay_factor/(in_neighbors_num[i]*in_neighbors_num[j])) * sim_sum
                else:
                    sim[i][j] = 1

        # 依據max iteration和threshold決定是否break
        # if iteration >= max_iteration or np.allclose(last_sim, sim, atol= epsilon):
        #     break
        # else:
        #     iteration += 1

        # 依據max iteration決定是否break
        if iteration >= max_iteration:
            break
        else:
            iteration += 1

    # 結束時間
    time_end = time()
    print(f"SimRank Execution Time: {round(time_end - time_start, 5)}")

    # 印出收斂的iteration
    print(f"SimRank iteration to converge: {iteration}")

    # 將結果寫入txt
    file_name = file_name.strip(".txt")
    os.makedirs(f'results/{file_name}', exist_ok=True)
    np.savetxt(f'{file_name}_SimRank02.txt', sim, fmt='%.3f', newline='\n')


