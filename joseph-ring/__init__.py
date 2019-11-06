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

    lst[len(lst) - 1].next = lst[0]
    return lst[0]


def printLinkedList(head):
    p = head
    while p:
        print(p.val)
        p = p.next


def josephRing(head, num):
    last = head
    while last.next != head:
        last = last.next

    count = 0
    while head != last:
        count = count + 1
        if count == num:
            last.next = head.next
            count = 0
        else:
            last = last.next
        # 尾部后移一个，头部后移一个位置。实在是太美味了，齿有余香呀。
        head = last.next
    return head.val


array = [0, 1, 2, 3, 4]
head = arrayToLinkList(array)
print("count result:", josephRing(head, 2))
