# 92. Reverse Linked list 2

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
   def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # 1. Move prev to node before `left`
        for _ in range(left - 1):
            prev = prev.next

        # 2. Reverse sublist
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next


# -------- Helper functions --------

def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")



if __name__ == "__main__":
    values = [1,2,3,4,5]
    head = build_linked_list(values)
    left = 2
    right = 4
    print("Input Linked list:")
    print_linked_list(head)
    print(f"Left: {left}, right: {right}")

    s = Solution()
    sol = s.reverseBetween(head, left, right)
    
    print("Output linkedlist: ")
    print_linked_list(sol)