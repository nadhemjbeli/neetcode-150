from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time - O(n + m): every node from both list is visted exactly once
    # Space - O(1): no new nodes created, just pointers rewired
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next

# main test cases
if __name__ == "__main__":
    s = Solution()
    # list1: 1 -> 2 -> 4 -> None
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    # list2: 1 -> 3 -> 4 -> None
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged_head = s.mergeTwoLists(list1, list2)
    # print the merged linked list
    while merged_head:
        print(merged_head.val) # -> 1, 1, 2, 3, 4, 4
        merged_head = merged_head.next