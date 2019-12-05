class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left) + 1
        right = self.getHeight(root.right) + 1
        return max(left, right)

    def priGetHeight(self, node, level):
        if not node:
            return level
        left = self.priGetHeight(node.left, level + 1)
        right = self.priGetHeight(node.right, level + 1)
        return max(left, right)

    def countHeight(self, root):
        return self.priGetHeight(root, 0)


"""
        50
       /  \
     30   100
    / \   / \
   20 40 80 120  
       \
       35     
"""

node50 = TreeNode(50)
node30 = TreeNode(30)
node100 = TreeNode(100)
node20 = TreeNode(20)
node40 = TreeNode(40)
node80 = TreeNode(80)
node120 = TreeNode(120)
node35 = TreeNode(35)

node50.left = node30
node50.right = node100
node30.left = node20
node30.right = node40
node100.left = node80
node100.right = node120
node40.left = node20
node40.right = node35

solution = Solution()
height = solution.countHeight(node50)
print(height)

exit(0)
