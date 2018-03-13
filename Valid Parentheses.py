#1st edition 44ms
class Solution:
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for par in s:
            if par in dict.values():
                stack.append(par)
            elif par in dict.keys():
                if stack==[] or dict[par] != stack.pop():
                    return False
            else:
                return False
        return stack==[]

'''
一开始的想法是按对称来做，后来发现给出的字符串
不一定就是对称的，所以使用配对来做。适合配对的
数据结构有字典和栈。python的list可以当栈使用。
'''