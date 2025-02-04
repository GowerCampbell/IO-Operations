"IO Operations Knotes by Gower Campbell"

"I/O stamds for input/putput"

"There should be one - and preferably only one - obvious way to do it."

# - The Zen of Python

"Two Methods use the Open()"

"Built IN Open() that accepts (including the path to the file) a filename"
'''The second argument is the mode or accesss modifier such as 'r+' for 
reading and writing mode'''

# Using the open() also needs to explicity have a close() to release the
# systems resources

# file = open("example.txt", "r+")
# Performs iperations on the open file
# file.close()

# System Resources included memory gor file contents and file descipters 
# to keep track of the file. Do not exhuast your systems capacity to 
# manage files, 

"Using the open() function with the 'with' and 'as' statements"

# This method of opening and managing a file in python is referred to as
# using a context manager. It leverages the eith statement, which ensures
# that resources are properly managed, and automatically closes the file
# once the block of code within the with statement is exited.

# with open('example.txt', 'r+') as file:
    # Perform file operations on the open file
    # the code here must be indented to be part of the with block.

# The 'with' block ensures that the file is proples closed after its code 
# finishes even if an error occurs. This is a safer and cleaner way to handle
# files because it manages resourse alllocation deallocation automatically

# The different modes available when opening a file in python.

# Commonoly used modes (ways a program or function can operate)

# Read: Acessing and retrieving data from a file or source without
# modifying it.

# with open("example.txt", "r") as file:  # Open file in read mode
#    content = file.read()              # Read the file's content
#    print(content)

# To view or use the data stored in a file

# Write: Creating or modifing data in a file or storage data
# with open("example.txt", "w") as file:  # Open file in write mode
#    file.write("Hello, World!") 
    
# Logging information, saving user inputs.

"Mode | Description"

# r Opens the file 'for reading' only. An I/O error is thrown if the file 
#   doesn't exist 

# r+ Opens the file for both 'reading and writing'. An I/O error is thrown if 
    # If the file doesn't exist

# w Opens the file 'for writing' only. It creates a new file if it doesn't
#   exist and if the file already exists, the previous content is overwritten.

# w+ Opens the file 'for writing and reading'. It creates a new file if it doesn't
#    exist and if the file already exists, the previous content is overwritten. 

# a Opens the file "for writing only, creating it" if it doesnt exist. 
   #  Any data written will be appeneded (thus a) at the end of the file,
   #  preserving the existing content.

# a+ Opens the file 'for reading and writing', creating it if it doesn't exist
#   # Any data written will be appended (thus a) at the end of the file 
    # preserving the existing content.

" Spliting | Stripping | Looping  " 

"Looping"
# Repeating a block of code for each item in a sequence 
# (like a list or string).

words = ["Hello", "World", "python"]
for word in words:
    print(word)

"Stripping"
# Default is a space and will remove all the stripping
#text "   Learn python Fast   "
words = text.strip().split()
for word in words:
    print(word)


"Splitting"

# READING FILES
# The read() (used to read the entire contents of a text file and then
# return the file contents as a string.

with open("event_items.txt", "r+") as my_file:
    # 'lines' will contain a string with all the data from the file.
    internal_file_lines = my_file.readlines()
    # Reads all data from the  file
    # lines = file.read()

# You can specify the lines you want read
lines = file.read(10)
# Passing an integer argument to the read() method

# Using the readlines method:

with open("example.txt","r+") as file:
    # 'lines' contain each line of the text file as a list element
    line = file.readline() # Reads a single line from the file.

# readlines() read the contents of a text file line by line

"Key Distinction in is that readline() & readlines()"
# Apart from the 's' as a possessive form

readline() # reads one line at a time
readlines() # :reads all lines and returns them

# Looping through the file:
# The appriach invovles looping through the file line by line and 
# performing operations on each line:

with open("example.txt", "r+") as file:
    for line in file:
        # Reads each line of data in the file,
        print(line) # Displays each line within 'example.txt'

with open("example.txt", "r+") as file:
    # Iterate each line in file
    for line in file:
        # Prints the entire line
        print("The entire line is: " + line)
        # Prints only the firs character of the line
        print("The first character of this line: " + line[0])

"You could up all the lines of the text file into one large string"

contents = "" #Initalise an empty string to store the contents

with open("example.txt", "r+") as file:
    # Open the file and iterate through each line
    for line in file:
        contents = contents + line # Append each line to 'contents'

# Print the contents outside 'with' statement
print(contents)

# Once stored using a variable named contents.
"We can manipulate the file's data"
# For example, print(contents)

# Alternative approach is to store each line in a list by appending it 
# to an intially empty, providing flexibility in how we handle and proccess
# the file's data.

lines = [] # Intialise an empty list to store each line

with open ("example.txt", "r+") as file:
    # Open the file and iterate through each line 
    for line in file:
        lines.append(line) # Appeand each line to the 'lines' list
        # print thre lines stored in the list
        print(lines)

'''WRITING DATA TO A TEXT FILE'''
# "w access mode"

name = input("Enter name: ")

with open("output.txt", "w") as f:
    f.write(name +"\n")

# By creating a new file named output.txt in write mode. 
# Once user inputs their name it will then be sent to the directory.
# Remember with the write() method add a (\n) to store your variables
# on the next newline.

# From prompts to eneter a name.

# Any additional write() statements will append content to file without
# overwriting the existing contents

name = input("Enter Name: ")

with open("output.txt", "w") as f:
    f.write(name + "\n")
    f.write("My name is on the line above in this text file.")

# If you use the Open() again the existing contents will be overwritten
# and will replace the previous contents in the file. 
# 
 '''DONT FORGET''' 
# Dont forget to close the file if you're not using with and as. 

open_file = open("text_file_name","w")

open_file.close() # Manually closing the opened file.

"FILE DIRECTORY"
# Also known as a folder, is a container that can hold multiple files
# and other directories. When working with files in Python, you may need 
# to specify the file location or path to access or manipulate files in 
# different directories.

# Never hard-code file locations. Use the the 'relative file path'

# Relative file paths use symbols like '.' (represents the current directory)
# and '..' (represent the parent directory)

# To specfiy the directorys hierarchy and as a directory separators within
# relative paths. 

# The forward slash '/' (linux, mac0S) 

# The blackslash '\' (Windows)

# WRONG: C:/Users/MyName/Document....
'''Use the following if the file is in the same folder'''
# CORRECT: example.txt OR ./example.txt
'''Use the following if the file is one folder back'''
# Correct ../example.txt


'''FILE ATTRIBUTES IN PYTHON'''
import os 
# 1. You can check if a file exists
print(os.path.exists("example.txt")) # Retirns True if the file exists

# 2. To get the size of a file:

import os
print(os.path.getsize("example.txt")) # Returns the size of the file in bytes

# 3. To check the time the file was last modified:

import os
import time

# Get the last modification time of 'example.txt'
last_modified = os.path.getmtime('example.txt')

# Convert the timestamp to a human-readable format
last_modified_str = time.ctime(last_modified)

#print the last modification time
print(last_modified_str)

'Handling execptions like 'FileNotFoundError'

# By anticipating and managing cases where files may not exist,
# your program can provide informative feedback to users and prevent 
# unexpected crashes.

'4. Handling a FileNotFoundError exception'

try:
    # Attempt to open 'example.txt' in read mode
    with open("example.txt", "r") as file:
        # Read the entire content of the file into 'content'
        content = file.read()

        # Print the content of the file
        print(content)

except FileNotFoundError:
    # Handle the case where 'example.txt' does bir exist
    print("The File does not exist.")

'''FILE ENCODING'''
#When you open a open, you can specify how the text in the file is encoded.
# Encoding is like a translator between himan-readable text and the computer
# bytes. When we turn text into bytes, its called encoding.
# Decoding: turn bytes back into text,

'Extra optional argument to the open() function to tell python'

# This is important because different systems and files use differenr encoding 
# methods and using the weong one can cause weird characters.

# To avoid this, you can specify the encoding method when you open a file.
# One common encoding method is utf-8

file = open(example.txy", "r+", encoding="utf-8")



