f = open('input4.txt', 'r')
f1 = open('output4.txt', 'w')

n, m = map(int, f.readline().split())
roads = [list(map(int, f.readline().split())) for i in range(m)]

def find(parent, i):
    if parent[i] == -1:
        return i
    return find(parent, parent[i])

def union(parent, i, j):
    parent[find(parent, i)] = find(parent, j)

def minimum_cost(n, roads):
    parent = [-1] * n
    total_cost = 0
    roads.sort(key=lambda x: x[2])
    for road in roads:
        u, v, w = road
        if find(parent, u-1) != find(parent, v-1):
            total_cost += w
            union(parent, u-1, v-1)
    return total_cost

print(minimum_cost(n, roads), file=f1)

f.close()
f1.close()