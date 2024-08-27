from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        frac = [0]
        vals = []
        over = False
        for i in expression:
            if i=="/":
                over=True
            if (i=="-" or i=="+") and over:
                frac[0] += Fraction(''.join(vals))
                over = False
                vals = []
            vals.append(i)
        frac[0] += Fraction(''.join(vals))
        ans = frac[0].as_integer_ratio()
        return str(ans[0])+"/"+str(ans[1])