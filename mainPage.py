from tkinter import *
from tkinter import ttk
import datetime

root = Tk()
root.title('Expense Splitting')

class AutoExpensesSplitterFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        #frame sectioning
        topframe = Frame(self)
        middleframe = Frame(self)
        bottomframe = Frame(self)

        #frame packing
        topframe.pack(fill=BOTH, expand=True)
        middleframe.pack(fill=BOTH, expand=True)
        bottomframe.pack(padx=10, pady=10)

        #grid packing for top and middle frame
        topframe.columnconfigure(0, weight=1)
        topframe.columnconfigure(1, weight=1)
        topframe.columnconfigure(2, weight=1) #this is to center column 1
        middleframe.columnconfigure(0, weight=1)
        middleframe.columnconfigure(1, weight=1)

        #labels
        titleLabel = Label(topframe, text='Automatic Expense Splitter')
        trackerNameLabel = Label(middleframe, text='Tracker Name: ')
        priceEntryLabel = Label(middleframe, text='Total Amount of the Price: ')
        firstPersonLabel = Label(middleframe, text='Main Person Paying Name: ')
        secondPersonLabel = Label(middleframe, text='First Person Name: ')
        thirdPersonLabel = Label(middleframe, text='Second Person Name: ')

        #buttons
        backButton = Button(topframe, text='Back', command=self.controller.frameChange(0))
        splitBillsButton = Button(bottomframe, text='Split Da Bills', command=lambda : self.splitBillsFunction(entryVars))

        #entry
        trackerNameEntry = Entry(middleframe)
        totalPriceEntry = Entry(middleframe)
        firstPersonEntry = Entry(middleframe)
        secondPersonEntry = Entry(middleframe)
        thirdPersonEntry = Entry(middleframe)
        entryVars = [trackerNameEntry, totalPriceEntry, firstPersonEntry, secondPersonEntry, thirdPersonEntry]

        #packing order
        backButton.grid(row=0, column=0, sticky="w")
        titleLabel.grid(row=0, column=1, sticky='nw')
        trackerNameLabel.grid(row=0, column=0)
        trackerNameEntry.grid(row=0, column=1)
        splitBillsButton.pack(pady=20)

    @staticmethod
    def splitBillsFunction(entryVars):
        personCounter = 0
        entry = [entryVars[1], entryVars[2], entryVars[3]]
        currentTime = datetime.datetime.now().strftime('%x')
        name = entryVars[0].get() + "_" + currentTime
        for i in entry:
            if entry[i] is None:
                break
            else:
                personCounter += 1



class ExpensesTrackerFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        testLabel = Label(self, text='test 2') #testing purpose
        testLabel.pack(padx=10)
        self.controller = controller
        Button(self, text='Back to Main', command=self.controller.frameChange(0)).pack()

class MainFrame(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        #frame sectioning
        topframe = Frame(self)
        middleframe = Frame(self)
        bottomframe = Frame(self)

        #frame packing
        topframe.pack(padx=10, pady=5)
        middleframe.pack(fill=BOTH, expand=True)
        bottomframe.pack(padx=10, pady=10)

        #grid packing for middle frame
        middleframe.columnconfigure(0, weight=1)
        middleframe.columnconfigure(1, weight=1)

        #buttons
        autoExpensesSplitterButton = Button(middleframe, text='Automatic Expenses Splitter', command=lambda: self.controller.frameChange(1))
        expensesTrackerButton = Button(middleframe, text='Expenses Tracker', command=lambda: self.controller.frameChange(2))

        #labels
        title = Label(topframe, text='Expense Splitting')

        #packing
        autoExpensesSplitterButton.pack(padx=10, pady=10)
        expensesTrackerButton.pack(padx=10, pady=10)
        title.pack(pady=10)

class FrameChanging:
    def __init__(self, root):
        self.root = root

        self.frameList = [MainFrame(root, self), AutoExpensesSplitterFrame(root, self), ExpensesTrackerFrame(root, self)] #setup the frame list
        self.currentIndex = 0 #default frame page
        self.frameList[0].pack(expand=True, fill=BOTH)

    def frameChange(self, index):
        self.frameList[self.currentIndex].pack_forget() #make the page blank
        self.currentIndex = index
        self.frameList[self.currentIndex].pack(expand=True, fill=BOTH) #fill in the new page

#function to center the window
def centerWindow(window, width, height):
    #get screen width and height
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    #calculate position coordinates
    x = (screenWidth - width) // 2
    y = (screenHeight - height) // 3

    #set window geometry
    window.geometry(f"{width}x{height}+{x}+{y}")

centerWindow(root, 500, 400)
app = FrameChanging(root)
root.mainloop()