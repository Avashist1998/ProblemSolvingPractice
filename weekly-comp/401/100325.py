""""



n - childer


[0, 1, 2, 3, 4, 5, 6, 7]

k - number of seconds 


We start at 0 and then pass to it right until no more 

k < n 

return k


n = 5

k =  12

[0, 1, 2, 3, 4]

12%5 = 2


""""



def numberOfChild(n: int, k: int) -> int:
	if k < n:
		return k
	
	r = k%(n-1)
	if (k//(n-1))%2 == 0:
		return r
	else:
		return (n - (r+1))

