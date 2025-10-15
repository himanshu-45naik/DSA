# 1352. Product of the last k numbers

![Alt text](product-kElements.png)


```python

obj = ProductOfNumbers()
obj.add(3)   # [1, 3]
obj.add(0)   # Reset -> [1]
obj.add(2)   # [1, 2]
obj.add(5)   # [1, 2, 10]
obj.add(4)   # [1, 2, 10, 40]

# Index:      0   1   2   3   4
# Value:      1   2  10  40

# prefix_product[-1] → last value → 40
# prefix_product[-3] → (k=2), so -2-1 = -3 → prefix_product[2] = 10
# Computation: 40/10=20

prefix_product[-1] // prefix_product[-k-1]
""" Why -k-1?
 -1 represents the last element of the list.
 -k-1 refers to the (k+1)th element from the end, which is the product before the last k elements.
"""
```