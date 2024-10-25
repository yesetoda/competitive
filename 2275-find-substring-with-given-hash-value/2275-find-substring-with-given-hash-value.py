class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def add(x,s):
            return (x * power + ((ord(s)-96)%modulo)) % modulo
        def rem(x,s):
            val = (x - ( (ord(s)-96)%modulo )*pow(power,k-1,modulo)) % modulo
            return val
        
        x = 0
        leng = len(s)
        for i in range(leng-1,leng-k-1,-1):
            x = add(x,s[i])
        ans = []

        for i in range(leng-k-1,-1,-1):
            if x == hashValue:
                ans.append(i)
        
            x = rem(x,s[i+k])
            x = add(x,s[i])

        if x == hashValue:
            ans.append(i-1)
        i = ans[-1]
        return s[i+1:i+k+1]


