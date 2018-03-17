#2nd edition 36ms
class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)
#1st edition 52ms
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
'''
中规中矩的解法，遍历haystack，没什么亮点
最简单的仍然是python的内置函数
'''
