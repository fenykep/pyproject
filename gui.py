import StudentDatabaseManager as sdm
import tkinter as tk
from tkinter import messagebox


def avgPrint():
	messagebox.showinfo('BestClass',sdm.classAvgs())

def donothing():
   filewin = tk.Toplevel(window)
   button = tk.Button(filewin, text="Do nothing button")
   button.pack()

def erase():
	sdm.delete()

	

class Window(tk.Tk):
	"""docstring for window"""
	def __init__(self):
		super().__init__()
		#self.arg = arg
		'''
		self.canvas = tk.Canvas(self)
		self.frame = tk.Frame(self.canvas)
		#self.tframe = tk.Frame(self)
		self.scrollbar = tk.Scrollbar(self.canvas,orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		'''
		self.title("Student Database Manager® 2020")
		self.geometry('1200x600')
		#Here I have put a label that is tabulated according to
		#the database
		self.lb1 = tk.Listbox(self,width=140, height=20)
		self.lb1.grid(row=0, column=0)
		self.yscroll = tk.Scrollbar(command=self.lb1.yview, orient=tk.VERTICAL)
		self.yscroll.grid(row=0, column=1,sticky=tk.N+tk.S)
		self.lb1.configure(yscrollcommand=self.yscroll.set)
		for i in range(3):
			self.lb1.insert(i,sdm.print_all("gui")[1])

		'''
		self.lbcont= tk.Listbox(self.frame)
		self.lbcont.insert(1,"John Doe")
		self.lbcont.pack(side=tk.TOP, fill=tk.BOTH,expand=1)

		self.canvas.pack(side=tk.TOP, fill=tk.BOTH,expand=1)
		self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
		self.canvas_frame = self.canvas.create_window((0, 0), window=self.frame, anchor="n")
		'''
		
		#shall we convert this to object-oriented as well? 
		#Anyways these lines just create the menubar
		menubar=tk.Menu(self)
		smenu=tk.Menu(menubar, tearoff=0)

		smenu.add_command(label="FirstName", command=donothing)
		smenu.add_command(label="LastName", command=donothing)
		smenu.add_command(label="RowID", command=donothing)

		smenu.add_separator()

		smenu.add_command(label="Exit", command=self.quit)
		menubar.add_cascade(label="Search", menu=smenu)
		fmenu = tk.Menu(menubar, tearoff=0)
		fmenu.add_command(label="Add", command=donothing)
		fmenu.add_command(label="Delete", command=donothing)
		fmenu.add_command(label="Edit", command=donothing)
		fmenu.add_command(label="Print", command=donothing)
		fmenu.add_command(label="Averages", command=avgPrint)

		menubar.add_cascade(label="Entry", menu=fmenu)
		self.config(menu=menubar)
		#until this
		'''
		#This handles the crossplatform mouse scrolling, bc apparantely different OSs handle it differently
		self.bind_all("<MouseWheel>", self.mouse_scroll)
		self.bind_all("<Button-4>", self.mouse_scroll)
		self.bind_all("<Button-5>", self.mouse_scroll)
        '''
	



if __name__ == "__main__":
	window = Window()
	window.mainloop()
