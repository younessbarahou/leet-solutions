class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: Dict[str, List[str]] = {}
        for string in strs:
            if f"{sorted(string)}" in result:
                result[f"{sorted(string)}"].append(string)
            else:
                result.update({f"{sorted(string)}": [string]})
        return [r for r in result.values()]
