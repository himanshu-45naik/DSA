## Bit Manipulation

### Shift Operator

- Bitwise shift operators (`<<` for left shift and `>>` for right shift) work directly on decimal (integer) numbers because integers are stored in binary format at the hardware level.

#### Right Shift (`>>`)

The right shift (`>>`) operator moves all bits to the right by `k` positions.

- Each right shift divides the number by 2 (integer division).
- The rightmost bit (Least Significant Bit, LSB) is discarded.

```python
n = 13
k = 2
result = n >> k  # Shift right by 2
print(result)  # Output: 3
```
`13 >> 2 = 3` (equivalent to `13 // 2^2` = 13 // 4 = 3).

#### Left SHift (`<<`)
The left shift (`<<`) operator moves all bits to the left by k positions.

- Each left shift multiplies the number by 2.
- Zeros (0) are added to the right.

```python
n = 5
k = 2
result = n << k  # Shift left by 2
print(result)  # Output: 20
```
`5 << 2 = 20` (equivalent to `5 * 2^2` = 5 * 4 = 20).

# Swap two numbers

 a = 10
 b = 12

 O/p => a = 12 b = 10

 - We can use XOR operator
 - 10^10 = 0
 - a = a ^ b
 - b = a ^ b = a ^ b ^ b = a
 - Thus, b = a
 - a = a ^ b = a ^ b ^ b = a ^ b ^ a = b
 - Thus, a = b

# Unset the last set bit(rightmost)

If the given number is n then,
The solution for this is `n&(n-1)`

- Subtracting 1 from n flips all bits after the rightmost set bit, including the rightmost 1 itself.
- n     =  101010  (42 in decimal)
- n - 1 =  101001  (41 in decimal)
- Performing n & (n - 1) clears this rightmost 1 while keeping the other bits unchanged
- n & (n - 1) = 101000  (40 in decimal)

# Set the last unset bit(rightmost)

If the given number is n then,
The solution for this is `n|(n+1)`

- n     =  100111  (39 in decimal)
- n + 1 =  101000  (40 in decimal)
- n | (n + 1) = 101111  (47 in decimal)

- The rightmost 0 in n is flipped to 1 in n + 1.
- n | (n + 1) ensures that this bit is set to 1, without affecting higher bits.
