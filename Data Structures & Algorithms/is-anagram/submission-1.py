class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using hashmap
        if len(s) != len(t):
            return False
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        # print(seen)
        for char in t:
            if char in seen:
                seen[char] -= 1
                if seen[char] < 0:
                    return False
            else:
                return False
        return True
        