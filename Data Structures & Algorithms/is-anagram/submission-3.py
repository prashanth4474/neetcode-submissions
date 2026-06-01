class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using sorted, returns a new list
        #  .sort() sorts a list in place, cannot use on strings as they are immutable
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)