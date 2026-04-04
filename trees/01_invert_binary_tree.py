# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time - O(n): every node on the tree is visited exactly once
    # Space - O(n): recursion call stack depth equals tree height h
    # O(log n) for balanced tree, O(n) worst case for skewed tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# main test cases
if __name__ == "__main__":
    s = Solution()
    # tree: [4,2,7,1,3,6,9]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print(s.invertTree(root)) # -> [4,7,2,9,6,3,1]

    # tree: [2,1,3]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(s.invertTree(root)) # -> [2,3,1]

    # tree: []
    print(s.invertTree(None)) # -> None