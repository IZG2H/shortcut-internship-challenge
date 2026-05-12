from tkinter import *
from tkinter import ttk
import datetime
import databaseConfigure as dbc

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

        #grid configuring for top and middle frame
        topframe.columnconfigure(0, weight=1)
        topframe.columnconfigure(1, weight=1)
        topframe.columnconfigure(2, weight=1) #this is to center column 1 only
        middleframe.columnconfigure(0, weight=1)
        middleframe.columnconfigure(1, weight=1)

        #labels
        titleLabel = Label(topframe, text='Automatic Expense Splitter')
        trackerNameLabel = Label(middleframe, text='Tracker Name: ')
        priceEntryLabel = Label(middleframe, text='Total Bills/Price Amount (in numbers): ')
        firstPersonLabel = Label(middleframe, text='First Person: ')
        secondPersonLabel = Label(middleframe, text='Second Person: ')
        thirdPersonLabel = Label(middleframe, text='Third Person: ')

        #buttons
        backButton = Button(topframe, text='Back', command=lambda : self.controller.frameChange(0))
        splitBillsButton = Button(bottomframe, text='Split Da Bills', command=lambda : self.splitBillsFunction(entryVars, self.controller))

        #entries
        trackerNameEntry = Entry(middleframe)
        totalPriceEntry = Entry(middleframe)
        firstPersonEntry = Entry(middleframe)
        secondPersonEntry = Entry(middleframe)
        thirdPersonEntry = Entry(middleframe)
        entryVars = EntryVars(trackerNameEntry, totalPriceEntry, firstPersonEntry, secondPersonEntry, thirdPersonEntry)

        #packing order
        backButton.grid(row=0, column=0, sticky="w")
        titleLabel.grid(row=0, column=1, sticky='s')

        trackerNameLabel.grid(row=0, column=0, sticky='e', padx=5)
        trackerNameEntry.grid(row=0, column=1, sticky='w', padx=5, pady=10)

        priceEntryLabel.grid(row=2, column=0, sticky='e', padx=5)
        totalPriceEntry.grid(row=2, column=1, sticky='w', padx=5, pady=10)

        firstPersonLabel.grid(row=3, column=0, sticky='e', padx=5)
        firstPersonEntry.grid(row=3, column=1, sticky='w', padx=5)

        secondPersonLabel.grid(row=4, column=0, sticky='e', padx=5)
        secondPersonEntry.grid(row=4, column=1, sticky='w', padx=5)

        thirdPersonLabel.grid(row=5, column=0, sticky='e', padx=5)
        thirdPersonEntry.grid(row=5, column=1, sticky='w', padx=5)
        splitBillsButton.pack(pady=20)

    @staticmethod
    def splitBillsFunction(entryVars, controller):
        entry = [entryVars.firstPersonEntry.get(), entryVars.secondPersonEntry.get(), entryVars.thirdPersonEntry.get()] #the names filled in

        #for the title
        trackerName = entryVars.trackerNameEntry
        currentTime = datetime.datetime.now().strftime('%x')

        #title creation
        name = trackerName.get() + "_" + currentTime

        #to check the amount of ppl and divide the total amount of the bills
        personCounter = len(entry)
        singlePersonPayment = int(entryVars.totalPriceEntry.get()) / personCounter

        #slot data in a nested array. format for each array is [(person name), (amount need to pay), (how much they paid(this one is zero by default))] (follow database table)
        data = []
        for personName in entry:
            if personName is None:
                break
            else:
                data.append([personName, str(singlePersonPayment), '0'])

        dbc.databaseConfigure(name, data)
        controller.frameChange(2) #to switch to tracker page

class EntryVars: #just for variable storage, no important functions here
    def __init__(self, trackerNameEntry, totalPriceEntry, firstPersonEntry, secondPersonEntry, thirdPersonEntry):
        self.trackerNameEntry = trackerNameEntry
        self.totalPriceEntry = totalPriceEntry
        self.firstPersonEntry = firstPersonEntry
        self.secondPersonEntry = secondPersonEntry
        self.thirdPersonEntry = thirdPersonEntry

class ExpensesTrackerFrame(Frame):
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

        #grid configuring for top and middle frame
        topframe.columnconfigure(0, weight=1)
        topframe.columnconfigure(1, weight=1)
        topframe.columnconfigure(2, weight=1) #this is to center column 1 only
        middleframe.columnconfigure(0, weight=1)
        middleframe.columnconfigure(1, weight=1)

        #labels
        testLabel = Label(self, text='test 2') #testing purpose (need to change later)

        #buttons
        Button(self, text='Back to Main', command=lambda : self.controller.frameChange(0)).pack() #testing purposes (need to change later)

        #entries

        #packing order
        testLabel.pack(padx=10)

class MainFrame(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        #frame sectioning
        topframe = Frame(self)
        middleframe = Frame(self)
        bottomframe = Frame(self)

        #frame packing
        topframe.pack(fill=BOTH, expand=True)
        middleframe.pack(fill=BOTH, expand=True)
        bottomframe.pack(padx=10, pady=10)

        #grid configuring for middle frame
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

root = Tk()
root.title('Expense Splitting')
centerWindow(root, 500, 400)
app = FrameChanging(root)
root.mainloop()