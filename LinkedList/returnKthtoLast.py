from LinkedList import single_linked_list
import unittest

def returnKthtoLast(my_list:single_linked_list, k:int):
    walker = my_list.head
    k_node = my_list.head
    for i in range(k):
        if walker is None:
            return None
        walker = walker.next_node
    
    while(walker):
        walker = walker.next_node
        k_node = k_node.next_node
    return k_node

class testReturnKthtoLast(unittest.TestCase):        
    def test_behavior_normal(self):
        values = [1,2,4,2,6,8,14,28,25,19,12]
        my_list = single_linked_list(name='my_list')
        for i in range(len(values)):
            my_list.add_back(values[i])
        # Testing Values
        self.assertEqual(12, returnKthtoLast(my_list,1).data_val)
        self.assertEqual(19, returnKthtoLast(my_list,2).data_val)
        self.assertIsNone(returnKthtoLast(my_list,20))

if __name__ == "__main__":
    unittest.main()