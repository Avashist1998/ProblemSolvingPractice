from typing import List 


def quick_sort(arr:List):

 
    if len(arr) > 1:
        pivot =  len(arr) - 1
        right, left, equal = list(), list(), 1

        for i in range(pivot):
            if arr[i] > pivot:
                right.append(arr[i])
            elif arr[i] < pivot:
                left.append(arr[i])
            else:
                equal += 1

        quick_sort(right), quick_sort(left)

        for i in range(len(arr)):
            if len(left) != 0:
                arr[i] = left.pop(0)
            elif equal != 0:
                arr[i] = arr[pivot]
                equal -= 1
            else:
                arr[i] = right.pop(0)


