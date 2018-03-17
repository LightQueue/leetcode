#1st edition 40ms
class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        nums.append(target)
        nums.sort()
        return nums.index(target)
        
        
'''
我今天就是累死，也不用python内置函数
呵呵，内置函数真好用
'''
