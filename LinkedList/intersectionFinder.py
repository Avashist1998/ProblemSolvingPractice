import unittest
from LinkedList import node
from LinkedList import single_linked_list as sll


def common_node_finder(n_1:node, n_2:node)-> node:
    while(n_1 and n_2):
        if (n_1 == n_2):
            return n_1
        n_1 = n_1.next_node
        n_2 = n_2.next_node
    return None

def intersection_finder(list_1:sll, list_2:sll) -> node:
    walker_1 = list_1.head
    walker_2 = list_2.head
    while(walker_1 and walker_2):
        if (walker_1 == walker_2):
            return walker_1
        walker_1 = walker_1.next_node
        walker_2 = walker_2.next_node
    if (walker_1 or walker_2):
        if (walker_1 is None):
            shift = 0
            while(walker_2):
                shift+=1
                walker_2 = walker_2.next_node
            walker_1 = list_1.head
            walker_2 = list_2.head
            while(shift):
                walker_2 = walker_2.next_node
                shift-=1
        elif(walker_2 is None):
            shift = 0
            while(walker_1):
                shift+=1
                walker_1 = walker_1.next_node
            walker_1 = list_1.head
            walker_2 = list_2.head
            while(shift):
                walker_1 = walker_1.next_node
                shift-=1
        return common_node_finder(walker_1,walker_2)
    return None

class testIntersectionFinder(unittest.TestCase):
    def test_head_intersect_case(self):
        list_1 = sll(1,name="One_list")
        list_1.add_back(2)
        self.assertEqual(list_1.head, intersection_finder(list_1, list_1))
    
    def test_no_intersect_case(self):
        list_1 = sll(1, name="list 1")
        list_2 = sll(2, name="list_2")
        self.assertIsNone(intersection_finder(list_1, list_2))

    def test_middle_intersect_case(self):
        list_1 = sll(name="list 1")
        for i in range(5):
            list_1.add_back(i)
        list_2 = sll(6, name="list 2")
        list_2.head.next_node = list_1.head.next_node
        self.assertEqual(list_2.head.next_node, intersection_finder(list_1, list_2)) 

    def test_diff_len_case(self):
        list_1 = sll(name="list 1")
        list_2 = sll(name="list 2")
        for i in range(5):
            list_1.add_back(i)
        for i in range(4,8):
            list_2.add_back(i)
        walker_2 = list_2.head
        while(walker_2.next_node):
            walker_2 = walker_2.next_node
        walker_2.next_node = list_1.head.next_node 
        self.assertEqual(list_1.head.next_node, intersection_finder(list_1,list_2))
        self.assertEqual(list_1.head.next_node, intersection_finder(list_2,list_1))

if __name__ == "__main__":
    unittest.main()