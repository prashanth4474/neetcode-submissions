class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using list and inbuilt sort
        if len(s) != len(t):
            return False
        s1 = list (s)
        s2 = list(t)
        s1.sort()
        s2.sort()
        # print(s1, s2)
        if s1 == s2:
            return True
        return False