import unittest
from LinkedList import single_linked_list as sll

def loop_detector(my_list:sll):
    slow_runner = my_list.head
    fast_runner = my_list.head
    colide = False
    while(fast_runner.next_node and fast_runner and not colide):
        slow_runner = slow_runner.next_node
        fast_runner = fast_runner.next_node.next_node
        if(slow_runner == fast_runner):
            colide = True
    if (fast_runner is None or fast_runner.next_node is None):
        return None
    else:
        slow_runner = my_list.head
        while(slow_runner != fast_runner):
            fast_runner = fast_runner.next_node
            slow_runner = slow_runner.next_node
        return slow_runner    
    return None

class testLoopDetector(unittest.TestCase):
    def test_no_loop_case(self):
        values = ['a', 'b', 'c', 'd', 'e','g','h']
        my_list = sll()
        for v in values:
            my_list.add_back(v)
        self.assertIsNone(loop_detector(my_list))
    
    def test_even_loop_case(self):
        values = ['a', 'b', 'c', 'd', 'e','g','h']
        my_list = sll()
        for v in values:
            my_list.add_back(v)
        walker = my_list.head
        while(walker.next_node):
            walker = walker.next_node
        walker.next_node = my_list.head.next_node
        self.assertEqual(my_list.head.next_node, loop_detector(my_list))

    def test_odd_loop_case(self):
        values = ['a', 'b', 'c', 'd', 'e','g','h']
        my_list = sll()
        for v in values:
            my_list.add_back(v)
        walker = my_list.head
        while(walker.next_node):
            walker = walker.next_node
        walker.next_node = my_list.head.next_node.next_node
        self.assertEqual(my_list.head.next_node.next_node, loop_detector(my_list))
    def test_head_loop_case(self):
        values = ['a', 'b', 'c', 'd', 'e','g','h']
        my_list = sll()
        for v in values:
            my_list.add_back(v)
        walker = my_list.head
        while(walker.next_node):
            walker = walker.next_node
        walker.next_node = my_list.head
        self.assertEqual(my_list.head, loop_detector(my_list))

if __name__ == "__main__":
    unittest.main()