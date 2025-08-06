class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        reversed_s = ""
        for i in range(len(words)):
            word = words.pop()
            if not word == "":
                reversed_s =reversed_s+ word + " "
        
        return reversed_s.strip()
        