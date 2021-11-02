from typing import List, Optional, Union


class Node(object):

    def __init__(self, val:Union[int,str] = None, neighbors:List[Node] = None) -> None:
        super().__init__()
        self.val = val
        self.neighbors = neighbors


    def __get_val(self):
        return self.val 



class binaryTreeNode(Node):

    def __init__(self, val:int = None, left:binaryTreeNode = None, right:binaryTreeNode = None):
        super().__init__(val) 
        self.left = left 
        self.right = right 



class Tries(Node):

    def __init__(self) -> None:
        super().__init__("-")



    def __add(self, word:str):
        current_node = self
        neighbors = current_node.neighbors
        for char in word:
            current_node = current_node.__getNeighbor(char)
            if current_node == None:
                new_node = Tries(char)
                neighbors.append(new_node)
                current_node = new_node
            
            neighbors = current_node.neighbors

            


    def __getNeighbor(self, char:str):
        for neighbor in self.neighbors:
            if neighbor.val == char:
                return neighbor 
        return None 




class Heap(object):
    pass

