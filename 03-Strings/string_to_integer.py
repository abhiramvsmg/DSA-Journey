class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Step 1: Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Step 2: Check the sign
        sign = 1

        if i < n and s[i] == "-":
            sign = -1
            i += 1
        elif i < n and s[i] == "+":
            i += 1

        # Step 3: Read digits
        number = 0

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")
            number = number * 10 + digit
            i += 1

        # Step 4: Apply the sign
        number = number * sign

        # Step 5: Handle 32-bit limits
        if number > 2147483647:
            number = 2147483647
        elif number < -2147483648:
            number = -2147483648

        return number