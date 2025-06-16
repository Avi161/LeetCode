from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_char_cnt = defaultdict(int)
        t_char_cnt = defaultdict(int)

        if len(s) != len(t):
            return False
        
        length = len(s)

        for i in range(length):
            s_char_cnt[s[i]] += 1
            t_char_cnt[t[i]] += 1
        
        for s_key in s_char_cnt.keys():
            if s_char_cnt[s_key] != t_char_cnt.get(s_key, 0):
                return False
        return True
