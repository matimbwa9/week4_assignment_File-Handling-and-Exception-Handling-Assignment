# error_handling.py

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Ask user for filename
filename = input("Please enter the filename: ")

# Read the file and handle errors
content = read_file(filename)

if content:
    print("File content read successfully!")
    print(content)
else:
    print("Failed to read the file.")
