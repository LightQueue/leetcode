#1st edition 36ms
class Solution:
    def lengthOfLastWord(self, s):
        lens=0
        s=s.strip()
        if not s:
            return 0
        for s in s[-1::-1]:
            if s != ' ':
                lens += 1
            else :
                break
        return lens
		
'''
python内置函数真好用
'''