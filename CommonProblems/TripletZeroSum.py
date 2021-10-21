from time import time
def naiveApproch(arr:list(), n:int):
    output = list()
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1, n):
                if (arr[i]+arr[j]+arr[k] == 0):
                  output.append([arr[i], arr[j], arr[k]])
    return output

def hashApproch(arr:list(), n:int):
    output = list()
    for i in range(n-1):
        s = set()
        for j in range(i+1, n):
            x = -1*(arr[i] + arr[j])
            if x in s:
                output.append([x,arr[i], arr[j]])
            else:
                s.add(arr[j])
    return output

def sortApproch(arr:list(), n:int):
    arr.sort()
    output = list()
    for i in range(n-1):
        l = i+1
        r = n-1
        x = arr[i]
        while (l < r):
            if (x + arr[l] + arr[r] == 0):
                output.append([x,arr[l],arr[r]])
                l+=1
                r-=1
            elif(x+arr[l] + arr[r] < 0):
                l+=1
            else:
                r-=1
    return output


arr = [0,-1,2,-3,1]
n = len(arr)
startNaive = time()
print(naiveApproch(arr,n))
print("Time of the nieve approch :{}".format(time()-startNaive))

startHash = time()
print(hashApproch(arr,n))
print("Time of the hash approch {}".format(time()-startHash))

startSort = time()
print(sortApproch(arr, n))
print("Time of the sort apporch {}".format(time()-startSort))
