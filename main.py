import sqlite3
import names
conn = sqlite3.connect('daba.db')
c = conn.cursor()

#our database will look like this:
	#ID |Name|Address|Class| MathGrades|SciGrades|EngRades|DutchGrades|ArtGrades
	#---|----|-------|-----|-----------|---------|--------|-----------|---------#
	# 0	|Bob | Cairo |  2  |   4,4,5   |  2,1,6  |   8,8  |	   3,9	  | 7,7,1,9
	#int|str |str 	 |int  |   str 	   |  str  	 |  str	  |    str 	  | str

names.lines(42)
namelist=[]
adds=[]
classes=[]
maths=[]
scis=[]
engs=[]
dutchs=[]
artss=[]

lista=[namelist,adds,classes,maths,scis,engs,dutchs,artss]

def newEntry(inputs):
	for i in range(len(lista)-1):
		lista[i].append(inputs[i])

def editEntry(index):
	for i in lista:
		print(i[index])

def delete(index):
	for i in lista:
		del i[index]

def show(name):
	for i in namelist:
		if (name in i.split(' ')):
			print("The suspect is at line",i)

def save():
	#iterate through all the lists, create strings and write to a newline in the txt

def load():
	#split up the lines !(indicate theend of name)! and append them to the lists