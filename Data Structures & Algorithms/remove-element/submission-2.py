class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read, write = 0,0

        for read in range(len(nums)):
            if nums[read] == val:
                nums[read] = "_"
            else:
                nums[write] = nums[read]
                write += 1
        return write


        