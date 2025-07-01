def convert_to_list(number: int) -> Node:
    """
        converts a positive integer into a (reversed) linked list.
        for example: give 112
        result 2 -> 1 -> 1
    """
    if number >= 0:
        head = Node(0)
        current = head
        remainder = number % 10
        quotient = number // 10

        while quotient != 0:
            current.next = Node(remainder)
            current = current.next
            remainder = quotient % 10
            quotient //= 10
        current.next = Node(remainder)
        return head.next
    else:
        print("number must be positive!")