from .Node import Node



def isPathBetweenNodes(start:Node, end:Node):

    # Beadth First Search 
    
    status = dict()
    queue = list()
    status[start.val] = "visiting"
    queue.append(start)


    while(len(queue) != 0):

        current_node = queue.pop(0)
        if current_node != None:
            if status[current_node.val] != 'visited':
                if current_node == end:
                    return True 

                else:
                    for neighbor in current_node.neighbors:
                        status[neighbor.val] = 'visiting'
                        queue.append(neighbor)

        
            status[current_node.val] = "visited"

    
    return False 
        


