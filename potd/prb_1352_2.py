## Product of the last k numbers
### Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.


class ProductOfNumbers:
    """Perform add and getProduct functions
    step1 = Instantiate the empty array to store the product.
    step2 = Add product to the array such that new number num is multiplied.
            **Edge case: If the number is zero, than reset the array to [1].
    step3 = Return the product of last k elements.
            Product = (Product of all numbers) // (Products of all numbers except last k elements)

    Time Complexity -> O(1)
    Space Complexity -> O(n)
    """

    def __init__(self):
        self.prefix_product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1]
        else:
            self.prefix_product.append(self.prefix_product[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(
            self.prefix_product
        ):  # If k exceeds stored products (meaning a 0 was added)
            return 0
        return self.prefix_product[-1] // self.prefix_product[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
obj.add(8)
print(obj.getProduct(2))
