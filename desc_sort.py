a=[]
n=int(input("Enter the no of elements in the list:"))
for i in range(0,n):
    element=int(input("Enter element"+str(i+1)+ ":"))
    a.append(element)
print("Original list:",a)
sort_list=sorted(a,key=lambda x:x,reverse=True)
print("Sorted list(descending order:",sort_list)
