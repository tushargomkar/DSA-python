class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2147483648 or x > 2147483647:
            return 0
        
        rnum = 0
        negative = x < 0
        n = abs(x)
        
        while n > 0:
            rem = n % 10
            rnum = rnum * 10 + rem
            n = n // 10
            
            # Check for overflow before updating rnum
            if rnum > 2147483647:  # If rnum exceeds 32-bit signed integer max
                return 0
        
        return -rnum if negative else rnum
