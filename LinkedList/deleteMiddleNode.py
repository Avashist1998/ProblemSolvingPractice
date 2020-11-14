import unittest
from LinkedList import single_linked_list,node
from returnKthtoLast import returnKthtoLast
def deleteMiddleNode(node:node):
    if (node is not None and node.next_node is not None):
        node_next = node.next_node
        node.data_val = node_next.data_val
        node.next_node = node_next.next_node


class testReturnKthtoLast(unittest.TestCase):        
    def test_behavior_normal(self):
        values = [1,2,4,2,6,8,14,28,25,19,12]
        my_list = single_linked_list(1, 'my_list')
        for i in range(1,len(values)):
            my_list.add_back(values[i])
        # Testing Values
        my_node = returnKthtoLast(my_list,6)
        values = my_list.list_val()
        deleteMiddleNode(my_node)
        update_values = my_list.list_val()
        self.assertEqual('1, 2, 4, 2, 6, 8, 14, 28, 25, 19, 12'
            ,values)
        self.assertEqual('1, 2, 4, 2, 6, 14, 28, 25, 19, 12'
            ,update_values)

if __name__ == "__main__":
    unittest.main()