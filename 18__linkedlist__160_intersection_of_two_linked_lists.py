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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA=[]
        stackB=[]

        stackA.append(ListNode(1))
        stackB.append(ListNode(2))
        
        p = headA
        while p:
            stackA.append(p)
            p = p.next

        p = headB
        while p:
            stackB.append(p)
            p = p.next

        i = -1
        while(stackA[i] == stackB[i]):
            i -= 1
        i+=1

        if i == 0:
            return None
        else:
            return stackA[i]

# if __name__ == '__main__':
    # head = create_linked_list([1, 2, 3, 4, 5])

    # print("Input:")
    # print_linked_list(head)

    # sol = Solution()
    # middle = sol.getIntersectionNode(head)

    # print("Middle:", middle.val)
    