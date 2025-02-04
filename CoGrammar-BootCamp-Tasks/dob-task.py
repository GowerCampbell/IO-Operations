'''dob_task.py'''
# Written by Gower Campbell

'''Objective: To demonstrate your ability to work with file handling, data 
extraction and formatted output in python.  

- Create a new Python file named dob_task.py
- Read and extract data from the provided text (DoB.txt)
- Organise the extracted data into two sections: 'Name' & 'Birth' 
- Format the Output as per format examoke provided'''

# <--------------------- Step 1 Intialize Variables --------------------> 
# These will store the extracted names and birth dates
names = []
birth_dates = []


# <--------------------- Step 2 Open File & Read Contents --------------------> 
# Using the open() to READ the file "DOB.txt" in read and write mode (r+)
# Using UTF-8 to handle special characters like (†), etc.
with open("DOB.txt", "r+", encoding="utf-8") as file:
# REMEMBER: The 'with' statement ensures that the file is properly closed.


# < --------------- Step 3 Reading Each Line in the File ----------------->
    for line in file:
# Starting a loop to read each line in the file one by one.


# < --------------- Step 4 Splitting Each Line into Three Parts ----------->
# Inside variable 'parts': the line.strip removes all the spaces.
# I can then create a list of parts based on what was stripped.
     # 1. Everything before the first space will be the first name.
     # 2. Everything between the first and second space the second 
        # will be the last name.
     # 3. Everything after the second space will be the birthdate.
# I learned when adding line.split(' ', 2), the 2 works to make sure the 
# agrument splits the string correctly: parts = ["Gower", "Campbell", "26 Feb 1999"]
                                             #     0         1               2
# Without the 2 the string will stay split at every space.
        parts = line.strip().split(' ', 2)  



# < --------------- Step 5 Correct Format? ----------->
        if len(parts) == 3: 
# If so, it means the line has the expected format (name + surname + birthdate)
# But what if someone is known by their middle names. 
# How do we write such a code?

# < --------------- Step 6 Appending Name & DoB to lists ----------->
            names.append(parts[0] + " " + parts[1])  
            birth_dates.append(parts[2])
# If part [0] is the first name, and parts [1] is the last name.
# Then birth_dates will be part[2]
# I can use the append to add this to my variables 

# < --------------- Step 7 Printing Results ----------->
"------Extracted Names------"
print(f"Names: {names}" + "\n")
"------Extracted Birthdates------"
print(f"Birth Dates: {birth_dates}" + "\n")

'''I learned how to read files, strip the data, and split it into parts 
to be used as variables for my arguments. One thing I’m wondering is how 
I can improve this code to handle people with middle names properly, 
so they’re sorted correctly.'''
