#revise
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack (ind, path, sm):
            if sm == target:
                ans.append(path[:])
                return
            if ind>= len(candidates) or sm > target:
                return
            for idx in range(ind, len(candidates)):
                if idx > ind and candidates[idx] == candidates[idx - 1]:
                    continue
                path.append(candidates[idx])
                backtrack(idx + 1, path, sm + candidates[idx])
                path.pop()
        candidates.sort()
        backtrack(0, [], 0)
        return ans