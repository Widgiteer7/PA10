import os

file_request = input("Enter file name: ")                     # User input for file name

file_found = False

for root, directories, files in os.walk("C:\\"):              # Searches computer for file
    if file_request in files or file_request in directories:
        file_path = os.path.join(root, file_request)            # Joins root and file name to get full path
        print("\nFile found\n")
        file_found = True
        
        with open(file_path, 'r') as file:                      # Opens file
            file_lines = file.readlines()
            if len(file_lines) <= 5:                              # Less than 5 Lines:
                print("".join(file_lines))                          # Outputs entire file
            else:
                for line in file_lines[:5]:                         # Less than 5 Lines:
                    print(line, end="")                               # Outputs first 5 lines

if not file_found:                                            # For when the program cannot find the file
    print("\nFile not found.")