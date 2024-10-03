class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word).most_common()
        x = 10
        ans = 0
        for i in freq:
            ans += i[1]*(x//10)
            x+=1.25
        return int(ans)
