from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            char_cnt = [0]*26

            for c in s:
                char_cnt[ord(c)-ord('a')] += 1

            anagrams[tuple(char_cnt)].append(s)
        
        ans = []
        for val in anagrams.values():
            ans.append(val)
        return ans