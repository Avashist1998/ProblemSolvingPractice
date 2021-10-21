from typing import List 



def insert_sort(arr: List) :

    for i in range(1, len(arr)):
        current_val = arr[i]
        j = i - 1

        while(j >= 0 and current_val < arr[j]):
            arr[j] = arr[j+1]
            j -= 1
        arr[j+1] = current_val