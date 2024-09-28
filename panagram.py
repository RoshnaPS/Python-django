def ispangram(str):
    alpbt = "abcdefghijklmnopqrstuvwxyz"
    for char in alpbt:
        if char not in str.lower():
            return False
    return True


string = input("Enter a string")
if (ispangram(string) == True):
    print("String is pangram")
else:
    print("String is not pangram")
