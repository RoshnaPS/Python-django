def pattern(num):
    m=1
    while m<num:
        print(" "*(num -m )+"* "*m)
        m+=1
    m=num
    while m>=1:
        print(" " * (num - m) + "* " * m)
        m-=1
num =int(input("Enter no of rows:"))
pattern(num)
