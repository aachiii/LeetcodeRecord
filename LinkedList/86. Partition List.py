'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Time Complexity O(n), space Complexity O(1)
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = left = ListNode(0)
        dummy2 = right = ListNode(0)

        while head:
            print(head.val, left.val, right.val)
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
            head = head.next

        left.next = None
        right.next = None
        left.next = dummy2.next

        return dummy1.next

'''
Two Pointer, keep maintaining 2 linkedlist, and then combine them in the end. Need to track the head of each linkedlist.
'''