#1st edition 132ms
class Solution:
    def romanToInt(self, s):
        digits = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result,maxdigit = 0,1
        for i in range(len(s)-1,-1,-1):
            if digits[s[i]] >= maxdigit:
                maxdigit = digits[s[i]]
                result += digits[s[i]]
            else:
                result -= digits[s[i]]
        return result
        

