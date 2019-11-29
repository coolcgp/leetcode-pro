from common.helper import arrayToLinkList, printLinkedList
from common.helper import ListNode


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next = node.next
        if next:
            node.next = next.next
            node.val = next.val
        else:
            node.val = None
            node.next = None


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
solution.deleteNode(head)
printLinkedList(head)
