class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
        }
        num = 0
        for i in range(len(s)-1):
            if roman_map[s[i]]>= roman_map[s[i+1]]:
                num += roman_map[s[i]]
            else:
                num -= roman_map[s[i]]
        num += roman_map[s[-1]]

        return num