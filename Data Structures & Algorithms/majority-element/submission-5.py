class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Hint 2
        Think about the problem like a series of 'battles'. 
        Since the majority element appears more than half the time, if every unique number 'fought' the majority element and both were removed, the majority element would be the last one standing.

        Hint 3
        Try the Boyer-Moore Voting Algorithm. You maintain a candidate and a count. 
        When you see the same number as the candidate, increase the count. 
        When you see a different number, decrease the count. 
        If the count hits zero, pick a new candidate.

        """
        candidate = None
        vote = 0
        for i,num in enumerate(nums):
            if vote == 0:
                candidate = num
            if num == candidate:
                vote += 1
            else:
                vote -= 1
            
        return candidate
        