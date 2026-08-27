class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        for j in range(i, len(nums)):
            if nums[j] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
