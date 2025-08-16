class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = 0
        maximum= 0
        for char in s:
            if char  == "(":
                curr +=1
            elif char == ")":
                curr -=1
            if curr>maximum:
                maximum = curr

        return maximum
            

        