import sqlite3
import math
conn = sqlite3.connect('daba.db')
c = conn.cursor()
#Superimportant!! Somehow you have to either show the rowID or every time you remove a row, you have to update all the rowidS
def newEntry(a):
	c.execute("INSERT INTO students(name, address, class, matg, scig, eng, dug, artg) VALUES (?,?,?,?,?,?,?,?)",push)
	conn.commit() #tuggyukmi

def delete(x):
	c.execute("DELETE FROM students WHERE rowid=?",str(x))
	conn.commit()

def editkegy(i,valtoc,val):
	val="'"+val+"'"
	#print('UPDATE students SET %s=%s WHERE rowid=%s' %(valtoc,val,i))
	c.execute('UPDATE students SET %s=%s WHERE rowid=%s' %(valtoc,val,i))
	conn.commit()

def editke(stuff):
	c.execute("UPDATE students SET name=?, address=?, class=?, matg=?, scig=?, eng=?, dug=?, artg=? WHERE rowid=?",stuff)
	conn.commit()

while True:
	sw=raw_input("[A]dd, [D]elete, [E]dit, [S]earch, [P]aint")
	if (sw=="A" or sw=="a"):
		print("Jovan bazmeg majd hozzaadom, pattogja ma anyadba el!")
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
		print("Torold a segged, ne engem baszogass.")
		delete(raw_input("Mindegyis, mit akarsz?"))
	elif (sw=="E" or sw=="e"):
		print("Nem kolaztad volna el a tamogatast, most lenne szerkesztoseg.")
		sortoedit=int(raw_input("Which line shall I do?"))
		lifechoices=raw_input("Do you want to edit a specific [V]alue or a whole [R]ow?")
		if (lifechoices=="V" or lifechoices == "v"):
			print("name address class matg scig eng dug artg")
			pumuroko=raw_input("Which one?")
			amirevaltunk=raw_input("What to set it?")
			editkegy(sortoedit,pumuroko,amirevaltunk)
		elif (lifechoices=="R" or lifechoices == "r"):
			print("Ezt persze nem tudtad volna korabban atgondolni ugye?")
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
		print("Faszom fog neked itt keresgetni.")
		suspect = raw_input("Who you lookin for?")
		c.execute("SELECT * FROM students WHERE name= '%s'" %(suspect))
		print(c.fetchone())
		c.execute("SELECT matg, scig, eng, dug, artg FROM students WHERE name= '%s'" %(suspect))
		osszesjegyek=c.fetchone()
		atlag=0
		for s in osszesjegyek:
			atlag+=int(s)
		
		#print(atlag)
		print("Average: ",atlag/5.0)
		#print("fa")
		#print(osszesjegyek[0])
		#for k in xrange(5):
		#	print(c.fetchone()[k])
	elif (sw=="P" or sw=="p"):
		print("Mit kutakodsz te spion geci?")
		c.execute('SELECT * FROM students')
		print(c.fetchone())
		dolgok = c.fetchall()
		for i in dolgok:
			print(i)
		

#c.execute('''CREATE TABLE students(id text primary key, name text, address text, class integer, matg text, scig text, eng text, dug text, artg text)''')
#name #address #class #matg #scig #eng #dug #artg

#Ez meno cucc, keep it
#for row in c.execute("select name, address from students WHERE rowid=1"):
#    print(row)

#c.execute("SELECT * FROM students WHERE name=?", "Bob")
#print(c.fetchone())
#newEntry("Berci")
#delete(1)




conn.close()