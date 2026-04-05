from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative BFS

    # Time  — O(n): every node visited exactly once
    # Space — O(w): queue holds at most one full level at a time
    # w is the maximum width of the tree
    # O(n) worst case when the last level holds n/2 nodes
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level
    
# main test cases
if __name__ == "__main__":
    s = Solution()
    # tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.maxDepth(root)) # -> 3

    # tree: [1,null,2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(s.maxDepth(root)) # -> 2

    # tree: []
    print(s.maxDepth(None)) # -> 0