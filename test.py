# from tkinter import *
# from tkinter import ttk
#
# class AutoExpenseSplitter(Frame):
#     def __init__(self, parent):
#         super(AutoExpenseSplitter, self).__init__(parent)  # Fixed super() call
#
#         #labels
#         title = Label(self, text='Auto Expense Splitter')
#         totalPriceLabel = Label(self, text='Total Price Amount')
#
#         #text fields
#         totalPriceEntry = Entry(self)
#
#         #grid based packing setup
#         self.columnconfigure(0, weight=1)
#         self.columnconfigure(1, weight=1)
#
#         #pack based packing setup
#         self.pack(pady=10, fill=BOTH, expand=True)
#
#         title.pack(pady=5)
#         totalPriceLabel.pack(pady=5)
#         totalPriceEntry.pack(pady=5)  # Added to show the entry
#
# class MainPage(Frame):  # Added Frame inheritance
#     def __init__(self, master):
#         super(MainPage, self).__init__(master)  # Added proper super() call
#
#         #content frame
#         mainFrame = ttk.Frame(self)  # Changed to self
#
#         #the switching of frames
#         self.index = 0 #this is the default page
#         self.mainFrame = mainFrame  # Store reference
#         self.frameList = [self, AutoExpenseSplitter(mainFrame)]  # Fixed recursion: use self for index 0
#         self.frameList[self.index].pack(fill=BOTH, expand=True)  # Show default frame
#         self.frameList[1].pack_forget()  # Fixed: use pack_forget() instead of forget()
#
#         #labels
#         title = Label(mainFrame, text="(title here)")
#         functionLabel = Label(mainFrame, text="Functions")
#         trackerLabel = Label(mainFrame, text="Trackers")
#
#         #button
#         autoExpenseSplitterButton = Button(mainFrame, text="Auto Expense Splitter", command=self.splitterFunction)
#         #expenseTrackerButton = Button(mainFrame, text="Expense Tracker", command=self.expenseTrackerFunction)
#
#         #grid based packing
#         mainFrame.columnconfigure(0, weight=1)
#         mainFrame.columnconfigure(1, weight=1)
#
#         #pack based packing
#         mainFrame.pack(pady=10, fill=BOTH, expand=True)
#
#         title.pack()
#         autoExpenseSplitterButton.pack()
#         #expenseTrackerButton.pack()  # Added to show button
#         functionLabel.pack()  # Added to show label
#         trackerLabel.pack()  # Added to show label
#
#     def splitterFunction(self):
#         self.frameList[self.index].pack_forget()  # Hide current
#         self.index = 1
#         self.frameList[self.index].tkraise() # Show new (in mainFrame)
#         self.frameList[self.index].pack(fill=BOTH, expand=True)  # Show new (in mainFrame)
#
# root = Tk() #root of the GUI
# app = MainPage(root)  # Fixed: Create and add MainPage instance to root
# root.title('(title here)')
# root.mainloop() #keeps the windows open and responsive

import datetime
var1 = 1
var2 = 2
var3 = 3
entryVars = [var1, var2, var3]
currentTime = datetime.datetime.now().strftime('%x')
print(str(entryVars[0]) + "_" + currentTime)