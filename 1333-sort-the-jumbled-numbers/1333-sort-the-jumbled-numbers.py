class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        for i in range(10):
            mapping[i] = str(mapping[i])
        def mechanism(i):
            ans = []
            for d in str(i):
                ans.append(mapping[int(d)])
            return int("".join(ans))
        nums.sort(key=mechanism)
        return nums


        