import sqlite3
import math
conn = sqlite3.connect('daba.db')
c = conn.cursor()
#Superimportant!! Somehow you have to either show the rowID or every time you remove a row, you have to update all the rowidS
def newEntry(a):
	c.execute("INSERT INTO students(name, address, class, matg, scig, eng, dug, artg) VALUES (?,?,?,?,?,?,?,?)",push)
	conn.commit() 

def delete(x):
	c.execute("DELETE FROM students WHERE rowid=?",str(x))
	conn.commit()

def editkegy(i,valtoc,val):
	val="'"+val+"'"
	c.execute('UPDATE students SET %s=%s WHERE rowid=%s' %(valtoc,val,i))
	conn.commit()

def editke(stuff):
	c.execute("UPDATE students SET name=?, address=?, class=?, matg=?, scig=?, eng=?, dug=?, artg=? WHERE rowid=?",stuff)
	conn.commit()

while True:
	sw=raw_input("[A]dd, [D]elete, [E]dit, [S]earch, [P]aint")
	if (sw=="A" or sw=="a"):
		print("Please enter the details of the new student.")
		#This could be cleaned up a bit
		push=()
		push+=(raw_input("Name: "),)
		push+=(raw_input("Address: "),)
		push+=(raw_input("Class: "),)
		push+=(raw_input("Mathematics grade: "),)
		push+=(raw_input("Science grade: "),)
		push+=(raw_input("English grade: "),)
		push+=(raw_input("Dutch grade: "),)
		push+=(raw_input("Art grade: "),)
		newEntry(push)
	elif (sw=="D" or sw=="d"):
		delete(raw_input("Please enter the ID of the row you want to delete."))
	elif (sw=="E" or sw=="e"):
		print("It's okay, we all make mistakes sometimes.")
		sortoedit=int(raw_input("Which row would you like to edit?"))
		lifechoices=raw_input("Do you want to edit a specific [V]alue or a whole [R]ow?")
		if (lifechoices=="V" or lifechoices == "v"):
			print("name address class matg scig eng dug artg")
			pumuroko=raw_input("Which one?")
			amirevaltunk=raw_input("Please enter the new value.")
			editkegy(sortoedit,pumuroko,amirevaltunk)
		elif (lifechoices=="R" or lifechoices == "r"):
			print("Let's enter all the new values, shall we?")
			push=()
			push+=(raw_input("Name: "),)
			push+=(raw_input("Address: "),)
			push+=(raw_input("Class: "),)
			push+=(raw_input("Mathematics grade: "),)
			push+=(raw_input("Science grade: "),)
			push+=(raw_input("English grade: "),)
			push+=(raw_input("Dutch grade: "),)
			push+=(raw_input("Art grade: "),)
			push+=(str(sortoedit),)
			editke(push)
	elif (sw=="S" or sw=="s"):
		suspect = raw_input("Who you lookin for?")
		#Here we could add a function that slices the names, so we can look for Bob and not only Bob Smith Jr.
		c.execute("SELECT * FROM students WHERE name= '%s'" %(suspect))
		print(c.fetchone())
		c.execute("SELECT matg, scig, eng, dug, artg FROM students WHERE name= '%s'" %(suspect))
		osszesjegyek=c.fetchone()
		atlag=0
		for s in osszesjegyek:
			atlag+=int(s)
		print("Average: ",atlag/5.0)
	elif (sw=="P" or sw=="p"):
		print("Here are all the entries in our database:")
		c.execute('SELECT * FROM students')
		print(c.fetchone())
		dolgok = c.fetchall()
		for i in dolgok:
			print(i)
conn.close()