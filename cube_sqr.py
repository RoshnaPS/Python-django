a=[]
n=int(input("Enter the no of elements in the list:"))
for i in range(0,n):
    element=int(input("Enter element"+str(i+1)+ ":"))
    a.append(element)
print("Original list:",a)
sqr=list(map(lambda x:x**2,a))
print("Square of the numbers from the list:",sqr)
cube=list(map(lambda x:x**3,a))
print("Cube of the numbers from the list:",cube)