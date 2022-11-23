class nStack():

    def __init__(self, n: int, size: int):
        total_lenght = n * size
        self.n = n
        self.sizes = [0] * n
        self.size_each = size
        self.values = [None] * total_lenght

    def push(self, stack_type: int, val: int):
        size = self.sizes[stack_type]
        if (size == self.size_each):
            raise ValueError("Stack is overloaded")
        else:
            index = stack_type * self.size_each + self.sizes[stack_type]
            self.values[index] = val
            self.sizes[stack_type] = size + 1

    def pop(self, stack_type: int):
        index = stack_type * self.size_each + self.sizes[stack_type] - 1
        val = self.values[index]
        self.values[index] = None
        self.sizes[stack_type] += -1
        return val

    def top(self, stack_type: int):
        index = stack_type * self.size_each + self.sizes[stack_type] - 1
        val = self.values[index]
        return val

    def is_empty(self, stack_type: int):
        return self.sizes[stack_type] == 0
