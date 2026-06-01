class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Used array frequency map method
        lists, dicts cannot be used as keys in dict as they mutable
        convert list to tuples
        compare frequency tuple and track in the hash map
        merged hashmap values to  a single list
        """
        freq_maps = defaultdict(list)
        # print(freq_maps)

        for s in strs:
            s_freq_list = self.getFreqMap(s)
            freq_maps[s_freq_list].append(s)
        
        return [val for val in freq_maps.values()]


    def getFreqMap(self, s: str) -> dict:
        freq_list = [0] * 26
        for char in s:
            i = ord(char) - ord('a')
            freq_list[i] += 1
        return tuple(freq_list)
        
        