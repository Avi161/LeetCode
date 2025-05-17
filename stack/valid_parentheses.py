# 20. Valid Parentheses Easy

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = {"}":"{","]":"[",")":"("}

        for par in s:
            if not stack and par in closeToOpen:
                return False
            else:
                if par in closeToOpen:
                    if stack[-1] == closeToOpen[par]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(par)
        if not stack:
            return True
        else:
            return False