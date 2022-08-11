
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution - using set (hash):
class Solution(object):
    def detectCycle(self, head):
        node_set = set()
        node = head
        while node:
            if node in node_set:
                junction = node
                pointer_finder = head
                #j = 0
                while pointer_finder:
                    if pointer_finder == junction:
                        return junction
                    else:
                        #j += 1
                        pointer_finder = pointer_finder.next
            else:
                node_set.add(node)
                node = node.next

        return None





if __name__ == '__main__':
    def linkedIn(x):
        if x == 0:
            return None
        else:
            node = ListNode(x)
            node.next = linkedIn(x-1)
            return node


    # create LL without loop:
    head1 = linkedIn(10)

    # create LL with loop in node 2:
    head2 = ListNode(0)
    node = head2
    for i in range(1, 6):
        new_node = ListNode(i)
        if i == 2:
            node2 = new_node
        node.next = new_node
        node = node.next
     # create loop into node 2
    node.next = node2


    # print a LL:
    node = head2
    i = 0
    while node and i < 10:
        print(f"Node: {i}, val: {node.val} Add: {node}")
        i += 1
        node = node.next


    head_test = head2
    obj1 = Solution()
    print("Junction in: ")
    print(obj1.detectCycle(head_test))
