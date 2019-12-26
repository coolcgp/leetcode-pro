import collections


class TreeNode(object):
    def __init__(self, x):
        self.id = x
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.map = dict()

    def recursionCountDepth(self, curNode, curDepth):
        if not curNode:
            return
        self.map[curNode.id] = curDepth
        # 计算左分支
        self.recursionCountDepth(curNode.left, curDepth + 1)
        # 计算右分支
        self.recursionCountDepth(curNode.right, curDepth + 1)

    def countDepth(self, root):
        self.recursionCountDepth(root, 0)

    def search(self, root, searchNode):
        self.countDepth(root)
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
node40.right = node35

solution = Solution()
rst = solution.search(node50, node120)
print(rst)

exit(0)
