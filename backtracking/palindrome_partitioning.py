class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        length = len(s)
        
        def backtrack(i):
            if i >= length:
                res.append(part.copy())
                return
            
            for j in range(i, length):
                if self.isPali(s[i:j+1]):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return res


    def isPali(self, word):
        for i in range(len(word)//2):
            if word[i] != word[-i-1]:
                return False
        return True