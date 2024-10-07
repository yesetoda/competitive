class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            if stack :
                if stack[-1] == "A":
                    if i == "B":
                        stack.pop()
                    else:
                        stack.append(i)
                elif stack[-1] == "C":
                    if i == "D":
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
            
        return len(stack)