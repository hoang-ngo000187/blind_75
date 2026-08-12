from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Useful function
def create_linked_list(nums):
    dummy = ListNode()
    cur = dummy

    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next


def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Problem code
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_map = {}
        p = head
        ret = None
        while p != None:
            if p in hash_map:
                ret = p
                break
            else:
                hash_map[p] = 1
                p = p.next
        return ret

# if __name__ == '__main__':
    # head = create_linked_list([1, 2, 3, 4, 5])

    # print("Input:")
    # print_linked_list(head)

    # sol = Solution()
    # middle = sol.getIntersectionNode(head)

    # print("Middle:", middle.val)
    