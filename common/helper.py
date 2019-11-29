class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def arrayToLinkList(array):
    lst = list()
    for i in array:
        node = ListNode(i)
        lst.append(node)

    for i in range(0, len(lst) - 1):
        lst[i].next = lst[i + 1]

    return lst[0]


def printLinkedList(head):
    p = head
    while p:
        print(p.val)
        p = p.next