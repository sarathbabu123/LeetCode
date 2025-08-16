class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31-1
        INT_MIN = -2**31

        n = len(s)
        i = 0
        while i<n and s[i] == " ":
            i+=1
        
        sign = 1
        if i<n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i+=1
        
        num = 0
        while i<n and s[i].isdigit():
            if num>INT_MAX//10 or (num == INT_MAX//10 and int(s[i]) > 7):
                return INT_MAX if sign == 1 else INT_MIN
            num = num*10 + int(s[i])
            i+=1
        return sign*num
            