"""
@author: raymondchen
@date: 2018/8/30
Description:
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        m_list = ListNode(0)
        tail_node = m_list
        while l1 is not None or l2 is not None:
            m_value = l1.val + l2.val + flag
            if m_value >= 10:
                flag = 1
                m_value -= 10
            else:
                flag = 0
            temp_node = ListNode(m_value)
            tail_node.next = temp_node
            tail_node = tail_node.next
            if l1.next is None and l2.next is None:
                break
            l1 = l1.next if l1.next is not None else ListNode(0)
            l2 = l2.next if l2.next is not None else ListNode(0)
        if flag == 1:
            tail_node.next = ListNode(1)

        return m_list.next



