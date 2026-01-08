# 328. Odd Even Linkedlist

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Group all nodes with odd indices followed by nodes with even indices.

        Args:
            head (Optional[ListNode]): Given singly linkedlist

        Returns:
            Optional[ListNode]: result linkedlist
        """

        # Use two pointers
        # Odd and Even -> such that these two pointers will be head of odd ll & even ll respectively
        # How to traverse the main ll, such that
            # Odd pointer traverse through odd indices
            # Even pointer traverse through even indices
        # Intialize odd pointer to head & even to head.next
        # Join odd node to odd indices ll -> odd.next = even.next (After even comes odd)
        # Join even node to  even indices ll -> even.next = even.next.next
        # Join odd tail to even head

        if not head:
            return None
        
        if not head.next:
            return head
            
        odd = head
        even = head.next

        even_head = even

        while even and even.next:
            odd.next = even.next  
            odd = even.next
            even.next = even.next.next
            even = even.next
        
        odd.next = even_head  # Connect odd tail with even head

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
    head = sol.oddEvenList(head)

    print("\nOdd even linked list:")
    print_linked_list(head)
