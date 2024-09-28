str=input("Enter a string")
res=''.join ([i for i in str if not i.isdigit()])
print("After removing integers",res)