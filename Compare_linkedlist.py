def compare_lists(llist1, llist2):
    while(llist1 != None and llist2 != None):
        if(llist1.data != llist2.data):
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
    if(llist1 != None or llist2 != None):
        return 0

    return 1
