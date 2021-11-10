from typing import List
from Node import Node


# Given
# tasks array of char or string
# dependecies is  list of tuples pairs


class node(Node):

    def __init__(self, val: str = None):
        super().__init__(val, [])
        self.visited = False
        self.parent_count = 0


def visted(n: node, queue: list) -> None:
    n.visited = True
    for child in n.neighbors:
        child.parent_count -= 1
        if child.parent_count == 0:
            queue.append(child)


def buildOrder(tasks: str, dependencies: List) -> str:

    if len(dependencies) == 0:
        return tasks

    res = ""

    graph = dict()
    # value => Node
    for i in range(len(tasks)):
        graph[tasks[i]] = node(tasks[i])

    for i in range(len(dependencies)):
        parent, child = dependencies[i]
        parent_node = graph[parent]
        child_node = graph[child]
        parent_node.neighbors.append(child_node)
        child_node.parent_count += 1
        graph[parent] = parent_node
        graph[child] = child_node

    queue = list()

    for task in graph:
        if graph[task].parent_count == 0:
            queue.append(graph[task])

    while(len(queue) != 0):

        walker = queue.pop(0)

        if not walker.visited:
            visted(walker, queue)
            res += walker.val

        else:
            return ""

    if len(res) != len(tasks):
        return ""

    return res

# Time complexity
# O(n+m)
# n : number of nodes
# m : number of average dependances

# Space complexity

# O(n*m)
# n : number of nodes
# m : number of average connection in of the graph


# Test case 1
# tasks: PMLK
# dependencies : [(P,M), (L, K)]
# build output should be
# PMLK, PLMK, PLKM, LPKM, LPMK


tests = [["PMLK", [("P", "M"), ("L", "K")]], ["PMLK", [("P", "M"), ("M", "L"), ("L", "K")]], [
    "PMLK", []], ["PMLK", [("P", "M"), ("M", "P")]]]


for test in tests:

    task, dependencies = test

    output = buildOrder(task, dependencies)

    print("Test result ", output)
