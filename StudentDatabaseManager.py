"""

@samya List of Edits - Date: 22/02/2020

* Changed all RAW_INPUTS to INPUTS to provide support for Python3 rather than Python2 (why are you even writing in python2 Abel....)
* Made a correction to the average calculator found under the Search funciton, as it was only supporting integer values till now
* Renamed some functions and variables to have clearer, more easily understandable names
* Reordered a bunch of commands from the main command line to seperate individual functions, in order to clean up a bit
* Added a last name column to the MySQL table, and renamed name to first_name
* Have expanded the search function to be able to use first name, last name or Row ID
* Have added a column for ROWIDs whenever a Row is printed, for example under the PRINT_ALL or search functions
* Inserted the ClassAvg Function
* Inserted vacuuming after deleting a row so the ids update properly
* Added an exit command to gracefully end the program when needed

To do - 

* We still get an error message and ungraceful exit whenever there's a wrong input in various cases - We should fix this
* Whenever we search for a record using the search function we always get one result back, but what if there are multiple people
with the same last or first name? We should edit the code to show all entries that have a specific last name or first name
* Waiting for the extra challenges from Mr Amin!

* Write the code more readable (spaces between symbols).
* Use more descriptive variable names to make it more understandable and easier to follow.


@samya List of Edits - Date: 24/02/2020

* Have added a validation checker for inputs! This is multifuctional tool that can be used in all your programs!
Simply put in the value to be checked, followed by which criterion it should be submitted to (Either FLOAT, INTEGER
or STRING) (e.g (input_to_be_checked, "INTEGER"))
* Have removed basically all crash possibilities/bugs within the program. Theoretically, the only way you should
be able to end the script now is through the "exit" command or a hard restart of the kernel.
* A few lines of code have been moved around to make the GUI/CL integration smoother and easier
* Made the main code redundant and moved it over to the cl.py file
"""

#Import of libraries and setting up the sqlite commands

import os.path
import sqlite3
from tabulate import tabulate

#Function to add a new entry to the database
def newEntry(student_attributes = ()):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "daba.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
        
    if(student_attributes == ()):
        print("Please enter the details of the new student.")
        student_attributes += (input_checker(input("First name: ").upper(), "STRING"),)
        student_attributes += (input_checker(input("Last name: ").upper(), "STRING"),)
        student_attributes += (input_checker(input("Address: ").upper(), "STRING"),)
        student_attributes += (input_checker(input("Class: ").upper(), "STRING"),)
        student_attributes += (input_checker(input("Mathematics grade: ").upper(), "FLOAT"),)
        student_attributes += (input_checker(input("Science grade: ").upper(), "FLOAT"),)
        student_attributes += (input_checker(input("English grade: ").upper(), "FLOAT"),)
        student_attributes += (input_checker(input("Dutch grade: ").upper(), "FLOAT"),)
        student_attributes += (input_checker(input("Art grade: ").upper(), "FLOAT"),)

    #Avg Calculator
    sum_grade = 0
    for value in student_attributes[4:8]:
        sum_grade += float(value)
    
    student_attributes += (sum_grade,)
    
    #Shows the sum of all grades and grade average to 1 d.p.
    avg_grade = sum_grade / 5.0
    
    student_attributes += (avg_grade,)
    
    
    c.execute("INSERT INTO students(first_name, last_name, address, class, matg, scig, eng, dug, artg, sum, avg) VALUES (?,?,?,?,?,?,?,?,?,?,?)",student_attributes)
    conn.commit() 
    
    conn.close()

#Function to delete an entry from the database according to ROW ID
def delete(x):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "daba.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("DELETE FROM students WHERE rowid=?",str(x)) 
    conn.commit()
    print("Record deleted successfully ")
    
    c.execute("VACUUM")
    conn.commit()
    
    conn.close()

#Function to edit a specific value on a row
def editkey_value(i):
   
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "daba.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    valid_types = ["first_name", "last_name", "address", "class", "matg" ,"scig", "eng", "dug", "artg"]
    
    while True:
        print("first_name last_name address class matg scig eng dug artg")  
        
        type_of_attribute = input("Which one? ").lower()
        
        if type_of_attribute in valid_types[0:4] :
            value_of_attribute = input_checker(input("Please enter the new value. ").upper(), "STRING")
            value_of_attribute = "'"+value_of_attribute+"'"
            c.execute('UPDATE students SET %s=%s WHERE rowid=%s' %(type_of_attribute,value_of_attribute,i))
            conn.commit()
            break
        elif type_of_attribute in valid_types[4:9]:
            value_of_attribute = input_checker(input("Please enter the new value. ").upper(), "FLOAT")
            value_of_attribute = "'"+str(value_of_attribute)+"'"
            c.execute('UPDATE students SET %s=%s WHERE rowid=%s' %(type_of_attribute,value_of_attribute,i))
            conn.commit()
                     
            c.execute("SELECT matg, scig, eng, dug, artg FROM students WHERE rowid=%s" %(i))
            results = c.fetchone()
            
            #Avg Calculator
            sum_grade = 0
            for value in results:
                sum_grade += float(value)
            
            #Shows the sum of all grades and grade average to 1 d.p.
            avg_grade = sum_grade / 5.0
            
            
            c.execute('UPDATE students SET sum=%s, avg=%s  WHERE rowid=%s' %(sum_grade,avg_grade,i))
            conn.commit()                    
            break
            
        else:
            print("Invalid input. Please try again.")
        
    conn.close()

#Function to completely replace a row
def editkey_full(i,student_attributes = ()):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "daba.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    print("Let's enter all the new values, shall we?")
    
    if(student_attributes==()):
        student_attributes += (input_checker(input("First name: ").upper(), "STRING"),)
        student_attributes += (input_checker(input("Last name: ").upper(), "STRING"),)
        student_attributes += (input_checker(input("Address: ").upper(), "STRING"),)
        student_attributes += (input_checker(input("Class: ").upper(), "STRING"),)
        student_attributes += (input_checker(input("Mathematics grade: ").upper(), "FLOAT"),)
        student_attributes += (input_checker(input("Science grade: ").upper(), "FLOAT"),)
        student_attributes += (input_checker(input("English grade: ").upper(), "FLOAT"),)
        student_attributes += (input_checker(input("Dutch grade: ").upper(), "FLOAT"),)
        student_attributes += (input_checker(input("Art grade: ").upper(), "FLOAT"),)
    print("----These will be the new values----")
    print(student_attributes)
    print("----These will be the new values----")
    #Avg Calculator
    sum_grade = 0
    for value in student_attributes[4:8]:
        sum_grade += float(value)
    
    student_attributes += (sum_grade,)
    
    #Shows the sum of all grades and grade average to 1 d.p.
    avg_grade = sum_grade / 5.0
    
    student_attributes += (avg_grade,)
    
    
    student_attributes += (str(i),)
    
    c.execute("UPDATE students SET first_name=?, last_name=?, address=?, class=?, matg=?, scig=?, eng=?, dug=?, artg=?, sum=?, avg=? WHERE rowid=?",student_attributes)
    conn.commit()
    print("!executed!")
    
    conn.close()

#Search Function!    
def searchfunction(decision="",student=""):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "daba.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    if (decision==""):
        decision = input("Search by [F]irst name, [L]ast name, or [R]ow ID? ").upper()
    
    
    if decision == "F":
        if (student==""):
            student = input_checker(input("What is the first name of the student you are searching for? ").upper(), "STRING")
        c.execute("SELECT rowid,* FROM students WHERE first_name= '%s'" %(student))
        
        student_rows = (c.fetchall())
        
        print(tabulate(student_rows, headers=['Row ID', 'First Name', 'Last Name', 'Address', 'Class', 'Math Grade', 'Science Grade', 'English Grade', 'Dutch Grade', 'Art Grade', 'Sum Grade', 'Average Grade']))
        
        if student_rows == []:
            print("No Matching Records found.")
            
    #Last Name Search
    elif decision == "L":
        if (student==""):
            student = input_checker(input("What is the last name of the student you are searching for? ").upper(), "STRING")
        c.execute("SELECT rowid,* FROM students WHERE last_name= '%s'" %(student))
        
        student_rows = (c.fetchall())
        
        print(tabulate(student_rows, headers=['Row ID', 'First Name', 'Last Name', 'Address', 'Class', 'Math Grade', 'Science Grade', 'English Grade', 'Dutch Grade', 'Art Grade', 'Sum Grade', 'Average Grade']))
        
        if student_rows == []:
            print("No Matching Records found.")
        
    #Row ID Search
    elif decision == "R":
        if (student==""):
            student = input_checker(input("What is the Row ID of the student you are searching for? ").upper(), "INTEGER")
        c.execute("SELECT rowid, * FROM students WHERE rowid= '%s'" %(student))
        
        student_rows = (c.fetchall())
        
        print(tabulate(student_rows, headers=['Row ID', 'First Name', 'Last Name', 'Address', 'Class', 'Math Grade', 'Science Grade', 'English Grade', 'Dutch Grade', 'Art Grade', 'Sum Grade', 'Average Grade']))
                
        if student_rows == []:
            print("No Matching Records found.")
   
    conn.close()
    
#Prints all Rows
def print_all(caller):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "daba.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()       
    c.execute('SELECT rowid, * FROM students')
    all_rows = c.fetchall()
    if(caller=="cl"):
        print("Here are all the entries in our database:")
        print(tabulate(all_rows, headers=['Row ID', 'First Name', 'Last Name', 'Address', 'Class', 'Math Grade', 'Science Grade', 'English Grade', 'Dutch Grade', 'Art Grade', 'Sum Grade', 'Average Grade']))
    elif(caller=="gui"):
        return(all_rows)


    conn.close()

def classAvgs():
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "daba.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    #This first part finds all student classes that exist in the database
    classes = []
    c.execute("SELECT class FROM students")
    all_rows = c.fetchall()
    
    #Creating a list of the classes, and making sure there are no duplicates
    for i in all_rows:
        if i[0] not in classes:
            classes.append(i[0])
            
    #This part now calculates average per class, then outputs it and also checks for highest average
    highest_class_avg = 0
    final_class_output = []
    for student_class in classes:
        c.execute("SELECT matg, scig, eng, dug, artg FROM students WHERE class= '%s'" %(student_class))
        results = c.fetchall()
        
        class_total = 0
        for grade_list in results:

            #Avg Calculator
            sum_grade = 0
            for grade_value in grade_list:
                sum_grade += float(grade_value)
    
            #Calculates the student grade average and adds it to the class total
            avg_grade = sum_grade/5.0
            class_total += avg_grade
        
        class_avg = round(class_total/len(results),1)
        
        #Print Class Average
        final_class_output.append(( student_class + " Average Score: " + str(class_avg)))
            
        #Calculate if current class avg is higher than highest class avg, and replace it if it is
        if class_avg > highest_class_avg:
            highest_class = student_class
            highest_class_avg = class_avg
    
    #Apply inline formatting here as well, idk why is it not working for me, on it
    final_class_output.append("The class with the best average is Class " + highest_class + ", with an overall average of " + str(highest_class_avg) + ".")
    
    conn.close()

    return(final_class_output)


#Validation checker! Multifunctional tool, so make good use of it!
def input_checker(user_input, input_type):
    while True:
        if input_type == "INTEGER":
            try:
                user_input = int(user_input)
                return (user_input)
            except ValueError:
                user_input = input("This is an invalid input. Please try again: ")
                
        elif input_type == "FLOAT":
            try:
                user_input = float(user_input)
                return (user_input)
            except ValueError:
                user_input = input("This is an invalid input. Please try again: ")
                
        elif input_type == "STRING":
            try:
               user_input = int(user_input)
               user_input = input("This is an invalid input. Please try again: ")
            except ValueError:
              try:
                user_input = float(user_input)
                user_input = input("This is an invalid input. Please try again: ")
              except ValueError:
                  return (user_input)
              
                
"""
REDUNDANT MAIN CODE


if __name__ == "__main__":
    while True:
        sw = input("[A]dd, [D]elete, [E]dit, [S]earch, [C]lass Averages, [P]rint all - ").upper() #+1 I didn't think of this :D 
    
        if (sw == "A"):
            newEntry()
            
        elif (sw == "D"):
            delete(input_checker(input("Please enter the ID of the row you want to delete: "), "INTEGER"))
            
        elif (sw == "E"):
            print("It's okay, we all make mistakes sometimes.")
            row_to_edit = int(input_checker(input("Which row would you like to edit? "), "INTEGER"))
            lifechoices = input("Do you want to edit a specific [V]alue or a whole [R]ow? ").upper()
            
            while True:
                if (lifechoices == "V"):
                    editkey_value(row_to_edit)
                    break;
                    
                elif (lifechoices == "R"):
                    editkey_full(row_to_edit)
                    break;
                else:
                    lifechoices = input("Invalid Input. Please try again: ").upper()
                
        elif (sw == "S"):
            searchfunction()
            
        elif (sw == "P"):
            print_all()
                
        elif (sw == "C"):
            classAvgs()
            
        elif (sw == "EXIT"):
            break
        
        else:
            print("Invalid input. Please try again.")

"""