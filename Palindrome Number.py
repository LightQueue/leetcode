#2nd edition 272ms
class Solution:
    def isPalindrome(self, x):
        return True if x == int(str(abs(x))[::-1]) else False

#1st edition 272ms
class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        else :
            return True if x == int(str(x)[::-1]) else False

'''
第二版受到discuss上的启发，把判断语句消去了。
当x是负数时，|x|!=x

还有一种方法是用reverse integer里面的方法，
逆转x之后与原x对比
'''

