class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result: List[List[int]] = []
        nums_set: set[int] = {n for n in nums}
        if len(nums_set) == 0:
            return 0
        for num in nums_set:
            temp: List[int] = [num]
            if num - 1 in nums_set:
                continue
            else:
                jndex: int = 1
                while num + jndex in nums_set:
                    temp.append(num + jndex)
                    jndex += 1
                result.append(temp)
        return len(max(result, key= lambda x: len(x)))