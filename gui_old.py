import StudentDatabaseManager as sdm
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

'''
Okay, so I have to rewrite a great chunk of the code
there has to be the listbox, which is updated after every function
I'll try to get rid of the object oriented parts as I want to learn
them a bit more slowly.
"UX" design:
- ditch the menubar (or keep it for the average and search functions)
-listbox with a stickied scrollbar
-3 text and 5 float entries under them
-3 buttons: add, edit, delete
'''
	


def avgPrint():
	avgoutput = "\n".join(sdm.classAvgs())
	messagebox.showinfo('BestClass',avgoutput)

def donothing():
	filewin = tk.Toplevel(window)
	button = tk.Button(filewin, text="Do nothing button")
	button.pack()

def find(t="F"):
	whotofind = simpledialog.askstring("Input", "Name?",parent=tk.Tk()).upper()
	sdm.searchfunction(t,whotofind)


def erase():
	#Here I'd like to use your input checker, or a widget that can only accept numerical input
	#Also it has to check if the index is in range of the db
	theTargetoftheTerminator = sdm.input_checker(simpledialog.askstring("Input", "RowID?",parent=tk.Tk()).upper(),"INTEGER",)
	print(theTargetoftheTerminator)
	curselection()
	sdm.delete(theTargetoftheTerminator)
	#Also after removing the entries from the db I would either have to call
	#the sql again or just delete the same from the list as well



'''
def newalue(be):
	sdm.newEntry(address="Belen")
	sdm.print_all("cl")
'''
class Window(tk.Tk):
	"""docstring for window"""
	def __init__(self):
		super().__init__()

		self.title("Student Database Manager® 2020")
		self.geometry('690x350')
		#Here I have put a label that is tabulated according to
		#the database
		self.lb1 = tk.Listbox(self,width=80, height=20)
		self.lb1.grid(row=1, column=0, columnspan=8)
		self.yscroll = tk.Scrollbar(command=self.lb1.yview, orient=tk.VERTICAL)
		self.yscroll.grid(row=1, column=7,sticky=tk.N+tk.S)
		self.lb1.configure(yscrollcommand=self.yscroll.set)
		k=0
		for i in sdm.print_all("gui"):
			self.lb1.insert(k,i)
			k+=1

		
		self.namein = tk.Entry(self)
		self.namein.grid(row=3,column=0)
		self.namelab = tk.Label(self, text="Name")
		self.namelab.grid(row=2,column=0)
		self.addressin = tk.Entry(self)
		self.addressin.grid(row=3,column=1)
		self.addlab = tk.Label(self, text="Address")
		self.addlab.grid(row=2,column=1)
		self.classin = tk.Entry(self)
		self.classin.grid(row=3,column=2)
		self.classlab = tk.Label(self, text="Class")
		self.classlab.grid(row=2,column=2)
		self.mgradein = tk.Entry(self)
		self.mgradein.grid(row=3,column=3)
		self.gradelab = tk.Label(self, text="Grades")
		self.gradelab.grid(row=2,column=3)
		
		

		#shall we convert this to more object-oriented as well? 
		#Anyways these lines just create the menubar
		menubar=tk.Menu(self)
		smenu=tk.Menu(menubar, tearoff=0)

		smenu.add_command(label="FirstName", command=lambda:find("F"))
		smenu.add_command(label="LastName", command=lambda:find("L"))
		smenu.add_command(label="RowID", command=lambda:find("R"))

		smenu.add_separator()

		smenu.add_command(label="Exit", command=self.quit)
		menubar.add_cascade(label="Search", menu=smenu)


		fmenu = tk.Menu(menubar, tearoff=0)
		#fmenu.add_command(label="Add", command=newalue(self.namein.get()))
		fmenu.add_command(label="Delete", command=erase)
		fmenu.add_command(label="Edit", command=donothing)
		#fmenu.add_command(label="Print", command=donothing)
		fmenu.add_command(label="Averages", command=avgPrint)

		menubar.add_cascade(label="Entry", menu=fmenu)
		self.config(menu=menubar)


if __name__ == "__main__":
	window = Window()
	window.mainloop()
