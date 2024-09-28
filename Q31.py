def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        return f"File '{filename}' not found."
    except Exception as e:
        return f"An error occurred: {e}"
file_name = input("Enter the filename: ")
result = count_lines_in_file(file_name)
if isinstance(result, int):
    print(f"The number of lines in the file '{file_name}' is: {result}")
else:
    print(result)