"""
@samya List of Edits - Date: 22/02/2020

* Imported the main code from studentdatabasemanager.py


"""
import StudentDatabaseManager as sdm
from tabulate import tabulate

if __name__ == "__main__":
    while True:
        sw = input("[A]dd, [D]elete, [E]dit, [S]earch, [C]lass Averages, [P]rint all - ").upper()
    
        if (sw == "A"):
            sdm.newEntry()
            
        elif (sw == "D"):
            sdm.delete(sdm.input_checker(input("Please enter the ID of the row you want to delete: "), "INTEGER"))
            
        elif (sw == "E"):
            print("It's okay, we all make mistakes sometimes.")
            row_to_edit = int(sdm.input_checker(input("Which row would you like to edit? "), "INTEGER"))
            lifechoices = input("Do you want to edit a specific [V]alue or a whole [R]ow? ").upper()
            
            while True:
                if (lifechoices == "V"):
                    sdm.editkey_value(row_to_edit)
                    break;
                    
                elif (lifechoices == "R"):
                    sdm.editkey_full(row_to_edit)
                    break;
                else:
                    lifechoices = input("Invalid Input. Please try again: ").upper()
                
        elif (sw == "S"):
            lookwhatifound = sdm.searchfunction()
            if not lookwhatifound == "No Matching Records found.":
                print(tabulate(lookwhatifound,headers=['Row ID', 'First Name', 'Last Name', 'Address', 'Class', 'Math Grade', 'Science Grade', 'English Grade', 'Dutch Grade', 'Art Grade', 'Sum Grade', 'Average Grade']))
            else:
                print("No Matching Records found.")

        elif (sw == "P"):
            sdm.print_all("cl")
                
        elif (sw == "C"):
            #Since the output of the function is multiple variables, they were collated in a list for ease of access
            print("\n".join(sdm.classAvgs()))
            
        elif (sw == "EXIT" or sw == "EXIT()"):
            break
        
        else:
            print("Invalid input. Please try again.")