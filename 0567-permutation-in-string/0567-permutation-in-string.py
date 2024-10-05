class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        l = 0
        r = 0
        cnt = Counter()
        need = len(s1)

        while r < len(s2):
            if s2[r] in freq:
                cnt[s2[r]] += 1
                while cnt[s2[r]] > freq[s2[r]]:
                    cnt[s2[l]] -= 1
                    l += 1
                if r - l + 1 == need:
                    return True
            else:
                cnt.clear()
                l = r + 1
            r += 1
        return False
