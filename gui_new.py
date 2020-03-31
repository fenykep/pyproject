'''
2020.03.25 - Ábel
This is not a best solution, but as speed doesnt matter and its getting more and more messy to 
sync the DB with the ListBox Ill just do a full DB call with every update.
Ill leave the attempts commented out.

Also tiny thing but shall everything be uppercase?

Can you please optimize the entries so they go through your checker algorithm?

Also so far I don't see more bad behavior, but while you work with it try to test it
with weird user inputs to see where does it fail.

Oh and the search stuff doesnt yet work.
'''

import StudentDatabaseManager as sdm
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

sw={
	'm':5,
	's':6,
	'e':7,
	'd':8,
	'a':9
}

#1.4 2.8 4.5 5.6 8

def callTheWholeDB():
	lb1.delete(0,'end')
	for i in sdm.print_all("gui"):
		lb1.insert('end',i)

def zeroEntries():
	namein.delete(0,len(namein.get()))
	addressin.delete(0,len(addressin.get()))
	classin.delete(0,len(classin.get()))
	mgradein.delete(0,len(mgradein.get()))

def avgPrint():
	avgoutput = "\n".join(sdm.classAvgs())
	messagebox.showinfo('BestClass',avgoutput)

def find(t="F"):
	whotofind = simpledialog.askstring("Input", "Name?",parent=tk.Tk()).upper()
	sdm.searchfunction(t,whotofind)

def erase(theTargetoftheTerminator):
	#theTargetoftheTerminator = sdm.input_checker(simpledialog.askstring("Input", "RowID?",parent=tk.Tk()).upper(),"INTEGER",)
	print("todelete:",theTargetoftheTerminator)
	lb1.delete (theTargetoftheTerminator)
	sdm.delete(theTargetoftheTerminator)
	
def clickDel():
	MsgBox = tk.messagebox.askquestion ('Delete','Are you sure you want to delete %s entry?' %(lb1.curselection()),icon = 'warning')
	if (MsgBox == 'yes'):
		erase(lb1.curselection()[0])
		sdm.delete(lb1.curselection()[0])

def edit():
	MsgBox = tk.messagebox.askquestion ('Edit','Are you sure you want to edit %s entry?' %(lb1.curselection()),icon = 'warning')
	#if letter is present at grade field, only edit those grades like this:[m-8.1 e-2.7]
	#if noletter -> update all nonempty vals in selected row
	if (MsgBox == 'yes'):
		newval=list(lb1.get(lb1.curselection()))
		newval.remove(newval[-2]) #bc the sdm recalculates the avg & sum anyways
		newval.remove(newval[-1])
		print("old: ",newval)
		if (not mgradein.get().replace('.','').replace(' ','').isdigit() and not mgradein.get()==""):
			print("Miez, betuteszta?")
			print("mgradein: ",mgradein.get())
			newGrades=mgradein.get().split(' ')
			for i in newGrades:
				newval[sw.get(i.split('-')[0])]=i.split('-')[1]
			
			mgradein.delete(0,len(mgradein.get()))
		else:
			if not namein.get()=='':
				if not namein.get().split(' ')[0]=='':
					newval[1]=namein.get().split(' ')[0]
				if not namein.get().split(' ')[1]=='':
					newval[2]=namein.get().split(' ')[1]
			if not addressin.get()=='':
				newval[3]=addressin.get()
			if not classin.get()=='':
				newval[4]=classin.get()
			if not mgradein.get()=='':
				for i in range(5):
					newval[5+i]=mgradein.get().split(' ')[i]

		newval.remove(newval[0])
		print("beforesending: ",tuple(newval))
		print("rowID: ",lb1.curselection()[0]+1)
		sdm.editkey_full(lb1.curselection()[0]+1,tuple(newval))
		#newval.insert(0,lb1.curselection()[0])
		#print("updated: ",newval)
		#lb1.insert(lb1.curselection(),newval)
		#lb1.delete(lb1.curselection())	
		callTheWholeDB()

		zeroEntries()


def addEntry():
	newval=[0]*9
	newval[0]=namein.get().split(' ')[0]
	newval[1]=namein.get().split(' ')[1]
	newval[2]=addressin.get()
	newval[3]=classin.get()
	print("newval: ",newval)
	for i in range(5):
		newval[4+i]=mgradein.get().split(' ')[i]
	sdm.newEntry(tuple(newval))
	#newval.insert(0,lb1.size()+1)
	#lb1.insert('end',newval)	
	callTheWholeDB()
	zeroEntries()


window = tk.Tk()

window.title("Student Database Manager® 2020")
window.geometry('690x350')
#Here I have put a label that is tabulated according to
#the database
lb1 = tk.Listbox(window,width=80, height=20)
lb1.grid(row=1, column=0, columnspan=8)
yscroll = tk.Scrollbar(command=lb1.yview, orient=tk.VERTICAL)
yscroll.grid(row=1, column=7,sticky=tk.N+tk.S)
lb1.configure(yscrollcommand=yscroll.set)

callTheWholeDB()

#Prolly this could be a tad more elegant
namein = tk.Entry(window)
namein.grid(row=3,column=0)
namelab = tk.Label(window, text="Name")
namelab.grid(row=2,column=0)
addressin = tk.Entry(window)
addressin.grid(row=3,column=1)
addlab = tk.Label(window, text="Address")
addlab.grid(row=2,column=1)
classin = tk.Entry(window)
classin.grid(row=3,column=2)
classlab = tk.Label(window, text="Class")
classlab.grid(row=2,column=2)
mgradein = tk.Entry(window)
mgradein.grid(row=3,column=3)
gradelab = tk.Label(window, text="Grades")
gradelab.grid(row=2,column=3)


#--This part generates the menubar--#
menubar=tk.Menu(window)
smenu=tk.Menu(menubar, tearoff=0)

smenu.add_command(label="FirstName", command=lambda:find("F"))
smenu.add_command(label="LastName", command=lambda:find("L"))
smenu.add_command(label="RowID", command=lambda:find("R"))

smenu.add_separator()

smenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Search", menu=smenu)


fmenu = tk.Menu(menubar, tearoff=0)
fmenu.add_command(label="Add", command=addEntry)
fmenu.add_command(label="Delete", command=clickDel)
fmenu.add_command(label="Edit", command=edit)
fmenu.add_command(label="Averages", command=avgPrint)

menubar.add_cascade(label="Entry", menu=fmenu)
window.config(menu=menubar)

window.mainloop()
