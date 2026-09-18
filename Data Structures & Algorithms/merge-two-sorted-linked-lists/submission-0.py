# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        res = None
        currRes = None

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                if not currRes:
                    currRes = ListNode(curr1.val)
                    res = currRes
                else:
                    currRes.next = ListNode(curr1.val)
                    currRes = currRes.next
                
                curr1 = curr1.next
                
            else:
                if not currRes:
                    currRes = ListNode(curr2.val)
                    res = currRes
                else:
                    currRes.next = ListNode(curr2.val)
                    currRes = currRes.next

                curr2 = curr2.next

        if curr1:
            if currRes:
                currRes.next= curr1
            else:
                return curr1
        else:
            if currRes:
                currRes.next = curr2
            else:
                return curr2

        return res

