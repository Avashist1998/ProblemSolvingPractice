#LC 739
from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:

    stack = []
    res = [0 for i in range(len(temperatures))]
    for i in range(len(temperatures)-1, -1, -1):
        if stack:
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop(-1)
            if stack:
                res[i] = (stack[-1][0] - i)
            stack.append([i, temperatures[i]])
        else:
            stack.append([i, temperatures[i]])
    return res
