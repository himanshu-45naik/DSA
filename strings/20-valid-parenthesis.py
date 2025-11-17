# Valid Parenthesis
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

class Solution:
    def isValid(self, s: str) -> bool:
        # We will use stack to solve this problem
        # Initiate an empty stack.
        # Parse through the string of parenthesis, keep adding each parenthesis in the stack.
        # When we come across an close parenthesis, pop the last open parenthesis
        # That is, we only add the open patenthesis in the stack and pop the last open parenthesis when a close parenthesis is found.

        n = len(s)
        stk = []

        mapped = {')': '(', ']': '[', '}': '{'}

        for i in range(n):
            if s[i] in ["(", "[", "{"]:
                stk.append(s[i])
            elif s[i] in [")", "]", "}"]:
                if not stk or (stk[-1] != mapped[s[i]]):
                    return  False
                stk.pop()
        
        return len(stk) == 0
                
s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))