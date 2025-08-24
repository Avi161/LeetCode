class Solution:
    def simplifyPath(self, path: str) -> str:
        res = "/"
        i = 1
        stack = []

        # strip extra "/"
        while i < len(path):
            while i < len(path)-1 and path[i] == "/" and path[i-1] == "/":
                i += 1
            res += path[i]
            i += 1
        
        print(res)
        i = 1
        while i < len(res):
            start = j = i
            cur_str = ""
            while j < len(res) and res[j] != "/":
                cur_str += res[j]
                j += 1
            if cur_str == "..":
                if stack:
                    stack.pop()
            elif cur_str == ".":
                pass
            else:
                stack.append(cur_str)
            j += 1
            i = j
        print(stack)

Solution().simplifyPath("/home//foo/")