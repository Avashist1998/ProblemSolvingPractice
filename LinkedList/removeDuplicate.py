import unittest
from LinkedList import single_linked_list as sll

def remove_duplicate(a_list:sll):
    tracker = set()
    walker = a_list.head
    tracker.add(walker.data_val)
    while(walker.next_node != None):
        if walker.next_node.data_val in tracker:
            walker.next_node = walker.next_node.next_node
        else:
            tracker.add(walker.next_node.data_val)
            walker = walker.next_node

class testRemoveDuplicate(unittest.TestCase):
    def test_one_value_case(self):
        my_list = sll(1, 'my_list')
        remove_duplicate(my_list)
        self.assertEqual(my_list.list_val(), sll(1,'my_list').list_val())

    def test_all_duplicate_case(self):
        values = [1, 2, 2, 2, 2, 2, 3]
        my_list = sll()
        for v in values:
            my_list.add_back(v)
        remove_duplicate(my_list)
        self.assertEqual(my_list.list_val(),'1, 2, 3')

    def test_even_duplicate_case(self):
        values = [1,2,4,2,6,8]
        my_list = sll()
        for v in values:
            my_list.add_back(v)
        remove_duplicate(my_list)
        self.assertEqual(my_list.list_val(), '1, 2, 4, 6, 8')
    
    def test_odd_duplicate_case(self):
        values = [1,2,4,9,2,6,8]
        my_list = sll()
        for v in values:
            my_list.add_back(v)
        remove_duplicate(my_list)
        self.assertEqual(my_list.list_val(), '1, 2, 4, 9, 6, 8')

if __name__ == "__main__":
    unittest.main()