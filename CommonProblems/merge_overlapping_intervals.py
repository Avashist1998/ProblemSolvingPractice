def merge_overlapping_intervals(arr:list):
    
    i = 0
    res = list()
    right, left = arr[0]
    while(i < len(arr)):
        new_right, new_left = arr[i]

        if new_right >= right and  new_right <= left:
            left = new_left 
        
        else:
            res.append([right,left])
            if i+1 < len(arr):
                right, left = arr[i+1]
        i += 1

