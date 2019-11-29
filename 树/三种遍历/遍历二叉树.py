class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pre_order(self, root):
        if not root:
            return
        print(root.val)
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)

    def mid_order(self, root):
        if not root:
            return
        self.mid_order(root.left)
        print(root.val)
        self.mid_order(root.right)

    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val)

    def pre_order_no_recursion(self, root):
        if not root:
            return

        stack = list()
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            print(cur_node.val)
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)

    def mid_order_no_recursion(self, root):
        if not root:
            return
        stack = list()
        cur_node = root
        while stack or cur_node:
            if cur_node:
                stack.append(cur_node)
            if cur_node and cur_node.left:
                cur_node = cur_node.left
            else:
                node = stack.pop()
                print(node.val)
                if node.right:
                    cur_node = node.right
                else:
                    cur_node = None

    def post_order_no_recursion(self, root):
        if not root:
            return
        stackA = list()
        stackB = list()
        stackA.append(root)
        while stackA:
            node = stackA.pop()
            stackB.append(node)
            if node.left:
                stackA.append(node.left)
            if node.right:
                stackA.append(node.right)

        while stackB:
            node = stackB.pop()
            print(node.val)

    def post_order_no_recursion_single_stack(self, root):
        if not root:
            return

        stack = list()
        stack.append(root)
        top = TreeNode(None)
        lastPop = TreeNode(None)
        while stack:
            # 看栈顶
            top = stack[len(stack) - 1]
            # 如果栈顶有子节点，就进栈；但是刚弹出元素就是栈顶元素的子节点，就不要重复进栈了。
            if (top.left or top.right) and lastPop is not top.right and lastPop is not top.left:
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
            else:
                lastPop = stack.pop()
                print(lastPop.val)


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
# node30.left = node20
node30.right = node40
node100.left = node80
node100.right = node120
node40.left = node20

solution = Solution()
solution.post_order_no_recursion_single_stack(node50)

exit(0)
