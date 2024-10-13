class Solution(object):
    def reverse(self,n):
        if n < -2147483648 or n > 2147483647:
           return 0
       
        rnum=0
        negative=n<0
        n=abs(n)
        while n>0:
            rem=n%10
            rnum=rnum*10+rem
            n=n//10
        if rnum>pow(2,31):
            return 0
        return -rnum if negative else rnum


    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
         return False
        return x ==self.reverse(x)




    # class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     x = str(x)
    #     return x == x[::-1]
