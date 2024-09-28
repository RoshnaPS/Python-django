def register(username, password):
    try:
        with open("user_details.txt", "a") as file:
            file.write(f"{username},{password}\n")
        print("Registration successful!")
    except IOError:
        print("Error writing to the file. Please try again.")
def login(username, password):
    try:
        with open("user_details.txt", "r") as file:
            for line in file:
                s_username, s_password = line.strip().split(',')
                if username == s_username and password == s_password:
                    print("Login successful!")
                    return
        print("Invalid username or password. Login failed.")
    except FileNotFoundError:
        print("User file not found. Please register first.")
def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))

            if choice == 1:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                register(username, password)
            elif choice == 2:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                login(username, password)
            elif choice == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()