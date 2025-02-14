## Product of the last k numbers
### Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.


class ProductOfNumbers:
    """Perform add and getProduct functions
    step1 = Instantiate the empty array.
    step2 = Add element in the array.
    step3 = Initialize count to k, i to one less than the length of array and product to one.
            While count is more than 0
            3.1 Calculate product of all last k number of elements of the array.
            3.2 Decrement count by -1.
            3.3 Decrement i by -1.
    step4 = Return the product.
    """

    def __init__(self):
        self.arr = []

    def add(self, num: int) -> None:
        self.arr.append(num)

    def getProduct(self, k: int) -> int:
        count = k
        i = len(self.arr) - 1
        product = 1
        while count > 0:
            product = product * self.arr[i]
            count -= 1
            i -= 1
        return product


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
