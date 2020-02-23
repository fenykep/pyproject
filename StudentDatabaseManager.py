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

*Write the code more readable (spaces between symbols).
*Use more descriptive variable names to make it more understandable and easier to follow.

"""

#Import of libraries and setting up the sqlite commands
import sqlite3

conn = sqlite3.connect('daba.db')
c = conn.cursor()
#Function to add a new entry to the database
#QUESTION 1(JUD: Why can't we use 'student' or another word more descriptive instead of 'push', it is very confusing to read, at least for me)
#QUESTION 2(JUD: Why so many interrogation marks in the commant of c.execute?)
#Q1: we can change it, I just set it because the push variable stores the data that we are pushing to the SQL "server"
#Q2: With those marks you can tell python that you want to insert some variables into a string, similar
#       to write print("welcome home",name," today is ",nameofday) and it handles variables better I think

def newEntry():
    push = ()
    push += (input("First Name: ").upper(),)
    push += (input("Last Name: ").upper(),)
    push += (input("Address: ").upper(),)
    push += (input("Class: ").upper(),)
    push += (input("Mathematics grade: "),)
    push += (input("Science grade: "),)
    push += (input("English grade: "),)
    push += (input("Dutch grade: "),)
    push += (input("Art grade: "),)
    c.execute("INSERT INTO students(first_name, last_name, address, class, matg, scig, eng, dug, artg) VALUES (?,?,?,?,?,?,?,?,?)",push)
    conn.commit() 

#Function to delete an entry from the database according to ROW ID
def delete(x):
    c.execute("DELETE FROM students WHERE rowid=?",str(x)) 
    conn.commit()
    print("Record deleted successfully ")
    
    c.execute("VACUUM")
    conn.commit()

#Function to edit a specific value on a row
def editkey_value(i):
    print("first_name last_name address class matg scig eng dug artg")
    type_of_attribute = input("Which one? ").lower()
    value_of_attribute = input("Please enter the new value. ").upper()
    value_of_attribute = "'"+value_of_attribute+"'"
    c.execute('UPDATE students SET %s=%s WHERE rowid=%s' %(type_of_attribute,value_of_attribute,i))
    conn.commit()

#Function to completely replace a row
def editkey_full(i):
    push = ()
    push += (input("First Name: ").upper(),)
    push += (input("Last Name: ").upper(),)
    push += (input("Address: ").upper(),)
    push += (input("Class: ").upper(),)
    push += (input("Mathematics grade: "),)
    push += (input("Science grade: "),)
    push += (input("English grade: "),)
    push += (input("Dutch grade: "),)
    push += (input("Art grade: "),)
    push += (str(i),)
    
    #Samya: Why is this edited in id as opposed to name, like the others? Abel: Because the name is not unique
    c.execute("UPDATE students SET first_name=?, last_name=?, address=?, class=?, matg=?, scig=?, eng=?, dug=?, artg=? WHERE rowid=?",push)
    conn.commit()

#Search Function!    
def searchfunction():
    decision = input("Search by [F]irst name, [L]ast name, or [R]ow ID? ").upper()
    
    #First Name Search
    #QUESTION: what is fetchone for? what does it do?)
    #c.execute only tells the database what to look for, but it doesn't listen (as many people in our current world, sadly)
    #c.fetchone is the one that listens to the reply (one line at a time), while c.fetchall gets every line
    if decision == "F":
        student = input("What is the first name of the student you are searching for?")
        c.execute("SELECT rowid,* FROM students WHERE first_name= '%s'" %(student))
        print(c.fetchone())
        c.execute("SELECT matg, scig, eng, dug, artg FROM students WHERE first_name= '%s'" %(student))
        results = c.fetchone()
        
        #Avg Calculator
        sum_grade = 0
        for s in results:
            sum_grade += float(s)

        #Shows the sum of all grades and grade average to 1 d.p.
        avg_grade = sum_grade / 5.0
        print("Sum of all Grades: %.1f" % sum_grade)
        print("Grade Average: %.1f" % avg_grade)
        
    #Last Name Search
    elif decision == "L":
        student = input("What is the last name of the student you are searching for?")
        c.execute("SELECT rowid,* FROM students WHERE last_name= '%s'" %(student))
        print(c.fetchone())
        c.execute("SELECT matg, scig, eng, dug, artg FROM students WHERE last_name= '%s'" %(student))
        results = c.fetchone()
        
        #Avg Calculator
        sum_grade = 0
        for s in results:
            sum_grade += float(s)

        #Shows the sum of all grades and grade average to 1 d.p.
        avg_grade = sum_grade / 5.0
        print("Sum of all Grades: %.1f" % sum_grade)
        print("Grade Average: %.1f" % avg_grade)
        
    #Row ID Search
    elif decision == "R":
        student = input("What is the Row ID of the student you are searching for?")
        c.execute("SELECT rowid, * FROM students WHERE rowid= '%s'" %(student))
        print(c.fetchone())
        c.execute("SELECT matg, scig, eng, dug, artg FROM students WHERE rowid= '%s'" %(student))
        results = c.fetchone()
        
        #Avg Calculator
        sum_grade = 0
        for s in results:
            sum_grade += float(s)

        #Shows the sum of all grades and grade average to 1 d.p.
        avg_grade = sum_grade / 5.0
        print("Sum of all Grades: %.1f" % sum_grade)
        print("Grade Average: %.1f" % avg_grade)
        
    else:
        print("Invalid Input.")
   
#Prints all Rows

def print_all():
    print("Here are all the entries in our database:")
    c.execute('SELECT rowid, * FROM students')
    print(c.fetchone())
    all_rows = c.fetchall()
    for i in all_rows:
        print(i)

def classAvgs():
    #!! Tell the code to connect to the DB when SDM.py is called, 
    conn = sqlite3.connect('daba.db')
    c = conn.cursor()
    #   so we dont have to do this in every function

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
    for i in classes:
        c.execute("SELECT matg, scig, eng, dug, artg FROM students WHERE class= '%s'" %(i))
        results = c.fetchall()
        
        class_total = 0
        for j in results:

            #Avg Calculator
            sum_grade = 0
            for s in j:
                sum_grade += float(s)
    
            #Calculates the student grade average and adds it to the class total
            avg_grade = sum_grade/5.0
            class_total += avg_grade
        
        class_avg = round(class_total/len(results),1)
        
        #Print Class Average
        print( i,"Average Score: " + str(class_avg))
            
        #Calculate if current class avg is higher than highest class avg, and replace it if it is
        if class_avg > highest_class_avg:
            highest_class = i
            highest_class_avg = class_avg
    
    #Apply inline formatting here as well, idk why is it not working for me, am on it
    return("The class with the best average is Class " + highest_class + ", with an overall average of " + str(highest_class_avg) + ".")


if __name__ == "__main__":
    
    while True:
        sw = input("[A]dd, [D]elete, [E]dit, [S]earch, [C]lass Averages, [P]rint all - ").upper() #+1 I didn't think of this :D 
    
        if (sw == "A"):
            print("Please enter the details of the new student.")
            newEntry()
            
        elif (sw == "D"):
            delete(input("Please enter the ID of the row you want to delete: "))
            
        elif (sw == "E"):
            print("It's okay, we all make mistakes sometimes.")
            row_to_edit = int(input("Which row would you like to edit? "))
            lifechoices = input("Do you want to edit a specific [V]alue or a whole [R]ow? ").upper()
            
            if (lifechoices == "V"):
                editkey_value(row_to_edit)
                
            elif (lifechoices == "R"):
                print("Let's enter all the new values, shall we?")
                editkey_full(row_to_edit)
                
        elif (sw == "S"):
            searchfunction()
            
        elif (sw == "P"):
            print_all()
                
        elif (sw == "C"):
            classAvgs()
            
        elif (sw == "EXIT"):
            break
    
conn.close()
