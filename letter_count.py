def letter_count(input_string):
    l_count={}
    for char in input_string:
        if char.isalpha():
            char_lower=char.lower()
            l_count[char_lower]=l_count.get(char_lower,0)+1
    print("No of occurences of each letter:")
    for letter,count in l_count.items():
        print(f"{letter}: {count}")
a=input("Enter a string:")
letter_count(a)