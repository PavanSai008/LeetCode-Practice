class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen={}
        for r in range(len(numbers)):
            if numbers[r] in seen:
                return [seen[numbers[r]]+1,r+1]
            seen[target-numbers[r]]=r