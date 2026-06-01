class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {value: i for  i, value in enumerate(nums)}
        
        for i in range(len(nums)):
            reqd = target - nums[i]
            if reqd in seen and seen[reqd] != i:
                return [i, seen[reqd]]
        return []
