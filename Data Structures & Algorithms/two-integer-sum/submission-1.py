class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # optimized space complexity solution track hash map as we traverse the array
        seen = {}

        for i,num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            # print(seen)
        return []
