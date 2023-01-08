import numpy as np

def is_in_list(list, num):
    for elem in list:
        if num == elem:
            return True
    return False

'''read file & record vertex information'''
def read_file(file_name):
    from_node = []      # 存放edge起始點
    to_node = []        # 存放edge終點
    node_set = set()    # 用來記錄總共有多少vertex
    vertex_size = 0

    if file_name.find('ibm') != -1:
        with open(file_name) as f:
            vertex_list = []
            for i in f.readlines():
                i = [int(x) for x in i.split()]
                if is_in_list(vertex_list, i[0]) == False:
                    vertex_list.append(i[0])
                if is_in_list(vertex_list, i[2]) == False:
                    vertex_list.append(i[2])
            vertex_list.sort()
            vertex_size = len(vertex_list)
        
        with open(file_name) as f:
            for i in f.readlines():
                i = [int(x) for x in i.split()]
                from_node.append(vertex_list.index(i[0])+1)
                to_node.append(vertex_list.index(i[2])+1)
    else:
        with open(file_name) as f:
        # 用with open就不用呼叫close()
            for i in f.readlines():
                data = i.split(',')
                node1 = data[0]
                node2 = data[1].split('\n')[0]
                from_node.append(node1)
                to_node.append(node2)
                node_set.add(node1)
                node_set.add(node2)
        vertex_size = len(node_set)

    print(f"number of vertex: {vertex_size}")
    print(f"number of edge: {len(from_node)}")
    
    return from_node, to_node, vertex_size

'''store graph in adjacency matrix'''
def construct_adj_matrix(from_node, to_node, vertex_size):
    
    # create adjacency matrix and initialize all the value to 0
    adj_matrix = [[0 for x in range(vertex_size)] for y in range(vertex_size)]

    # 將adjacency matrix的edge設定成1
    for i in range(len(from_node)):
        adj_matrix[int(from_node[i])-1][int(to_node[i])-1] = 1

    return adj_matrix

'''write file'''
# def write_file(file_name, output):
#     f = open(file_name, "w")
#     f.write(output)
#     f.close()
def write_file(file_name, output):
    np.savetxt(file_name, output, fmt='%.3f', newline=' ')

# 1-norm normalization
def one_norm(list, vertex_size):
    sum = 0
    for i in range(vertex_size):
        sum += list[i]
    if sum != 0:
        for i in range(vertex_size):
            list[i] = list[i]/sum
    return list
