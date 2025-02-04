import random
# This module allows me to use randint method to generate random numbers.

"student_register.py" # Written by Gower Campbell


# <--------------------- Program Objective ------------------------------>
''' Demonstrate my understanding of user input, loops, and file 
handling in Python. You will:

- Create a new Python file named student_register.py.
- Ask the user how many students will be registering.
- Use a for loop to collect student ID numbers for the specified number of
students.

- Save each ID number to a text file named reg_form.txt, ensuring:
- Each student ID is followed by a dotted line, to act as a space for
student signatures. '''



# <--------------------- Number of Students ------------------------------>
# num_students: Stores the number of students as an int() from a input()
# from the Examiner's program.
num_students = int(input(
    "\nHow many students are registering for the exam? \n"))


# <--------------------- Open/Create the File ---------------------------->
# Open/Create a single file for Writing & Reading "w+"
with open("reg_form.txt", "w+", encoding="utf-8") as reg_form:


# <--------------------- Write Exam Rules to the File -------------------->  
    reg_form.write('''
During the exam, students must adhere to the following rules: 
The exam lasts 10 hours, and all submissions must be completed on 
time. Only approved materials are allowed; electronic devices and 
collaboration are prohibited. Show all work clearly, and ensure answers 
are legible. Cheating or plagiarism will result in disqualification. 

Report any issues to the invigilator immediately. Maintain silence, 
follow instructions, and uphold academic integrity throughout the exam. \n''')

# <--------------------- Adds Headers to the File -------------------->             
    reg_form.write('''\nStudent Examinees Name | Assigned ID \n''')
    reg_form.write("." * 40 + "\n")



# <--------------------- Loop Through Each Student -------------------->   
    for student_counter in range(1, num_students + 1):
# To collect their details for the exact number of students attending
# specfied by the examiners. I learned that starting at 1 (not 0) ensures
# the loop 'Starts'  at the exact number of students. And 'Ends' the same.
# Remember(Start, End, Step) I can't 'end' on the number set so I +1


# <--------------------- Ask for Student Name -------------------->  
        student_name = str(input(
             "\nEnter your full name to register: (or type '0' to quit):"))
# From collecting the user full name to receive their exam ID.
# I found its important to cast the input if I use various inputs.



# <--------------------- Exit Option -------------------->  
# Check if the user wants to exit. Along as the 0 is entered
# It meets its condition to Terminate this Loop with a 'Break'
        if student_name.lower() == '0':
            print("\nExiting registration process.\n")
            break


# <--------------------- Process Student Name -------------------->  
        else:
            parts = student_name.split(' ')
# Splitting the name into parts for example "Gower Campbell".split()
# Produces ["Gower", "Campbell"] because ' ' 
# I've assigned it to take away the space from my characters.

            initials = ''.join([word[0] for word in parts]).upper()
# Generating Initials for a Student's Exam ID.
# Take the first [0] letter of each part and ''.join() the together.
# The '' is the delimter?  And places no spaces or characters between.
# .Upper Ensures the initials are in Uppercase: GC



# <--------------------- Generate Random ID -------------------->  
            random_number = random.randint(100000, 999999)
# Output the initials with random.randint(a, b)
# I've used the random module to generate a random number 
# between A & B In this case, a 6-digit random number between 100000 and 999999 
            id = f"{initials}{random_number}"
# Using the f-string to concatenate the initials and the random number.
# Example if the initials is "GC" and a random number "123456" 
# resulting ID is GC123456


#<---------------- Write Student Details to the File ------------>
            reg_form.write(
                f"\nStudent Name: {student_name.upper()} | ID: {id}\n")
            reg_form.write(">" * 40 + "\n")
# Sending this information to reg_form the file is appended with
# student name and unique ID to the file. Alongside a dotted line to the
# added entry.          

#<---------------- Print Confirmation --------------------------> 
        print(f"\nRegistration complete! Student Name:{student_name.upper()}\
                    " "| ID: {id}\n")
            
'''I’ve learned how to create a program that collects student details and 
saves them in a file (reg_form.txt). I’m focusing on making the code dynamic 
for later integration into frontend interfaces (e.g., API). I enjoyed 
generating unique IDs for each student and sending the exam details 
along with the registrations.'''

'''I have a few questions:

Are there ways to make the process more dynamic?
Would a while loop be more effective than a for loop here?
Can I create a code to append students who can't attend the exam?'''
