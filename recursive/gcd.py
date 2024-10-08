def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

print(gcd(48, 18)) # 6
print(gcd(54, 24)) # 6

