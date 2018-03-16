#1st edition 52ms
class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
        
'''
python 内置函数三行解法
'''
