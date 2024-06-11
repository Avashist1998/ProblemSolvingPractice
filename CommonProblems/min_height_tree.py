# LC 310

"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

## Example 1 

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

## Example 2

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

"""
from typing import List

def base_test_case_1():
    n = 4 
    edges = [[1,0],[1,2],[1,3]]
    exp_res = [1]

    res = findMinHeightTrees(n, edges)

    assert len(res) == len(exp_res)
    assert res[0] == exp_res[0]

def base_test_case_2():
    n = 6 
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    exp_res = [3, 4]

    res = findMinHeightTrees(n, edges)

    assert len(res) == len(exp_res)
    assert res[0] == exp_res[0]
    assert res[1] == exp_res[1]


def base_test_case_3():
    n = 6 
    edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
    exp_res = [3]

    res = findMinHeightTrees(n, edges)

    assert len(res) == len(exp_res)
    assert res[0] == exp_res[0]


def findMinHeightTrees(n: int, edges: List[int]) -> List[int]:
    """Finds the the node of the graph that create a tree of min height.
    
    Args:
        n: number of nodes
        edges: array of edge in the graph
    Returns:
        A list of nodes that will be the root of the tree with min height.
    """


    if n <= 2:
        return [i for i in range(n)]

    graph = {i: set() for i in range(n)}
    edge_count = {i: 0 for i in range(n)}
    for edge in edges:
        l, r = edge
        edge_count[l] += 1
        edge_count[r] += 1
        graph[l].add(r)
        graph[r].add(l)


    queue = []

    for node in edge_count:

        if edge_count[node] == 1:
            queue.append(node)
    

    while len(queue):
        
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            if list(graph[node])[0] in graph:
                graph[list(graph[node])[0]].remove(node)
                edge_count[list(graph[node])[0]] -= 1
                if edge_count[list(graph[node])[0]]  == 1:
                    queue.append(list(graph[node])[0])
            graph.pop(node)
            edge_count.pop(node)
        if len(graph) <= 2:
            break
    return queue


base_test_case_1()
base_test_case_2()
base_test_case_3()
