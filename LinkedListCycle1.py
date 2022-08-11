# https://www.youtube.com/watch?v=gBTe7lFR3vc&ab_channel=NeetCode

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution1 - using set (hash):
class Solution1(object):
    def hasCycle(self, head):
        node_set = set()
        while head:
            if head in node_set:
                return True
            else:
                node_set.add(head)
                head = head.next
        return False


# Solution2 - using 2x pointers:
class Solution2(object):
    def hasCycle(self, head):
        pointer_fast = head
        pointer_slow = head
        while pointer_fast and pointer_fast.next:
            pointer_slow = pointer_slow.next
            pointer_fast = pointer_fast.next.next
            if pointer_slow == pointer_fast:
                return True
        return False



if __name__ == '__main__':
    def linkedIn(x):
        if x == 0:
            return None
        else:
            node = ListNode(x)
            node.next = linkedIn(x-1)
            return node
    head1 = linkedIn(10)

    head2 = ListNode(0)
    node = head2
    for i in range(1, 10):
        new_node = ListNode(i)
        if i == 3:
            node3 = new_node
        node.next = new_node
        node = node.next
     # create loop into node 3
    node.next = node3

    """
    node = head2
    i = 0
    while node and i < 10:
        i += 1
        print(node.val)
        node = node.next
    """

    head_test = head1

    obj1 = Solution1()
    print(obj1.hasCycle(head_test))

    obj2 = Solution2()
    print(obj2.hasCycle(head_test))

