# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    cache = {}

    newlist = []

    while node:
        for i in node:
            if i in cache:
                newlist.append(i)

            else:
                newlist.append(i)
    return newlist














node = [3, 4, 3, 2, 6, 1, 2, 6]
# Expected Output: [3, 4, 2, 6, 1]


print(node)
print(condense_linked_list(node))
