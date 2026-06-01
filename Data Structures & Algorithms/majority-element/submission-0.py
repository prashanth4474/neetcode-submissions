class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_threshold = math.ceil(len(nums)/2)
        frequency_map = defaultdict(lambda: 0)

        for num in nums:
            frequency_map[num] += 1
            if frequency_map[num] >= majority_threshold:
                return num

        