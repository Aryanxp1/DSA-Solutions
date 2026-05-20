class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minnum = [nums[-1]]*n
        for i in range(n-2, -1, -1):
            minnum[i] = min(minnum[i+1], nums[i])
        
        maxnum = nums[0]
        for i in range(0, n):
            maxnum = maxnum if maxnum > nums[i] else nums[i]
            if maxnum - minnum[i] <= k:
                return i
        
        return -1
