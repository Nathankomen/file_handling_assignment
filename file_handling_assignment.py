# File Creation
def create_and_write_file():
    try:
        # Create and open the file in write mode
        with open("my_file.txt", 'w') as file:
            # Write at least three lines of text to the file
            file.write("Hello, this is the first line.\n")
            file.write("12345 - This line includes numbers.\n")
            file.write("This is the third line with more text.\n")
        print("File 'my_file.txt' created and written successfully.")
    except PermissionError:
        print("Error: Permission denied when trying to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_file():
    try:
        # Open the file in read mode and display the content
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nContents of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", 'a') as file:
            # Append three additional lines of text
            file.write("Appending a new line here.\n")
            file.write("Another line with some more text.\n")
            file.write("Final appended line with 789.\n")
        print("Appended new lines to 'my_file.txt' successfully.")
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    try:
        create_and_write_file()
        read_file()
        append_to_file()
        read_file() # Read the file again to display the appended content
    except Exception as e:
        print(f"An unexpected error occurred in the main process: {e}")
    finally:
        print("\nExecution completed.")

if __name__ == "__main__":
    main()
