class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for i, num in enumerate(nums):
            if num == val:
                nums[i] = 51
                k -= 1
        nums.sort()
        # print(nums)
        return k

        