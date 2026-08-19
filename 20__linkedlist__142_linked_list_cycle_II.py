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

HASH_MAP = 0
# Problem code
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if HASH_MAP:
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
        else:
            def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
                # First, find the meeting point
                fast = slow = head
                while fast and fast.next:
                    fast = (fast.next).next
                    slow = slow.next

                    if fast == slow: # Fast is in meeting point
                        # Move slow to head, start slow from the head, fast from the meeting point with the same speed
                        slow = head
                        while fast != slow:
                            fast = fast.next
                            slow = slow.next
                        return slow
                # If no cycle is detected, return None
                return None
            

# if __name__ == '__main__':
    # head = create_linked_list([1, 2, 3, 4, 5])

    # print("Input:")
    # print_linked_list(head)

    # sol = Solution()
    # middle = sol.getIntersectionNode(head)

    # print("Middle:", middle.val)
    