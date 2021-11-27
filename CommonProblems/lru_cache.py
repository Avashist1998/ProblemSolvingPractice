from LinkedList import node_d

class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.tail = None
        self.head = node_d(-1)
        self.capacity = capacity 
        self.head.next_node = self.tail
        
        
    def updateStatus(self, val_node) -> None:
        # assume that key is in data and already has a node

        if val_node.val != self.tail.val:
            # capacity is more than 1
            # there are at least two nodes in the list 
            # node that we are updating can not be the tail 
            
            tmp = val_node.next_node
            tmp.prev_node = val_node.prev_node
            val_node.prev_node.next_node = tmp
            
            self.tail.next_node = val_node
            val_node.prev_node = self.tail
            self.tail = self.tail.next_node
        

    def get(self, key: int) -> int:
        
        if key in self.data:
            val, key_node =  self.data[key]
            # update noede position
            self.updateStatus(key_node)
            return val
        
        return -1

    
        
    def put(self, key: int, value: int) -> None:

        
        if self.tail == None:
            # we are adding the first node 
            
            val_node = node_d(key)
            val_node.prev_node = self.head 
            self.head.next_node = val_node
            self.tail = val_node
        
        
        elif self.capacity == 1:
            if key in self.data:
                _, val_node = self.data[key]
            else:
                if self.tail:
                    prev_node = self.tail
                    self.data.pop(prev_node.val)

                val_node = node_d(key)
                self.head.next_node = val_node 
                val_node.prev_node = self.head
                self.tail = val_node                

        else:
            
            if key in self.data:
                # we need to update the data
                _, val_node = self.data[key]
                self.updateStatus(val_node)

            else:
                    
                if self.capacity == len(self.data):
                    # we need to remove the data
                    # removing the node
                    remove_node = self.head.next_node
                    self.data.pop(remove_node.val)
                    
                    # updating the head pointer
                    self.head.next_node = remove_node.next_node
                    remove_node.next_node.prev_node = self.head
                    
                    # add the new pointer 
                    val_node = node_d(key)
                    
                    # updating the tail 
                    val_node.prev_node = self.tail 
                    self.tail.next_node = val_node
                    self.tail = self.tail.next_node 
                else:
                    # we have space and we are adding a new node 
                    val_node = node_d(key)
                    val_node.prev_node = self.tail 
                    self.tail.next_node = val_node
                    self.tail = self.tail.next_node
                        
        self.data[key] = (value, val_node)
