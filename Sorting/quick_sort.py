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



def partition(arr, left_index=None, right_index=None):
    pivot = arr[left_index + (right_index - left_index) //2]

    while(left_index <= right_index):
        while(arr[left_index] < pivot):
            left_index += 1
        while(arr[right_index] > pivot):
            right_index -= 1
        
        if (left_index <= right_index):
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
            left_index += 1
            right_index -= 1

    return left_index



def quick_sort_inplace(arr:List, left_index:int, right_index:int):

    index = partition(arr, left_index, right_index)

    if (left_index < index - 1 ):
        quick_sort_inplace(arr, left_index, index-1)
    if (index < right_index):
        quick_sort_inplace(arr, index, right_index)



