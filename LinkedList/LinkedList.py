class node():
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_node = None

class node_d(node):
    def __init__(self, data_val=None):
        super().__init__(data_val)
        self.prev_node = None

class single_linked_list():
    def __init__(self, data_val, name:str="list"):
        head_node = node(data_val)
        self.head = head_node
        self.name = name

    def __str__(self):
        return f'single_linked_list with name :({self.name})'
    
    def list_print(self):
        print(self.head.data_val, end='')
        walker = self.head.next_node
        while (walker is not None):
            print(', ', walker.data_val,end='')
            walker = walker.next_node
        print(' ')

    def add_node_back(self, value):
        new_node = node(value)
        walker = self.head
        while (walker.next_node):
            walker = walker.next_node
        walker.next_node = new_node

    def add_node_front(self, value):
        walker = self.head
        self.head = node(value)
        self.head.next_node = walker

    def add_node_middle(self, mid_node:node, value):
        new_node = node(value)
        new_node.next_node = mid_node.next_node
        mid_node.next_node = new_node

class double_linked_list():
    def __init__(self, data_val, name:str="list_d"):
        head_node = node_d(data_val)
        self.head = head_node
        self.name = name
        self.tail = node_d()
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def __str__(self):
        return f'single_linked_list with name :({self.name})'

    def list_print(self):
        walker = self.head
        while (walker is not None):
            print(walker.data_val,end=', ')
            walker = walker.next_node
        print(' ')

    def add_node_front(self, value):
        new_head = node_d(value)
        new_head.next_node = self.head
        self.head.prev_node = new_head
        self.head = new_head

    def add_node_back(self, value):
        new_tail = node_d(value)
        self.tail.next_node = new_tail
        new_tail.prev_node = self.tail
        self.tail = new_tail
    
    def add_node_middle(self, mid_node:node_d, value):
        new_node = node_d(value)
        new_node.next_node = mid_node.next_node
        new_node.prev_node = mid_node
        mid_node.next_node = new_node
    