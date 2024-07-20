class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        def dfs(candidates, target, index, path, result):
            if target <0:
                return
            if target==0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(candidates, target - candidates[i], i, path + [candidates[i]], result)
        dfs(candidates, target, 0, [], result)
        return result