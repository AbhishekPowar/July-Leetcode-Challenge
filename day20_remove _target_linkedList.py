def removeElements(head, val):
    def remove(head, tar):
        if head:
            root = ListNode('root')
            root.next = head
            cur = root
            while cur.next and cur.next.val != tar:
                cur = cur.next
            if cur.next and cur.next.val == tar:
                cur.next = remove(cur.next.next, tar)
            return root.next
        else:
            return head
    return remove(head, val)

# Iterative


def removeElements(head, val):
    root = ListNode('root')
    root.next = head
    cur = root
    while cur:
        if cur.next and cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return root.next
