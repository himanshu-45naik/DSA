# 21. Merge two sorted Linkedlist

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #  Both LL1 and LL2 are sorted
        #  Use 2 pointers
        #  temp1 → LL1
        #  temp2 → LL2
        # Create a dummy head
        # Compare temp1 and temp2 
        # if temp1 is smaller add it to resultant LL, and udpate temp1 ⇒ [temp1.next](http://temp1.next) and temp2 as it is.
        # else temp2 is smaller add it to resultant LL and update temp2 ⇒ [temp2.next](http://temp2.next) and temp1 as it is.
        # If either one is bigger in size then add remaining elements in the result after the loop.
        # Return the dummy.next
        
        
        temp1 = list1
        temp2 = list2

        dummy = ListNode()
        curr = dummy

        while temp1 and temp2:
            if temp1.val < temp2.val:
                curr.next = temp1
                temp1 = temp1.next
            else:
                curr.next = temp2
                temp2 = temp2.next
            curr = curr.next

        if temp1:
            curr.next = temp1
        else:
            curr.next = temp2

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
    values1 = [1, 2, 4]
    values2 = [1, 3, 4]
    L1 = build_linked_list(values1)
    L2 = build_linked_list(values2)

    print("List1:")
    print_linked_list(L1)

    print("List2:")
    print_linked_list(L2)

    s = Solution()
    res = s.mergeTwoLists(L1, L2)
    print("Result")
    print_linked_list(res)