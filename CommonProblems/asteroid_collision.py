# LC 735
from typing import List

def asteroid_collision(asteroids: List[int]) -> List[int]:
    res = []
    for aster in asteroids:
        if len(res) == 0:
            res.append(aster)
        elif res[-1] < 0:
            res.append(aster)
        else:
            while len(res) > 0 and aster is not None and aster < 0 and res[-1] >= 0:
                top = res.pop()
                if abs(aster) > abs(top):
                    aster = aster
                elif abs(aster) < abs(top):
                    aster = top
                else:
                    aster = None
            if aster is not None:
                res.append(aster)
    
    return res