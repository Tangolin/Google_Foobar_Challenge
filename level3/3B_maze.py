from collections import deque
import time


class mapnode:
    def __init__(self, coord, dist, chance=1):
        self.c = coord
        self.d = dist
        self.chance = chance


def BFS(map):
    n_row = len(map)
    n_col = len(map[0])
    visited = [[0] * n_col for _ in range(n_row)]

    q = deque()
    q.append(mapnode((0,0), 1))

    while q:
        cur = q.popleft()
        visited[cur.c[0]][cur.c[1]] == 1

        if cur.c == (n_row-1, n_col-1):
            return cur.d
        
        else:
            for neighbour in find_n(cur.c, n_row, n_col):
                validity = is_valid(neighbour, visited, map, cur.chance)
                if validity == 1:
                    q.append(mapnode(neighbour, cur.d + 1))
                elif validity == 2:
                    q.append(mapnode(neighbour, cur.d + 1, 0))
        
    return -1


def is_valid(n, visited, map, chance):
    if visited[n[0]][n[1]] != 1 and map[n[0]][n[1]] != 1:
        return 1
    if visited[n[0]][n[1]] != 1 and map[n[0]][n[1]] == 1 and chance == 1:
        return 2
    return 0


def find_n(coord, n_row, n_col):
    x, y = coord[0], coord[1]
    c = [(x+i, y) for i in range(-1,2)] + [(x, y+i) for i in range(-1, 2)]
    n = []
    for item in c:
        if n_row-1 >= item[0] >= 0 and n_col-1 >= item[1] >= 0 and item != (x,y):
            n.append(item)
    
    return n


def solution(map):
    coords = [(i, j) for i in range(len(map)) for j in range(len(map[0])) if map[i][j] == 1]
    shortest = DJK(map)

    for coord in coords:
        map[coord[0]][coord[1]] = 0
        s = DJK(map)
        if s <= shortest:
            shortest = s
        map[coord[0]][coord[1]] = 1
    
    return shortest


def DJK(map):
    n_row = len(map)
    n_col = len(map[0])
    visited = [[0] * n_col for _ in range(n_row)]
    d = [[float('inf')] * n_col for _ in range(n_row)]
    q = [float('inf')] * (n_col * n_row)

    d[0][0] = 1
    q[0] = 1

    while True:
        if min(q) == float('inf'):
            return float('inf')
        min_idx = q.index(min(q))
        cur_node = (min_idx // n_col, min_idx % n_col)
        visited[cur_node[0]][cur_node[1]] = 1
        q[min_idx] = float('inf')

        if cur_node == (n_row-1, n_col-1):
            return d[cur_node[0]][cur_node[1]]
    
        else:
            for neighbour in find_n(cur_node, n_row, n_col):
                if dijk_is_valid(neighbour, visited, map):
                    if d[cur_node[0]][cur_node[1]] + 1 < d[neighbour[0]][neighbour[1]]:
                        d[neighbour[0]][neighbour[1]] = d[cur_node[0]][cur_node[1]] + 1
                        q[neighbour[0] * n_col + neighbour[1]] = d[cur_node[0]][cur_node[1]] + 1


def dijk_is_valid(n, visited, map):
    if visited[n[0]][n[1]] != 1 and map[n[0]][n[1]] != 1:
        return True
    return False


if __name__ == '__main__':
    map1 = [[0, 1, 1, 0], 
            [0, 0, 0, 1], 
            [0, 1, 0, 0], 
            [0, 0, 0, 0]]

    map2 = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
    cur_time = time.time()
    print("Dijkstra")
    print(solution(map1))
    print(solution(map2))
    print('Time taken is ', time.time() - cur_time)
    cur_time = time.time()
    print('BFS')
    print(BFS(map1))
    print(BFS(map2))
    print('Time taken is ', time.time() - cur_time)
    