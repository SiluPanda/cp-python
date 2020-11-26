import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root, memo):
        if root == None:
            return
        left, right = [0, 0], [0, 0]
        if root.left:
            if root.left not in memo:
                self.helper(root.left, memo)
            left = memo[root.left]
        if root.right:
            if root.right not in memo:
                self.helper(root.right, memo)
            right = memo[root.right]
        #take this node, have to skip it's children
        take = left[0] + right[0] + root.val
        #skip this node, can take it's children
        skip = max(left) + max(right)
        memo[root] = [skip, take]

    def rob(self, root) -> int:
        memo = {}
        if root == None:
            return 0
        self.helper(root, memo)
        return max(memo[root])
            

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(sol.rob(root))
