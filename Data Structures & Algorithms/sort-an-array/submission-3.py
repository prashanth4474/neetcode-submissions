class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.selectionSort(nums)

    def bubbleSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    def selectionSort(self, nums: List[int]) -> List[int]:
        n= len(nums)

        # left, right = 0

        for l in range(n-1):
            smallest = l
            for r in range(l+1, n):
                # smallest = nums[l]
                
                if nums[r] < nums[smallest]:
                    smallest = r
            nums[l], nums[smallest] = nums[smallest], nums[l]
        return nums

        