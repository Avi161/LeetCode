class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        L, R = 0, 1
        char_set = set(s[0])
        max_len = 1

        while R < len(s):
            this_char = s[R]
            if this_char in char_set:
                while s[L] != this_char:
                    char_set.remove(s[L])
                    L += 1
                char_set.remove(s[L])
                L += 1
            char_set.add(this_char)
            max_len = max(max_len, R - L + 1)
            R += 1
        return max_len