class Solution:
    def soupServings(self, n: int) -> float:
        rem_A = n
        rem_B = n

        options = [[100,0],[75,25],[50,50],[25,75]]
        self.prob = 0

        def dfs(rem_A, rem_B, root):
            if rem_A <= 0 and rem_B <= 0:
                self.prob += root*0.5*0.25
                return
            elif rem_A <= 0:
                self.prob += root*0.25
                return
            elif rem_B <= 0:
                return
            else:
                pass

            for a, b in options:
                new_A = rem_A - a
                new_B = rem_B - b
                dfs(new_A, new_B, root/2)
            return
        dfs(rem_A, rem_B, 2)
        return self.prob

Solution().soupServings(100)