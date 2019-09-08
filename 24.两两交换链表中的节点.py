#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Easy (61.94%)
# Likes:    272
# Dislikes: 0
# Total Accepted:    37.2K
# Total Submissions: 60K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = dummy = ListNode(0)  # 定义一个虚拟的头结点，它指向“首节点”head
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            # 通过画链表图得到交换逻辑
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next
