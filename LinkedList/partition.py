import unittest
from LinkedList import single_linked_list

def partition(my_list:single_linked_list, value:int):
    walker = my_list.head
    right_list = single_linked_list(name='right_side')
    left_list = single_linked_list(name='left_side')
    while(walker is not None):
        if walker.data_val < value:
            right_list.add_back(walker.data_val)
        else:
            left_list.add_back(walker.data_val)
        walker = walker.next_node
    walker = right_list.head
    while(walker.next_node is not None):
        walker = walker.next_node
    walker.next_node = left_list.head
    return right_list

class testPartition(unittest.TestCase):
    def test_behavior(self):
        values = [1,2,4,2,6,34,123,8,7,14,28,25,19,12]
        my_list = single_linked_list(name='my_list')
        for i in range(len(values)):
            my_list.add_back(values[i])
        self.assertEqual('1, 2, 4, 2, 6, 34, 123, 8, 7, 14, 28, 25, 19, 12',
            my_list.list_val())
        my_list = partition(my_list, 14)
        self.assertEqual('1, 2, 4, 2, 6, 8, 7, 12, 34, 123, 14, 28, 25, 19',
            my_list.list_val())

if __name__ == "__main__":
    unittest.main()