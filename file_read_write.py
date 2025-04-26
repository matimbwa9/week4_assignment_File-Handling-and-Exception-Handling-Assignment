# file_read_write.py
def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Count words
        words = content.split()
        word_count = len(words)
        
        # Convert text to uppercase
        uppercase_content = content.upper()
        
        with open(output_filename, 'w') as file:
            file.write(f"Word Count: {word_count}\n")
            file.write(uppercase_content)
        
        print(f"File has been processed and saved as {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Call function with filenames
process_file('input.txt', 'output.txt')
