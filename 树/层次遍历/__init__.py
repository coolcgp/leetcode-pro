from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hierarchicalPrint(self, root):
        queue = deque()
        queue.append(root)

        level = 1
        last = root
        nLast = TreeNode(None)

        while queue:
            curHead = queue.popleft()
            print("cur_value=", curHead.val, ", 当前值", level)
            if curHead.left:
                queue.append(curHead.left)
                nLast = curHead.left
            if curHead.right:
                queue.append(curHead.right)
                nLast = curHead.right

            if curHead == last and queue:
                level += 1
                last = nLast


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
solution = Solution()
solution.hierarchicalPrint(node1)
