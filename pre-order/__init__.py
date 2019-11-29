class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def peek(self, stack):
        if len(stack) == 0:
            return None
        return stack[len(stack) - 1]

    def postorderTraversal(self, root):
        """
        这是迄今为止，我写的最喜欢的leetcode代码
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = list()
        stack.append(root)
        f = TreeNode(None)
        lst = list()
        while stack:
            cur = self.peek(stack)
            if (cur.right or cur.left) and not (f == cur.left or f == cur.right):
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
            else:
                v = stack.pop()
                lst.append(v.val)
                f = v

        return lst


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node6.right = node7

solution = Solution()
lst = solution.postorderTraversal(node1)
print(lst)
