#LC 134.
from typing import List


# TODO: need to review

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:

    if sum(gas) < sum(cost):
        return -1

    n=len(gas)
    res, total = 0, 0
    diff=[gas[i]-cost[i] for i in range(n)]
    for i in range(n):
        total+=diff[i]
        if total<0:
            res=i+1
            total=0
    return res