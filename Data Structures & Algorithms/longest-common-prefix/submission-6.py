class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """ 
        * vertical compare is good
        * no need to find the shortest length, just check length on compare
        * we can anchor to the first char no need to compare current vs next
        * if same continue, else return tracked prefix
        """

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]

        