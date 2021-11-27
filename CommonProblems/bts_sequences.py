from typing import Optional, List, Tuple, Union

from Graphs import BinaryTreeNode



def get_all_seq(root:BinaryTreeNode) -> List[List[int]]:

    res = [[root.val]]
    left_res, right_res = None, None
    if root.left:
        left_res = get_all_seq(root.left)

    if root.right:
        right_res = get_all_seq(root.right)


    if left_res and right_res:
        # do some work 
        


    elif left_res:
        for i in range(len(left_res)):
            left_res[i] =  res[0] + left_res[i]
            res.append(left_res[i])
        
        res.pop(0)

    elif right_res:
        for i in range(len(right_res)):
            right_res[i] =  res[0] + right_res[i]
            res.append(right_res[i])
        
        res.pop(0)
    
    
    return res 




def get_all_sequeneces(root:BinaryTreeNode) -> List[List[int]]:

    # def get_all_sequeneces(node:BinaryTreeNode, pastCombinations:List[List[int]]) -> List[List[int]]:

    #     pass 


    # basically have to treverse the tree 
    # then I have to add the left and the right in swaping order 
    # if right and left exist otherwise just add one and move 


    def get_all_combination(base_list:List[List[int]], new_pair:Union(int, Tuple[int,int])) -> List[List[int]]:

        if int == type(new_pair):

            for list in base_list:
                list.append(new_pair)
            return base_list
        else:
            
            for list in base_list:
                
                tmp_list =



    res = []
    if root:
    
        res = [[root.val]]
        queue = [root]

        while(len(queue) != 0):

            walker = queue.pop(0)
        
            
            
            if walker.right and walker.left:
                # both case 

            elif walker.right:
                # only right case
                get_all_combination(res, walker.right.val)
            elif walker.left:
                # only left case 
                get_all_combination(res, walker.left.val)

            else:
                # skip case
                pass
            

            if walker.


        

    


    return res 





