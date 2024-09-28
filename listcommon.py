
list1=[]
n=int(input("Enter the no of elements in the list1:"))
for i in range(0,n):
    element1=input("Enter element"+str(i+1)+ ":")
    list1.ap(element1)
print("First list:",set(list1))
list2=[]
m=int(input("Enter the no of elements in the list2:"))
for i in range (0,m):
    element2 = input("Enter element" + str(i + 1) + ":")
    list2.append(element2)
print("Second list:",set(list2))

print(list1&list2)

