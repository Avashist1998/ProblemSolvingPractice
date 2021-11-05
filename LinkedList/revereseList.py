from .LinkedList import node



def reverseList(previous_node:node = None, start_node:node = None, end_node:node=None):
  if previous_node == None:
    previous_node = node(-1)
    previous_node.next_node = start_node
  
  walker = start_node  
  
  while(walker.next != end_node):
    walker_next = walker.next_node
    walker.next_node = walker_next.next_node
    walker_next.next_node = previous_node.next_node
    previous_node.next_node = walker_next
  
  if previous_node.val == -1:
    previous_node.next_node = None





