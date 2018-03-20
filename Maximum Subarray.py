#1st edition 56ms
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        maxsum=cur=nums[0]
        for i in nums[1:]:
            cur=max(i,cur+i)
            maxsum=max(cur,maxsum)
        return maxsum
        
'''
'''
