
Graph_nodes = {
    'A': [('B', 1), ('I', 4)], 'B': [('C', 1), ('F', 2)], 'C': [('D', 1)],
    'D': [('E', 1)], 'E': [('L', 3)], 'F': [('G', 1)], 'G': [('F', 1)],
    'H': [('K', 1)], 'I': [('O', 2), ('J', 1)], 'J': [('M', 1), ('K', 1)],
    'K': [('L', 1)], 'L': [('N', 1)], 'M': [('N', 2 ), ('P', 1)],
    'N': [('S', 1)], 'O': [('P', 1), ('Q', 1)], 'P': [('M', 1), ('O', 1)],
    'Q': [('O', 1), ('R', 1)], 'R': [('Q', 2), ('S', 1)], 'S': [('N', 2), ('R', 2)]
}
def AStar_algorithm(start_node, stop_node):
    open_set =set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    #finding the adjacent node with the lowest f(n) value
    while len(open_set) > 0:
        n = None

        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            open_set.remove(n)
            closed_set.add(n)

            for(m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path doesnt exist')
            return None

        if n == stop_node:
            path = []

            while parents[n] !=n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()

            print('Path found: {}'.format(path))
            return path

    print('Path doesnt exist')
    return None




def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):   #Manhattan heuristics
    H_dist = {   # A -> S
        'A': 10,
        'B': 9,
        'C': 8,
        'D': 7,
        'E': 6,
        'F': 7,
        'G': 6,
        'H': 5,
        'I': 6,
        'J': 5,
        'K': 4,
        'L': 3,
        'M': 4,
        'N': 2,
        'O': 4,
        'P': 3,
        'Q': 3,
        'R': 2,
        'S': 0
    }

    H_dist_D_0 = {  # D->O
        'A': 6,
        'B': 7,
        'C': 8,
        'D': 7,
        'E': 8,
        'F': 5,
        'G': 6,
        'H': 5,
        'I': 2,
        'J': 3,
        'K': 4,
        'L': 5,
        'M': 2,
        'N': 4,
        'O': 0,
        'P': 1,
        'Q': 1,
        'R': 2,
        'S': 4
    }
    return H_dist[n]


if __name__ == '__main__':
    AStar_algorithm('A', 'S')




