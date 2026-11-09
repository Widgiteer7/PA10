import os

file_request = input("Enter file name: ")  # User input for file name

for root, directories, files in os.walk("C:\\"):
    if file_request in files:
        file_path = os.path.join(root, file_request)  # Joins root and file name to get full path
        print("File found")
        with open(file_path, 'r') as file:           # Opens file
            if sum(1 for line in file) <= 5:           # Checks for files with less than 5 lines
                print(file.read())                       # Outputs entire file
            else:
                file.seek(0)                           # Resets file pointer to the beginning
                for i in range(5):                       # Loops through lines
                    line = file.readline()                 # Reads line
                    print(line)                            # Prints line
    else:
        print("File not found.")
        break


#with open(file_path, 'r') as file:           # Opens file
#    if sum(1 for line in file) <= 5:           # Checks for files with less than 5 lines
#        print(file.read())                       # Outputs entire file
#    else:
#        file.seek(0)                           # Resets file pointer to the beginning
#        for i in range(5):                       # Loops through lines
#            line = file.readline()                 # Reads line
#            print(line)                            # Prints line