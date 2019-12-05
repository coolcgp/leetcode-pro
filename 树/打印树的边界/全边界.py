class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def getHeight(self, root, level):
        if not root:
            return level
        else:
            return max(self.getHeight(root.left, level + 1), self.getHeight(root.right, level + 1))

    def printEdge(self, root):
        height = self.getHeight(root, 0)
        edgeArray = [[None] * 2 for x in range(height)]
        self.setEdge(root, 0, edgeArray)
        for array in edgeArray:
            print("left:", array[0].val)
        self.printNotInMap(root, 0, edgeArray)
        for array in edgeArray:
            if array[1] and array[1] != array[0]:
                print("right:", array[1].val)

    def setEdge(self, curNode, level, edgeArray):
        if not curNode:
            return
        edgeArray[level][0] = curNode if not edgeArray[level][0] else edgeArray[level][0]
        edgeArray[level][1] = curNode
        self.setEdge(curNode.left, level + 1, edgeArray)
        self.setEdge(curNode.right, level + 1, edgeArray)

    def printNotInMap(self, curNode, level, edgeArray):
        if not curNode:
            return
        if not curNode.left and not curNode.right and (
                curNode != edgeArray[level][0] and curNode != edgeArray[level][1]):
            print("mid:", curNode.val)
        else:
            self.printNotInMap(curNode.left, level + 1, edgeArray)
            self.printNotInMap(curNode.right, level + 1, edgeArray)


"""
        50
       /  \
     30   100
    / \   / \
   20 40 80 120  
"""

node50 = TreeNode(50)
node30 = TreeNode(30)
node100 = TreeNode(100)
node20 = TreeNode(20)
node40 = TreeNode(40)
node80 = TreeNode(80)
node120 = TreeNode(120)

node50.left = node30
node50.right = node100
node30.left = node20
node30.right = node40
node100.left = node80
node100.right = node120

Solution().printEdge(node50)

exit(0)
