#2nd edition 60ms
class Solution:
    def reverse(self, x):
        x=int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
        return x if x.bit_length() < 32 else 0

#1st edition 60ms
class Solution:
    def reverse(self, x):
        flag = -1 if x < 0 else 1
        y,x=0,abs(x)    
        while x:
            y = y*10 + x%10
            x//=10
        y=flag*y
        return y if y < 2147483648 and y >= -2147483648 else 0 
        
'''
第一版是最常见的思路循环除法，另外一开始也想到使用字符串，
于是就有了第二版，直接倒置字符串

p.s. 一开始不知道python3的/符号改成了真除，结果一直是inf，
leetcode里面也没有log，还以为是循环写错了－_－b 

p.p.s 另外第二版一开始使用的判断条件是
return x if x >= -2147483648 and x < 2147483648 else 0 
改成了return x if x.bit_length() < 32 else 0之后从56ms
变成了60ms－_－b  Run code的时候明明节省了10多ms啊o(≧口≦)o
'''
