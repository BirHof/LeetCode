# https://www.youtube.com/watch?v=XVuQxVej6y8&ab_channel=NeetCode

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# going over the list twice O(2n):
# not working with list length 1 !!!
class Solution1(object):
    def removeNthFromEnd(self, head, n):

        node = head
        serial = 0
        while node:
            serial += 1
            if node.next is None:
                break
            else:
                node = node.next

        if n == 0:
            return head
        if n > serial:
            return None

        node = head
        new_last_i = serial - n
        idx = 1
        while idx < new_last_i:
            idx += 1
            node = node.next

        node.next = node.next.next
        return head

# going over the list once O(n):
class Solution2(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        point_left = dummy
        point_right = head

        while n > 0 and point_right:
            point_right = point_right.next
            n -= 1

        while point_right:
            point_right = point_right.next
            point_left = point_left.next

        point_left.next = point_left.next.next

        return dummy.next





def linkedIn(x):
    if x == 0:
        return None
    else:
        node = ListNode(x)
        node.next = linkedIn(x-1)
        return node

# create LL 5-4-3-2-1:
head1 = linkedIn(10)

# create LL 1-2-3-4-5:
head2 = ListNode(0)
node = head2
for i in range(0):
    node.next = ListNode(i)
    node = node.next

i = 0
node = head2
while node:
    print(f"Node: {i}, val: {node.val} Add: {node}")
    i += 1
    node = node.next
print("")


obj1 = Solution2()
ans = obj1.removeNthFromEnd(head2, 1)
print(ans)


i = 0
node = ans
while node:
    print(f"Node: {i}, val: {node.val} Add: {node}")
    i += 1
    node = node.next

