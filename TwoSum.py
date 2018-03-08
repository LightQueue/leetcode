#2nd edition 376ms
class Solution:
    def twoSum(self, nums, target):
        newtarget=[]
        for i in range(len(nums)):
            if(nums[i] in newtarget):
                return nums.index(target-nums[i]),i
            else:
                newtarget.append(target-nums[i])

#1st edition 6472ms
class Solution:
    def twoSum(self, nums, target):
        numslen = len(nums)
        for i in range(numslen):
            for j in range(i+1,numslen):
                if(nums[i]+nums[j]==target):
                    return i,j
        return 0,0
        
'''
相比第一版，第二版节省了大量时间（从O（n^2）到O(n)）
原因是第一版嵌套循环在循环过程中并未生成新的可供参考
的信息，而第二版循环时会生成协助判断的信息列表newtarget
p.s. discuss上有很多答案使用了dict

然并卵，还是没有嵌套循环的cpp跑得快
'''
