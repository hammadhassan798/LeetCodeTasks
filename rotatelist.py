class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rotateRight(head, k):

    # Empty list or one node
    if head is None or head.next is None:
        return head

    # Find length and last node
    temp = head
    count = 1

    while temp.next:
        temp = temp.next
        count += 1

    # Avoid unnecessary rotations
    k = k % count

    if k == 0:
        return head

    # temp is currently the last node
    last = temp

    # Find new tail
    temp = head

    for i in range(count - k - 1):
        temp = temp.next

    # Node after new tail becomes new head
    new_head = temp.next

    # Connect old tail to old head
    last.next = head

    # Break the list
    temp.next = None

    return new_head


# -------------------------
# Create Linked List
# -------------------------

head = Node(1)

head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


# -------------------------
# Rotate
# -------------------------

k = 2

head = rotateRight(head, k)


# -------------------------
# Print Linked List
# -------------------------

temp = head

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")