# Monotonic Stack
- The stack in which the elements are stored in a specific order is called as monotonic stack

---

# Next greater element - 1

- Lets say we have an list of integer [4,12,5,,3,1,2,5,3,1,2,4,6]
- If we traverse form left we wont know what are the elemnts on the right of (lets say) 3. As we have not traversed it yet.
- So we will do back traversing.
- We will create a empty stack.
- Now  using a for loop traversing from back.
    - First when the element is 6 and stack is empty so the NGE is -1, add 6 to stack. res = [-1], stk = [6]
    - Now the top element of stack is 6 and it is greater than 4, so the NGE of 4 is 6, add 4 to stack. res = [6,-1], stk = [4.6]
    - Now the top element is 4 and it is a NGE of 2 , add 2 to stack.  res = [4,6,-1], stk = [2,4,6]
    - Top element is 2 and it is NGE of 1, add 1 to stack. res = [2,4,6,-1], stk = [1,2,4,6]
    - Now the element is 3 and the top stack element is 1, so pop 1 as it is not NGE of 3.  stk = [2,4,6]
    - Now the element is 3 and the top stack element is 2, so pop 2 as it is not NGE of 3.  stk = [4,6]
    - Top element is 4 and it is NGE of 3, add 3 to stack. res = [4,2,4,6,-1], stk = [3,4,6]
    - And so on...

---


# Next greater element - 2

**Approach 1**
- We have a circular array, where the NGE maybe at the right or left.
- So we will have to traverse to the left side of the element if we dont get the NGE to the right side.
- ## How to traverse?
  - Array : [2, 10, 12, 1, 11] 2, 10, 12, 1, 11
  - Here we dont have NGE of 11 to the right so we will have to traverse left. Here to the `right` the index of 2:5, 10:6, 12:7 & so on.....
  - There are about 5 elements to the right of 10, in order to reach 10 again. 
  - We can acces the index of left elements by the hypothetical elements on the right.
  - Lets say N is the size of array.
  - 2:5 --> 5 % N --> 5 % 5 = 0
  - 10:6 --> 6 % N  --> 6 % 5 = 1
 