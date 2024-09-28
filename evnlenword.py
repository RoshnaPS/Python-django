a = input("Enter a String")
b = a.split(" ")
for i in b:
    if len(i) % 2 == 0:
        print(i)
