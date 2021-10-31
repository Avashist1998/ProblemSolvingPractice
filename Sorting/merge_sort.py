from typing import List 


def merge_routine(arr_a: List, arr_b:List) -> List:

    res = list()
    while(len(arr_a) > 0 or len(arr_b) > 0):

        if len(arr_a) == 0:
            res.append(arr_b.pop(0))
        
        elif len(arr_b) == 0:
            res.append(arr_a.pop(0))
        
        elif arr_a[0] < arr_b[0]:
            res.append(arr_a.pop(0))
        else:
            res.append(arr_b.pop(0))

    return res

def merge_sort(arr: List):
    
    if len(arr) == 1:
        pass 
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

    else:

        mid = len(arr)//2

        left, right = arr[:mid], arr[mid:]
        merge_sort(left), merge_sort(right)
        sorted_arr = merge_routine(left, right)

        for i in range(len(arr)):
            arr[i] = sorted_arr[i]


