from collections import defaultdict
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        char_map = Counter(t)
        L = 0
        min_window_len = float("inf")
        min_window = ""
        missing = len(t)

        for R in range(N):
            char = s[R]
            if char in char_map:
                if char_map[char] > 0:
                    missing -= 1
                char_map[char] -= 1

                while missing == 0:
                    # 1) record smaller window
                    if R - L + 1 < min_window_len:
                        min_window, min_window_len = s[L:R+1], R - L + 1

                    # 2) give back s[L]
                    if s[L] in char_map:
                        char_map[s[L]] += 1
                        # 3) if we now need it again, bump missing
                        if char_map[s[L]] > 0:
                            missing += 1
                    # 4) slide left
                    L += 1
        return min_window

Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd") # type: ignore