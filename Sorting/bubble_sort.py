from typing import List 



def bubble_sort(arr: List):

    sorted_index = len(arr) - 1
    while(sorted_index != 0):

        for i in range(0, sorted_index):
            if arr[i] > arr[i-1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
        sorted_index += 1

