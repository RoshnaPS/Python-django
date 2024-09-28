rows = 5
i = 0
while i < rows:
    j = 0
    while j < rows - i - 1:
        print(" ", end="")
        j += 1

    k = i
    while k >= 0:
        print(chr(65 + k), end="")
        k -= 1

    print()
    i+=1
