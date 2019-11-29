class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverse(self, stack):
        if not stack:
            return None
        # 阴险的一步：翻转后，会形成循环链
        last = stack[len(stack) - 1].next
        dummyHead = ListNode(None)
        p = dummyHead
        while stack:
            node = stack.pop()
            p.next = node
            p = p.next
        p.next = last
        return dummyHead.next

    def reverseKGroup(self, head, k):
        """
        1 -> 2 -> 3 -> 4 -> 5
        卡了我一下，但是我还是给你干出来了！！！
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        stack = list()
        rst = ListNode(None)
        cur = rst
        while p or len(stack) == k:
            count = 0
            if len(stack) == k:
                subHead = self.reverse(stack)
                cur.next = subHead
                count += 1
                while count <= k:
                    cur = cur.next
                    count += 1
                stack = list()
            if p:
                stack.append(p)
                p = p.next

        return rst.next


def arrayToLinkList(array):
    lst = list()
    for i in array:
        node = ListNode(i)
        lst.append(node)

    for i in range(0, len(lst) - 1):
        lst[i].next = lst[i + 1]

    return lst[0]


def printList(head):
    p = head
    while p:
        print(p.val)
        p = p.next


array = [1, 2, 3, 4, 5, 6]
k = 2
head = arrayToLinkList(array)
solution = Solution()
rst = solution.reverseKGroup(head, k)
printList(rst)
