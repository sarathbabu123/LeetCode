class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq_dict = {}
        for char in s:
            freq_dict[char] = freq_dict.get(char,0) +1
        unsorted_keys = freq_dict.keys()
        results = []
        sorted_keys = sorted(freq_dict, key = lambda char: freq_dict[char], reverse = True)
        for char in sorted_keys:
            results.append(char*freq_dict[char])

        return "".join(results)
