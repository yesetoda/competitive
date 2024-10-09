# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         stack = []
#         pre = [0]
#         mx = 0
#         for i in s:
#             if stack:
#                 if stack[-1] == "(":
#                     if i == ")":
#                         stack.pop()
#                         pre.append(pre[-1]+1)
#                         if stack and stack[-1] == ")":
#                             mx = max(mx,pre[-1]-len(stack))
#                         if not stack:
#                             mx = max(mx,pre[-1]-len(stack))
#                     else:
#                         stack.append(i)
#                         pre.append(pre[-1]+1)
#                 else:
#                     if i == "(":
#                         pre.append(pre[-1]+1)
#                     else:
#                         pre.append(0)
#                     stack.append(i)
#             else:
#                 if i == "(":
#                     pre.append(pre[-1]+1)
#                 else:
#                     pre.append(0)
#                 stack.append(i)
#         print(pre)
#         return mx



# 6((4
           
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        mx = 0
        def calculate(val):
            nonlocal stack,mx

            while stack and not stack[-1] in p:
                val+=stack.pop()
            stack.append(val)
            mx = max(mx,val)
        p = set("()")
        for i in s:
            if stack:
                if stack[-1] == "(":
                    if i == ")":
                        stack.pop()
                        calculate(2)
                    else:
                        stack.append(i)
                elif stack[-1] == ")":
                    stack.append(i)
                else:
                    if i =="(":
                        stack.append(i)
                    else:
                        if stack :
                            val =  stack.pop()
                            if stack:
                                if stack[-1] == "(":
                                    stack.pop()
                                    val+=2
                                    stack.append(val)
                                    calculate(0)
                                else:
                                    stack.append(val)
                                    stack.append(i)
                            else:
                                stack.append(val)
                                stack.append(i)
            else:
                stack.append(i)
        return mx

