"""
@samya List of Edits - Date: 22/02/2020

* Imported the main code from studentdatabasemanager.py


"""
import StudentDatabaseManager as sdb

if __name__ == "__main__":
    while True:
        sw = input("[A]dd, [D]elete, [E]dit, [S]earch, [C]lass Averages, [P]rint all - ").upper()
    
        if (sw == "A"):
            sdb.newEntry()
            
        elif (sw == "D"):
            sdb.delete(sdb.input_checker(input("Please enter the ID of the row you want to delete: "), "INTEGER"))
            
        elif (sw == "E"):
            print("It's okay, we all make mistakes sometimes.")
            row_to_edit = int(sdb.input_checker(input("Which row would you like to edit? "), "INTEGER"))
            lifechoices = input("Do you want to edit a specific [V]alue or a whole [R]ow? ").upper()
            
            while True:
                if (lifechoices == "V"):
                    sdb.editkey_value(row_to_edit)
                    break;
                    
                elif (lifechoices == "R"):
                    sdb.editkey_full(row_to_edit)
                    break;
                else:
                    lifechoices = input("Invalid Input. Please try again: ").upper()
                
        elif (sw == "S"):
            sdb.searchfunction()
            
        elif (sw == "P"):
            sdb.print_all()
                
        elif (sw == "C"):
            print(sdb.classAvgs())
            
        elif (sw == "EXIT" or sw == "EXIT()"):
            break
        
        else:
            print("Invalid input. Please try again.")