#!/usr/bin/env python


#Definition for singly-linked list.
class ListNode:
    """
    定义节点类
    val:数据
    next:指向下一节点
    """
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        len = 0
        k = 0

        while node1 or node2:
            try:
                val1 = node1.val
                node1 = node1.next
            except AttributeError:
                val1 = 0
            try:
                val2 = node2.val
                node2 = node2.next
            except AttributeError:
                val2 = 0

            temp = val1 + val2 + k
            k = int(temp / 10)
            if len == 0:
                head = ListNode(temp % 10)
                pnode = head
            else:
                pnode.next = ListNode(temp % 10)
                pnode = pnode.next
            len += 1

        if k != 0:
            pnode.next = ListNode(k)

        return head
