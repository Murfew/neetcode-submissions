# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        values= []
        
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        res = ListNode()
        curr = res
        for i in range(len(values) - 1, -1, -1):
            curr.val = values[i]

            if not i == 0:
                curr.next = ListNode()
                curr = curr.next

        return res
