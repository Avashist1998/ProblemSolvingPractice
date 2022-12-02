"""N stack implementation"""
from logging import getLogger
from typing import List, Optional, Final

_LOGGER: Final = getLogger(__name__)


class NStack():
    """N stacks class implementation."""

    def __init__(self, n_number: int, size: int):
        """N stack constructors
        Args:
            n: number of stack
            size: capacity of each stack.
        """
        self.number_of_stack = n_number
        self.capacity_each_stack = size
        self.sizes_of_each_stack = [0] * n_number
        self.data: List[int] = [0] * n_number * size

    def push(self, stack_number: int, val: int):
        """Add number to stack with the given stack number."""
        if stack_number <= 0 or stack_number > len(self.sizes_of_each_stack):
            raise IndexError("stack number is out of range")
        stack_index = stack_number - 1
        size = self.sizes_of_each_stack[stack_index]
        if size == self.capacity_each_stack:
            raise ValueError("Stack is overloaded")

        index = stack_index * self.capacity_each_stack + size
        self.data[index] = val
        self.sizes_of_each_stack[stack_index] += 1

    def _get_top_index(self, stack_number: int) -> int:
        """Gets to index of the top element of the stack
        Args:
            stack_number: number assocated with that stack
        """
        if stack_number <= 0 or stack_number > len(self.sizes_of_each_stack):
            raise IndexError("stack number is out of range")
        if self.is_empty(stack_number):
            return -1
        stack_index = stack_number - 1
        top_val_index = stack_index * self.capacity_each_stack + self.sizes_of_each_stack[
            stack_index] - 1
        return top_val_index

    def pop(self, stack_number: int) -> Optional[int]:
        """Pop the top number from the stack.
        Args:
            stack_number: number assocated with that stack
        Return:
            int value on top of the stack with the given stack number.
        """
        try:
            top_val_index = self._get_top_index(stack_number)
            if top_val_index == -1:
                return None
            self.sizes_of_each_stack[stack_number - 1] += -1
            val = self.data[top_val_index]
            return val
        except Exception as ex:
            _LOGGER.error(ex)
            raise

    def top(self, stack_number: int) -> Optional[int]:
        """Gives top number from the stack.
        Args:
            stack_number: number assocated with that stack
        Return:
            int value on top of the stack with the given stack number.
        """
        try:
            top_val_index = self._get_top_index(stack_number)
            if top_val_index == -1:
                return None
            val = self.data[top_val_index]
            return val
        except Exception as ex:
            _LOGGER.error(ex)
            raise

    def is_empty(self, stack_number: int) -> bool:
        """Check if the stack with stack_number is empty
        Args:
            stack_number: number assocated with that stack
        Returns:
            True if stack is empty and false if stack has data
        """
        if stack_number <= 0 or stack_number > len(self.sizes_of_each_stack):
            raise IndexError("stack number is out of range")
        stack_index = stack_number - 1
        return self.sizes_of_each_stack[stack_index] == 0
