list1 = input("Enter elements for List 1 separated by spaces: ").split()
list2 = input("Enter elements for List 2 separated by spaces: ").split()

common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)