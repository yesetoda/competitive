class Solution:
    def reverseWords(self, s: str) -> str:
        x = []
        v = []
        for i in s:
            if i == " ":
                if x and x[0] == " " and not v:
                    continue
                x = [" "]+v+x
                v = []
            else:
                v.append(i)
        if v and v[0] != " ":
            x = v+x
        return "".join(x).strip()

