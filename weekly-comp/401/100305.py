"""


array size -> n

a[i] = 1 
0 <= i <= n - 1
 

kk 
"""


def value_after_k_second(n: int, k: int) -> int:
	def update(arr):
		val = arr[0]
		i = 1
		while i < len(arr):
			val += arr[i]
			arr[i] = val
			i+= 1

	arr = [1]*n
	
	for i in range(k):
		update(arr)
	return arr[-1]



