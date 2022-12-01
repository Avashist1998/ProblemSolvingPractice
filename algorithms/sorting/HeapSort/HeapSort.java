public class HeapSort{
    // sort the inputed array
    public void sort(int arr[]){
        // define the size of the array
        int n = arr.length;
        // n/2 -1 defines the number of level will the heap will have
        for (int i = n/2 -1 ; i >= 0; i--)
            heapify(arr, n,i);    
            //This will make creat the heap such that the root is the largest value 
        for (int i = n-1; i > 0; i--){
            // replacing the largest value(index 0) to the very last value
            int temp = arr [0];
            arr[0] = arr[i];
            arr[i] = temp;
            // reduces the a size of the array by 1 and recreats the heap.
            // this will cause the root to be the largest value always and
            // they will be removed from the heapify part by reducing i
            heapify(arr, i, 0);
        }
    }
    // This function just goes throught the array and create a heap
    void heapify(int arr[], int n, int i){
        // set the ith element as the largest element
        int largest = i;
        // set index for the right and left node of the tree. 
        // using a next math trick to extract the index
        int l = 2*i + 1;
        int r = 2*i + 2;
        // if the i th element is smaller than the left node
        if (l < n && arr[l] > arr[largest])
            largest = l;
        // if the i th or right element is smaller than the left node
        if (r < n && arr[r] > arr[largest])
            largest = r;
        // if ith value was less than either left than right node values
        if (largest != i){
            // set the largest value to the i th index
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            // recursion to call the sub trees
            heapify(arr,n,largest);
        }
    }
    //This function basically print the array.
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
        System.out.println("Original array is");
        printArray(arr);
        HeapSort ob = new HeapSort(); 
        ob.sort(arr); 
        System.out.println("Sorted array is"); 
        printArray(arr); 
    } 
}