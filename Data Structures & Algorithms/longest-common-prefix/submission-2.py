class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        n = len(strs)
        if n == 1:
            return strs[0]
        shortest = 300
        for i in range(n):
            item_len = len(strs[i])
            # print(item_len)
            if item_len < shortest:
                shortest = len(strs[i])

        for i in range(shortest):
            # print(len(strs[i]))
            for j in range(n-1):
                if strs[j][i] == strs[j+1][i]:
                    continue
                else:
                    return prefix
            prefix += strs[j-1][i]
        return prefix
            

        