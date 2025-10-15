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
