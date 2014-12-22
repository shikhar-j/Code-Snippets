class ListNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.child = None
        self.value = None


def flatten(current, last):
    """
    current = head
    last = tail
    """
    head = current
    while current.next != None:
        if current.child:
            tail = current.next
            current.next = flatten(current.child, tail)
            current.child = None
            current = tail
        else:
            current = current.next

    last.prev = current
    current.next = last
    return head

def initList():
    head = ListNode()
    head.next = ListNode()
    head.child = ListNode()
    head.value = 1
    head.next.value = 2
    head.next.prev = head
    head.next.child = ListNode()
    head.next.child.value = 3
    head.next.child.next = ListNode()
    head.next.child.next.value = 4
    head.next.child.next.next = ListNode()
    head.next.child.next.next.value = 5
    head.next.child.next.next.child = ListNode()
    head.next.child.next.next.child.value = 6
    head.next.child.next.next.child.next = ListNode()
    head.next.child.next.next.child.next.value = 7
    head.next.child.next.next.child.next.next = ListNode()
    head.next.child.next.next.child.next.next.value = 8
    head.child = None
    next = head.next
    next.next = ListNode()
    next = next.next
    next.value = 9
    next.next = ListNode()
    next = next.next
    next.value = 10
    next.child = ListNode()
    next.child.value = 11
    next.child.next = ListNode()
    next.child.next.value = 12
    next.next = ListNode()
    next = next.next
    next.value = 13

    return head

def printList(list):
    current = list
    while current.next != None:
        print current.value
        current = current.next
    
    return current
