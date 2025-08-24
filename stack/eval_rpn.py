from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []
        for n in tokens:
            if n in ops:
                second = stack.pop()
                first = stack.pop()
                # res = second ops first
                num1 = int(first)
                num2 = int(second)
                operator_str = n

                # Perform the calculation based on the operator
                if operator_str == "+":
                    result = num1 + num2
                elif operator_str == "-":
                    result = num1 - num2
                elif operator_str == "*":
                    result = num1 * num2
                else:
                    result = round(num1 / num2)
                stack.append(str(result))
            else:
                stack.append(n)
        return stack[0]
Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])