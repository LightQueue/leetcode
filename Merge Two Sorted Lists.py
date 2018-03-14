#1st edition 52ms
class Solution:
    def mergeTwoLists(self, l1, l2):
        if None in (l1,l2):
            return l1 or l2
        result = node = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else :
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1 or l2:
            node.next = l1 or l2
        return result.next
        
'''
中规中矩的解法，对每个节点进行比较，没什么亮点
'''
