n1 = int(input("Enter the first number"))
n2 = int(input("Enter the last number"))
print("prime numbers are:")
for num in range(n1, n2 + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
                print(num)
