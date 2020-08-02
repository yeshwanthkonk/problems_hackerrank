def reverse(head):
    ptr = head
    prev = None
    curr = None
    while(ptr is not None):
        curr = ptr
        ptr = ptr.next
        curr.next = prev
        prev = curr

    return curr
