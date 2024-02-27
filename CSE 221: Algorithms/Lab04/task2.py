# Task 2
file_in = 'input2.txt'
with open(file_in, 'r') as file:
    lines = file.readlines()
    vertices, edges = lines[0].split(' ')    
    #print(f"Vertices: {vertices}, Edges: {edges}")    

edges = [tuple(map(int, i.strip().split())) for i in lines[1:]]
#print(edges)

def adjacencyList(edges):
    adj_list = {}
    for edge in edges:
        u, v = edge
        adj_list.setdefault(u, []).append(v)
        adj_list.setdefault(v, []).append(u)
        
    #print(adj_list)
    return adj_list

graph = adjacencyList(edges)
visited = [False for i in range(int(vertices) + 1)]
result = []

def BFS(G, s):
    queue = [s]
    visited[s] = True
    while len(queue) > 0:
        u = queue.pop(0)
        #print(u, end=" ")        
        result.append(u) 
        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True          

BFS(graph, 1)

file_out = 'output2.txt'
with open(file_out, 'w') as file:
    for i in result:
        file.write(str(i) + " ")