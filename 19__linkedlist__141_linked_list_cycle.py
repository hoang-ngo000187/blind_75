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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        ret = False
        while(fast != None and fast.next != None):
            fast = (fast.next).next
            slow = slow.next
            if (fast == slow):
                ret = True
                break
        return ret

# if __name__ == '__main__':
    # head = create_linked_list([1, 2, 3, 4, 5])

    # print("Input:")
    # print_linked_list(head)

    # sol = Solution()
    # middle = sol.getIntersectionNode(head)

    # print("Middle:", middle.val)
    