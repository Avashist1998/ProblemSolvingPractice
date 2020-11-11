import unittest
from LinkedList import single_linked_list


def remove_duplicate(a_list:single_linked_list):
    tracker = set()
    walker = a_list.head
    tracker.add(walker.data_val)
    while(walker.next_node != None):
        if walker.next_node.data_val in tracker:
            walker.next_node = walker.next_node.next_node
        else:
            tracker.add(walker.data_val)
        walker = walker.next_node
def main():
    values = [1,2,4,2,6,8,14,28,25,19,12]
    my_list = single_linked_list(1, 'my_list')
    for i in range(1,len(values)):
        my_list.add_node_back(values[i])
    my_list.list_print()
    remove_duplicate(my_list)
    my_list.list_print()

if __name__ == "__main__":
    main()