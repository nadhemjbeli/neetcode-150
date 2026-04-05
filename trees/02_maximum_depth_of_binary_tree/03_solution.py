from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative DFS

    # Time  — O(n): every node visited exactly once
    # Space — O(h): stack holds at most h levels deep at any time
    # O(log n) balanced tree, O(n) worst case skewed tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
    
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