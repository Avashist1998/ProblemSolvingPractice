from typing_extensions import ParamSpec
import object


class MinHeap(object):
    
    def __init__(self, capacity:int = 10) -> None:
        
        self.arr = list()
        self.capacity = 10
            


    def getLeftChildIndex(self, parentIndex:int) -> int:
        return 2*parentIndex + 1

    def getRightChildIndex(self, parentIndex: int) -> int:
        return 2*parentIndex + 2

    def getParentIndex(self, childIndex) -> int:
        return (childIndex - 1) // 2

    def getLeftChild(self, parentIndex) -> int:
        return self.arr[self.getLeftChildIndex(parentIndex)]

    def getRightChild(self, parentIndex) -> int:
        return self.arr[self.getRightChildIndex(parentIndex)]

    def getParent(self, childIndex) -> int:
        return self.arr[self.getParentIndex(childIndex)]

    def hasLeftChild(self, index:int) -> bool:
        return self.getLeftChildIndex(index) < self.capacity 

    def hasRightChild(self, index:int) -> bool:
        return self.getRightChildIndex(index) < self.capacity 

    def hasParent(self, index:int) -> bool:
        return index > 0

    def swap(self, index_1:int, index_2:int):
        self.arr[index_1], self.arr[index_2] = self.arr[index_2], self.arr[index_1]


    def ensureCapacitySize(self):
        if self.size > self.capacity:
            self.pool()

 

    def peek(self):
        if self.size != 0:
            return self.arr[0]
        return None
    
    def pool(self) -> int:
        
        self.swap(0, len(self.arr)-1)
        previous_min = self.arr.pop(-1)
        self.size -= 1
        self.heapifyDown()
        return previous_min
    

    def add(self, item:int):

        self.arr.append(item)
        self.heapifyUp()


    def heapifyUp(self):
        index = len(self.arr) - 1

        while(self.hasParent(index) and self.getParent(index) > self.arr[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParent(index)

    def heapifyDown(self):

        index = 0
        while(self.hasLeftChild(index)):
            smallerIndex = self.getLeftChildIndex(index)

            if self.hasRightChild(index) and self.getRightChild(index) < self.arr[smallerIndex]:
                smallerIndex = self.getRightChild(index)

            if self.arr[index] < self.arr[smallerIndex]:
                break

            self.swap(index, smallerIndex)            
            index = smallerIndex

