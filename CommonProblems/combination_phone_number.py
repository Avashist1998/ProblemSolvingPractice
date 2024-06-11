# LC 17.
from typing import List

def letterCombinations(self, digits: str) -> List[str]:
    lookup = {
            "2": "a,b,c",
            "3": "d,e,f",
            "4": "g,h,i",
            "5": "j,k,l",
            "6": "m,n,o",
            "7": "p,q,r,s",
            "8": "t,u,v",
            "9": "w,x,y,z"
    }

    def nested_lookup_combination(digits: str, prefix: str) -> List[str]:

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            res = lookup[digits].split(",")
            for i in range(len(res)):
                res[i] = prefix + res[i]
            return res
        else:
            prefixes = nested_lookup_combination(digits[0], prefix)
            res = []
            for sub_pre in prefixes:
                sub = nested_lookup_combination(digits[1:], sub_pre)
                res += sub
            return res

    return nested_lookup_combination(digits, "")