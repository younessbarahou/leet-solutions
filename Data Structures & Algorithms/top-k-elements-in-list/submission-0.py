class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result: Dict[str, int] = {}
        for num in nums:
            if f"{num}" in result:
                result[f"{num}"] += 1
            else:
                result.update({f"{num}": 1})
        result = sorted(result, key= lambda x: result[x], reverse=True)
        return result[:k]