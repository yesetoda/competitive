class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        op = set("&|!")
        def operate(operator,a,b):
            if operator == "&":
                return a and b
            elif operator == "|":
                return a or b
            return not a
        stack = []
        order = []
        for ind,i in enumerate(expression):
            if i in op:
                order.append(i)
            else:
                if i == "(" or i == ",":
                    pass
                elif i == ")":
                    val = order.pop()
                    _ = order.pop()
                    if order:
                        if order[-1] in op:
                            order.append(not val if order[-1]=="!" else val)
                        else:
                            order[-1] = operate(order[-2],order[-1],val)
                    else:
                        order.append(val)
                else:
                    if order[-1] in op:
                        if order[-1] == "!":
                            order.append(i!="t")
                        else:
                            order.append(i=="t")
                    else:
                        order[-1] = operate(order[-2],order[-1],i=="t")
        return order[0]
        