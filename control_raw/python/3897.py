def kth_to_last_dict(head, k):
    """
    This is a brute force method where we keep a dict the size of the list
    Then we check it for the value we need. If the key is not in the dict,
    our and statement will short circuit and return False
    """
    if not (head and k > -1):
        return False
    d = dict()
    count = 0
    while head:
        d[count] = head
        head = head.next
        count += 1
    return len(d)-k in d and d[len(d)-k]