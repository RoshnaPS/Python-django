l=[]
def palindrome_list(my_str):
    if my_str==my_str[::-1]:
        print("The list is palindrome")
    else:
        print("The list is not a palindrome ")
n=int(input("Enter the no of elements in the list:"))
for i in range(0,n):

    element=int(input("Enter element"+str(i+1)+ ":"))
    l.append(element)
print("The list is:",l)
palindrome_list(l)

