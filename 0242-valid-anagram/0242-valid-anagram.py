class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        freq = [0]*26
        for char in s.lower():
            freq[ord(char) - ord("a")] +=1
        for char in t.lower():
            freq[ord(char) - ord("a")] -=1
        return all(f == 0 for f in freq)
        