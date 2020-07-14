def flatten(head):
    def clean(node):
        cur = node
        if cur.child:
            nxt = cur.next
            nh, nl = clean(cur.child)
            cur.next = nh
            nl.next = nxt
            nh.prev = cur
            if nxt:
                nxt.prev = nl
            cur.child = None
        last = cur
        while cur:
            if cur.child:
                nxt = cur.next
                nh, nl = clean(cur.child)
                cur.next = nh
                nl.next = nxt

                nh.prev = cur
                if nxt:
                    nxt.prev = nl
                cur.child = None
            last = cur
            cur = cur.next
        return node, last
    if head:
        h, t = clean(head)
    return head
