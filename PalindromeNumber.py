
x1 = 121
#Out1 true

x2 = -121
# Output: false

x3 = 10
# Output: false


def isPalindrome(x) -> bool:
    x = str(x)
    return x == x[::-1]


print(isPalindrome(x1))
print(isPalindrome(x2))
print(isPalindrome(x3))
