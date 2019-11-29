import collections

class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        map = collections.OrderedDict()
        p = head
        while p:
            map[p] = Node(p.val, None, None)
            p = p.next

        p = head
        while p:
            if p.random:
                map[p].random = map[p.random]
            p = p.next

        dummyHead = Node(None, None, None)
        p = dummyHead
        for i in map.values():
            p.next = i
            p = p.next

        return dummyHead.next


node2 = Node(2, None, None)
node2.random = node2
node1 = Node(1, node2, None)

solution = Solution()
head = solution.copyRandomList(node1)
print(head)
