## Find the punishment number of an integer


def is_possible(x):
    sx = str(x * x)

    def calculate(index, current, sum):
        if index == len(sx):
            sum += current
            return sum == x

        current = current * 10 + int(sx[index])

        return calculate(index + 1, 0, sum + current) or calculate(
            index + 1, current, sum
        )

    return calculate(0, 0, 0)


class Solution:
    def punishmentNumber(self, n: int) -> int:

        total = 0
        for i in range(1, n + 1):
            if is_possible(i):
                total += i * i

        return total


s1 = Solution()
print(s1.punishmentNumber(37))
