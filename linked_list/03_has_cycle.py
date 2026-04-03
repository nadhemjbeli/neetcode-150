from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity - O(n): looping through the whole list items 
    # to check if the linkedList has a cycle
    # Space complexity - O(1): just two variable pointers 
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# main test cases
if __name__ == "__main__":
    s = Solution()
    # list: 3 -> 2 -> 0 -> -4 -> 2 (cycle)
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next # create cycle
    print(s.hasCycle(head)) # -> True

    # list: 1 -> 2 -> None (no cycle)
    head = ListNode(1, ListNode(2))
    print(s.hasCycle(head)) # -> False