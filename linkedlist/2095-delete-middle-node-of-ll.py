# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     """
    #         - Head of the ll is given
    #         - Delete the middle node
    #         - If the length of the ll is even -> remove the largest interger 
    #         - Ex -> [1,2] => [1]
    #         - Ex -> [1,2,3,4] => [1,2,4]
    #     """

    #     # Brute force
    #     # First we need to find the length of the linkedlist
    #     # Based on that find the half of that length (x = length // 2)
    #     # If length is odd -> remove the xth index  
    #     # If legth is even -> remove the x+1th index

    #     # Edge case if empty linkedlist
    #     if not head:
    #         return None

    #     # Initializing length and curr pointer
    #     length_ll = 0
    #     curr = head

    #     # Calculating the length of ll
    #     while curr:
    #         length_ll += 1
    #         curr = curr.next

    #     # Edge case if lenght is 1
    #     if length_ll == 1:
    #         return None

    #     # Calculate the index to be removed
    #     half = length_ll // 2

    #     i = 0
    #     curr = head
    #     prev = head

    #     while i <= half:
    #         if i == half:
    #             prev.next = curr.next
    #             return head
    #         prev = curr
    #         curr = curr.next
    #         i += 1


    # Optimal Solution
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is at the middle node
        prev.next = slow.next
        return head


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
    values = [1, 2, 3, 4, 5]
    head = build_linked_list(values)

    print("Original linked list:")
    print_linked_list(head)

    sol = Solution()
    head = sol.deleteMiddle(head)

    print("\nAfter deleting middle node:")
    print_linked_list(head)
