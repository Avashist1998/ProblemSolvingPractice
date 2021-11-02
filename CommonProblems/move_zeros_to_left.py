def move_zeros_to_left(arr: list):

    zero_count = 0 

    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            zero_count += 1

        else:
            arr[i+zero_count] = arr[i]

    for i in range(zero_count):
        arr[i] = 0



        
tests = [[1,2,3,4,5], [1, 0, 2, 0, 4,0,5], [0,0,0,0,0], [1,2,3,4,0]]


for test in tests:
    print(test)
    move_zeros_to_left(test)
    print(test)
