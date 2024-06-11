#LC 287
from typing import List

def findDuplicate(nums: List[int]) -> int:
    # tmp = set()

    # for num in nums:
    #     if num in tmp:
    #         return num        
    #     tmp.add(num)

    # for i in range(len(nums)):
    #     val = nums[i]
    #     if val < 0:
    #         val = val * -1
    #     if nums[val-1] < 0:
    #         return val
    #     nums[val-1] = nums[val-1]*-1 


    slow, fast = nums[0], nums[0]
    slow = nums[slow]
    fast = nums[nums[fast]]

    while (slow != fast):
        slow = nums[slow]
        fast = nums[nums[fast]]

    fast = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow