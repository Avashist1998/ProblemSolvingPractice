"""LC: 108. Convert Sorted Array to Binary Search Tree"""
from typing import List

class Node:
	def __init__(self, val: int):
		self.val = val
		self.left = None
		self.right = None


def sortedArrayToBST(arr: List[int]):

	if len(arr) == 0:
		return None
	if len(arr) == 1:
		return Node(arr[0])
	
	l, r = 0, len(arr)
	res = []
	mid = (r-l)//2 + l
	root = Node(arr[mid])
	queue = [[l, mid, root, "l"], [mid+1, r, root, "r"]]

	while queue:
		l, r, node, dir = queue.pop(0)
		if r-l == 0:
			pass
		else:
			mid = (r-l)//2 + l
			if dir == "l":
				node.left = Node(arr[mid])
				queue.append([l, mid, node.left, "l"])
				queue.append([mid+1, r, node.left, "r"])
			else:
				node.right = Node(arr[mid])
				queue.append([l, mid, node.right, "l"])
				queue.append([mid+1, r, node.right, "r"])
	return root
		
