def write_list_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        return f"Data written to file '{filename}' successfully."
    except Exception as e:
        return f"An error occurred: {e}"
file_name = input("Enter the filename to write the list: ")
my_list = [1, 2, 3, 4, 5]
res = write_list_to_file(file_name, my_list)
print(res)