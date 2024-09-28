def ind_err(list, index):
    try:
        result = list[index]
        print(f"Value at index {index}: {result}")
    except IndexError:
        print(f"Index {index} is out of range. Please provide a valid index.")
list = [1, 2, 3, 4, 5]
try:
    i = int(input("Enter an index to access: "))
    ind_err(list, i)
except ValueError:
    print("Invalid input. Please enter a valid integer.")