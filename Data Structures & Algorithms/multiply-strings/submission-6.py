class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Need the length of the product
        # Likely need to index strings. E.g. s[2] = 4
        # What if we use ord. Add weight to numbers in a higher position
        # Position i = weight i (281) 2 gets mul by 10^(position)
        int1, int2 = 0, 0
        n1, n2 = len(num1), len(num2)

        for pos in range(n1):
            int1 += int(num1[pos]) * 10**(n1 - pos - 1)
        for pos in range(n2):
            int2 += int(num2[pos]) * 10**(n2 - pos - 1)
        print(int1, int2)

        return str(int1 * int2)