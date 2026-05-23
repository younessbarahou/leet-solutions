class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index: int = 0
        while index < len(nums) - 1:
            jndex: int = index + 1
            while jndex < len(nums):
                if nums[index] + nums[jndex] == target:
                    return [index, jndex]
                jndex += 1
            index += 1
        