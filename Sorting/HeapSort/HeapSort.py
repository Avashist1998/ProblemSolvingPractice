class HeapSort():
    def __init__(self):
        self.arr = []
    def sort(self, arr):
        n = len(arr)
        for i in range(n//2-1,-1,-1):
            self.heapify(arr, n, i)
        
        for i in range(n-1, 0,-1):
            temp = arr[0]
            arr[0] = arr[i]
            arr[i] = temp
            self.heapify(arr, i, 0)
        return arr 

    def heapify(self, arr, n, i):
        rightVal = 2*i+1
        leftVal = 2*i+2
        largest = i
        if (n > rightVal and arr[rightVal]> arr[largest]):
            largest = rightVal
        if (n > leftVal and arr[leftVal] > arr[largest]):
            largest = leftVal
        if (i != largest):
            temp = arr[i]
            arr[i] = arr[largest]
            arr[largest] = temp
            self.heapify(arr, n , largest)
    


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("The Original Array")
    print(arr)
    sorter = HeapSort()
    arr = sorter.sort(arr)
    print("The Sorted Array")
    print(arr)