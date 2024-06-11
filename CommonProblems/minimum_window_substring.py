# 76. Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        class IncrementalStringMatcher:
            def __init__(self, t: str):
                self.t_map = {}
                for ch in t:
                    if ch in self.t_map:
                        self.t_map[ch] += 1
                    else:
                        self.t_map[ch] = 1
                self.curr_map = {}
                self.missing = len(self.t_map.keys())

            def add_char(self, ch: str):
                if ch in self.curr_map:
                    self.curr_map[ch] += 1

                else:
                    self.curr_map[ch] = 1
                
                if ch in self.t_map and self.t_map[ch] == self.curr_map[ch]:
                    self.missing -= 1


            def remove(self, ch: str):
                if ch in self.curr_map:
                    if ch in self.t_map and self.t_map[ch] == self.curr_map[ch]:
                        self.missing += 1
                    self.curr_map[ch] -= 1

            def is_match(self):
                return self.missing == 0

        if len(t) == 0 or len(s) == 0:
            return ""

        if len(s) < len(t):
            return ""

        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
    
        store = IncrementalStringMatcher(t)

        res = ""
        l, r = 0, 0
        sub_res =  ""
        while (l < len(s) or r < len(s)):

            if r < len(s):
                if not store.is_match():
                    store.add_char(s[r])
                    r += 1
                else:
                    sub_res = s[l:r]
                    if res == "":
                        res = sub_res
                    elif len(sub_res) < len(res):
                        res = sub_res
                    store.remove(s[l])
                    l += 1
            else:
                if store.is_match():
                    sub_res = s[l:r]
                    if res == "":
                        res = sub_res
                    elif len(sub_res) < len(res):
                        res = sub_res
                store.remove(s[l])
                l += 1
        return res