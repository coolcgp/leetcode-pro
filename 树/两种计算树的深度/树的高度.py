class TreeNode(object):
    def __init__(self, x):
        self.id = x
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.map = dict()

    def countHeight(self, node):
        if not node:
            return 0
        else:
            leftHeight = self.countHeight(node.left) + 1
            rightHeight = self.countHeight(node.right) + 1
            height = max(leftHeight, rightHeight)
            self.map[node.id] = height
            return height

    def search(self, root, searchNode):
        self.countHeight(root)
        if searchNode.id in self.map:
            return self.map[searchNode.id]
        else:
            return -1


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
depth = solution.search(node50, node30)
print(depth)

exit(0)
