from common.helper import arrayToLinkList


def isPalindorme(head):
    stack = list()
    p = head
    while p:
        stack.append(p)
        p = p.next

    rst = True
    while head:
        if head.val != stack.pop().val:
            rst = False
            break
        else:
            head = head.next

    return rst


array = [1, 2, 3, 2, 2]
head = arrayToLinkList(array)
print(isPalindorme(head))
