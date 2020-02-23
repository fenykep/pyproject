import StudentDatabaseManager as sdm
import tkinter as tk


def edit():
	print(sdm.tryThis())
	#tkMessageBox.showinfo("Beep Boop", sdm.tryThis())

def donothing():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()
	
window=tk.Tk()

window.title("Student Database Manager® 2020")
window.geometry('800x600')
menubar=tk.Menu(window)
smenu=tk.Menu(menubar, tearoff=0)

smenu.add_command(label="FirstName", command=donothing)
smenu.add_command(label="LastName", command=donothing)
smenu.add_command(label="RowID", command=donothing)

smenu.add_separator()

smenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Search", menu=smenu)
fmenu = tk.Menu(menubar, tearoff=0)
fmenu.add_command(label="Add", command=donothing)
fmenu.add_command(label="Delete", command=donothing)
fmenu.add_command(label="Edit", command=donothing)
fmenu.add_command(label="Print", command=donothing)
fmenu.add_command(label="Averages", command=donothing)

menubar.add_cascade(label="Entry", menu=fmenu)
window.config(menu=menubar)

window.mainloop()

