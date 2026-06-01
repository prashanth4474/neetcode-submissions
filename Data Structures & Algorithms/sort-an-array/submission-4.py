class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def bubbleSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    def selectionSort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # left, right = 0

        for l in range(n-1):
            smallest = l
            for r in range(l+1, n):
                # smallest = nums[l]
                
                if nums[r] < nums[smallest]:
                    smallest = r
            nums[l], nums[smallest] = nums[smallest], nums[l]
        return nums

    def insertionSort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(1, n):
            current_item = nums[i]

            j = i-1

            while j >= 0 and nums[j] > current_item:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = current_item
        return nums

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        left_half = nums[:mid]
        right_half = nums[mid:]
        self.mergeSort(left_half)
        self.mergeSort(right_half)

        i,j,k = 0,0,0

        while i < len(left_half) and j < len(right_half):
            if(left_half[i] < right_half[j]):
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1
        return nums
        





        