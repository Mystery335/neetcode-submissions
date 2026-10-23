class Solution:
    def isValid(self, s: str) -> bool:
        chart = {
            "}" : "{",
            ")" : "(",
            "]" : "[" 
        }
        stack = []
        for c in s:
            if c in chart:
                # If stack isn't empty and top of stack is the corresponding opening bracket
                if stack and stack[-1] == chart[c]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack




