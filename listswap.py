a=[]
n=int(input("Enter the no of elements in the list:"))
for i in range(0,n):

    element=int(input("Enter element"+str(i+1)+ ":"))
    a.append(element)
print("Original list:",a)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("New list: ",a)
