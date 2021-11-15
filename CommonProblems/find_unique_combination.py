from typing import List

# Candiated = [1, 2, 3, 4, 5, 6]

def find_unique_combination(nums:List[int], target:int) -> List[List[int]]:
    res = list()
    
    for i in range(len(nums)):
        val = nums[i]
        new_target = target - val
        
        if new_target == 0:
            res.append([nums[i]])
        
        elif new_target  > 0:
            new_candidates = val.pop(i)
            sub_solution = find_unique_combination(new_candidates, new_target)

            for solution in sub_solution:
                solution.append(val)
                res.append(solution)
            
    return res


