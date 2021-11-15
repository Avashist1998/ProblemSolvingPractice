from Type import Optional
from Graphs import binaryTreeNode



def isSubtree(tree_1:Optional[binaryTreeNode], tree_2:Optional[binaryTreeNode]) -> bool:

    
    def check_same_tree(tree_1:Optional[binaryTreeNode], tree_2:Optional[binaryTreeNode]) -> bool:

        queue_1 = [tree_1]
        queue_2  = [tree_2]


        while(len(queue_1) != 0  and len(queue_2) != 0):

            walker_1 = queue_1.pop(0)
            walker_2 = queue_2.pop(0)

            if walker_1.val != walker_2.val:
                return False 

            if walker_1.left != None and walker_2.left != None:
                queue_1.append(walker_1.left)
                queue_2.append(walker_2.left)
            
            elif walker_1.left == None and walker_2.left == None:
                pass
            
            else:
                return False
            
            if walker_1.right and walker_2.right:
                queue_1.append(walker_1.right)
                queue_2.append(walker_2.right)

            elif walker_1.right == None and walker_2.right == None:
                pass
            
            else:
                return False   



        if len(queue_1) == len(queue_2):
            return True
        return False
    
    if tree_1 != None:
        if tree_2 == None:
            # because tree_1 will contain some node does have a none Node
            return True

        else:
            # use btf and treverse the tree_1 and find the sub tree node in tree one  
            res = False
            queue = [tree_1]

            while(len(queue) != 0):
                walker = queue.pop(0)

                if walker.val == tree_2.val:                    
                    res += check_same_tree(walker, tree_2)
                    if res:
                        return res
                
                if walker.left:
                    queue.append(walker.left)

                if walker.right:
                    queue.append(walker.right)

            return res


