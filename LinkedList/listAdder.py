import unittest
from LinkedList import single_linked_list

def listAdder(list_1:single_linked_list, list_2:single_linked_list):
    walker_1 = list_1.head
    walker_2 = list_2.head
    sum_list = single_linked_list(name="Sum_list")
    carry = 0
    while ((walker_1 is not None) or (walker_2 is not None)):
        val_1 = 0
        val_2 = 0
        if walker_1:
            val_1 = walker_1.data_val
        if walker_2:
            val_2 = walker_2.data_val
        new_val = val_1 + val_2 + carry
        carry = 0
        if (new_val > 10):
            carry = 1
            new_val -= 10
        sum_list.add_back(new_val)
        if walker_1:
            walker_1 = walker_1.next_node
        if walker_2:
            walker_2 = walker_2.next_node
    if carry:
        sum_list.add_back(carry)
    return sum_list

def list_slist(name:str, values:list):
    my_list = single_linked_list(name=name)
    for i in range(len(values)):
        my_list.add_back(values[i])
    return my_list
    
class testListAdder(unittest.TestCase):
    def test_single_number_case(self):
        list_1 = single_linked_list(data_val=7,name='list_1')
        list_2 = single_linked_list(data_val=5,name='list_2')
        sum_list = listAdder(list_1, list_2)
        self.assertEqual('2, 1' ,sum_list.list_val())

    def test_diff_length_case(self):
        values_1 = [7, 1]
        values_2 = [5]
        list_1 = list_slist('list_1', values_1)
        list_2 = list_slist('list_2', values_2)
        sum_list = listAdder(list_1, list_2)
        self.assertEqual('2, 2' ,sum_list.list_val())
    
    def test_classic_case(self):
        values_1 = [7,1,6]
        values_2 = [5,9,2]
        list_1 = list_slist('list_1', values_1)
        list_2 = list_slist('list_2', values_2)
        sum_list = listAdder(list_1, list_2)
        self.assertEqual('2, 1, 9' ,sum_list.list_val())


if __name__ == "__main__":
    unittest.main()