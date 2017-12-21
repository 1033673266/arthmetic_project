# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l = ListNode(0)
        curt = l
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while l1 is not None or l2 is not None:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            sum = l1_val + l2_val + carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            carry = sum // 10
            value = sum % 10
            curt.val = value
            if l1 is not None or l2 is not None or carry:
                curt.next = ListNode(carry)
                curt = curt.next

        return l


n1 = (2, 4, 3)
n2 = (5, 6, 4)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

a = Solution.addTwoNumbers(l1, l2)
print(a)
