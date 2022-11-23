class EmptyObject(Exception):

    def __init__(self):
        super().__init__
        self.message = "The object is empty"

    pass


class stack():

    class Node():

        def __init__(self, data_val=None):
            self.data_val = data_val
            self.next_node = None

        def __str__(self):
            return f"Data val: {self.data_val}"

    def __init__(self, data_val=None, name="a_stack"):
        self.top = Node(data_val)
        self.next = Node()
        self.name = name

    def pop(self):
        top_node = self.top
        self.top = self.top.next_node
        return top_node.data_val

    def push(self, data_val):
        if self.top is None:
            self.top = Node(data_val)
        else:
            new_top = Node(data_val)
            new_top.next_node = self.top
            self.top = new_top

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data_val

    def isEmpty(self):
        return self.top is None


class queue():

    class Node():

        def __init__(self, data_val=None):
            self.data_val = data_val
            self.next_node = None

        def __str__(self):
            return "data val : {}".format(self.data_val)

    def __init__(self, data_val=None, name="a_queque"):
        self.name = name
        self.first = None
        self.last = None
        if (data_val is not None):
            self.first = self.node(data_val)
            self.last = self.node(data_val)

    def add_item(self, data_val):
        new_node = self.node(data_val)
        if (self.last is not None):
            self.last.next = new_node
        self.last = new_node
        if (self.first is None):
            self.first = self.last

    def remove(self):
        if (self.first is None): raise EmptyObject
        data = self.first
        self.first = self.first.next_ndoe
        if (self.first is None):
            self.last = None
        return data.data_val

    def peek(self):
        if (self.first is None): raise EmptyObject
        return self.first.data_val

    def isEmpty(self):
        return self.first is None
