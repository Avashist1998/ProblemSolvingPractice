import unittest
from LinkedList import single_linked_list

def reverse_list_palendrome(my_list:single_linked_list) -> bool:
    
    walker = my_list.head
    reversed_list = single_linked_list(
        name="reverse_{}".format(my_list.name))
    while(walker):
        reversed_list.add_node_front(walker.data_val)
        walker = walker.next_node
    walker_1 = my_list.head
    walker_2 = reversed_list.head
    while walker_1:
        if(walker_1.data_val != walker_2.data_val):
            return False
        walker_1 = walker_1.next_node
        walker_2 = walker_2.next_node
    return True

def palendrome(my_list:single_linked_list)->bool:
    
    slow_runner = my_list.head
    fast_runner = my_list.head
    odd = False
    stack = []
    while(fast_runner):
        stack.append(slow_runner.data_val)
        slow_runner = slow_runner.next_node
        if (fast_runner.next_node):
            fast_runner = fast_runner.next_node.next_node
        else:
            odd = True
            fast_runner = None
    if len(stack) == 1: return True
    if odd: stack.pop()
    while(slow_runner):
        if stack.pop() != slow_runner.data_val:
            return False
        slow_runner = slow_runner.next_node
    return True

class testPalendrome(unittest.TestCase):

    def test_single_case(self):
        pal_1 = single_linked_list(name="palendrome")
        pal_1.add_back('a')
        self.assertTrue(palendrome(pal_1))
    
    def test_even_case(self):
        pal_1 = single_linked_list(name="palendrome")
        values = ['a', 'n', 'n', 'a']
        for v in values:
            pal_1.add_back(v)
        self.assertTrue(palendrome(pal_1))
        pal_1.add_back('a')
        pal_1.add_back('n')
        self.assertFalse(palendrome(pal_1))

    def test_odd_case(self):
        pal_1 = single_linked_list(name="palendrome")
        values = ['m', 'o', 'm']
        for v in values:
            pal_1.add_back(v)
        self.assertTrue(palendrome(pal_1))
        pal_1.add_back('o')
        pal_1.add_back('n')
        self.assertFalse(palendrome(pal_1))

if __name__ == "__main__":
    unittest.main()