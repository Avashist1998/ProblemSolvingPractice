from typing import List 



def selection_sort(arr: List):


    for i in range(len(arr)-1, -1, -1):
        current_max = arr[0]

        for j in range(0, i+1):
            if current_max < arr[j]:
                current_max = arr[j]

        arr[i] = current_max 