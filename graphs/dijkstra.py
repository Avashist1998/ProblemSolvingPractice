from typing import Tuple, Dict, Set


def get_min_distance(n: int, start: int, end: int, edges: Tuple[int, int, int]):
    """
    """

    graph = {}
    for edge in edges:
        a, b, cost = edge
        if a in graph:
            graph[a][b] = cost
        else:
            graph[a] = {b: cost}


    cost = {}
    parent = {}
    visited = set()

    for i in range(n):
        if i == start:
            cost[i] = 0
        else:
            cost[i] = float("inf")
    
    def get_lower_cost_node(cost: Dict[int, float], visited: Set):
        res = -1
        min_val = float("inf")
        for node in cost.keys():
            if min_val > cost[node] and node not in visited:
                res = node
                min_val = cost[node]
        return res
    

    node = get_lower_cost_node(cost, visited)

    while node is not -1:
        node_cost = cost[node]
        neighbor = graph[node]

        for n in neighbor.keys():
            new_cost = node_cost + neighbor[n]
            if new_cost < cost[n]:
                cost[n] = new_cost
                parent[n] = node
        visited.add(node)
        node = get_lower_cost_node(cost, visited)
