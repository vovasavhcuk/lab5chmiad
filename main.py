from tkinter import *

from Actor import Actor


class FirstWindow:

    def __init__(self, master):
        master.title('lab5')
        master.geometry('300x100')

        frame = Frame(master)
        frame.pack(fill=X)

        self.addButton = Button(frame, text = 'Add an Actor', command=self.open_window)
        self.addButton.pack(fill = BOTH)
        self.quitButton = Button(frame, text = 'Quit', command=frame.quit)
        self.quitButton.pack(fill = BOTH)

    @staticmethod
    def open_window():
        root1.destroy()
        root2 = Tk()
        SecondWindow(root2)
        root1.mainloop()


class SecondWindow(FirstWindow):
    actorList = []


    def __init__(self, master):
        master.protocol('WM_DELETE_WINDOW', self.close)
        var1 = StringVar()

        frame_top = Frame(master)
        frame_top.pack()
        frame1 = Frame(master)
        frame1.pack(side=TOP, fill=BOTH)

        self.label = Label(frame_top, text='Actor\'s name')
        self.label.grid(row=0, column=0, sticky=E)
        self.label1 = Label(frame_top, text='Actor\'s salary')
        self.label1.grid(row=1, column=0, sticky=E)
        self.label2 = Label(frame_top, text='Actor\'s role')
        self.label2.grid(row=2, column=0, sticky=E)
        self.label3 = Label(frame_top, text='Actor\'s film')
        self.label3.grid(row=3, column=0, sticky=E)

        self.txt = Entry(frame_top)
        self.txt.grid(row=0, column=1)
        self.txt1 = Entry(frame_top)
        self.txt1.grid(row=1, column=1)
        self.txt2 = Entry(frame_top)
        self.txt2.grid(row=2, column=1)
        self.txt3 = Entry(frame_top)
        self.txt3.grid(row=3, column=1)

        self.btn1 = Button(frame1, text='ok', command=self.write_to_file)
        self.btn1.pack(fill=X)
        self.showBtn = Button(frame1, text='Show list', command=self.show_btn_click)
        self.showBtn.pack(fill=X)
        self.clearBtn = Button(frame1, text='Clear list', command=self.clear_list)
        self.clearBtn.pack(fill=X)
        self.delBtn = Button(frame1, text='delete last line', command=self.delete_last)
        self.delBtn.pack(fill=X)
        self.closeBtn = Button(frame1, text='Close', command=self.close)
        self.closeBtn.pack(fill=X)

        self.R1 = Radiobutton(master, text="By name", variable=var1, value='1', command=self.sort_by_name)
        self.R1.pack(fill=X)
        self.R2 = Radiobutton(master, text="By salary", variable=var1, value='2', command=self.sort_by_salary)
        self.R2.pack(fill=X)
        self.R3 = Radiobutton(master, text="By role", variable=var1, value='3', command=self.sort_by_role)
        self.R3.pack(fill=X)
        self.R4 = Radiobutton(master, text="By film", variable=var1, value='4', command=self.sort_by_film)
        self.R4.pack(fill=X)
        self.quickButton = Button(master, text='sort', command=self.sort)
        self.quickButton.pack(fill = X)

    def compareByName(self, inputStr):
        return inputStr[0]

    def compareBySalary(self, inputStr):
        return inputStr[1]

    def compareByRole(self, inputStr):
        return inputStr[2]

    def compareByFilm(self, inputStr):
        return inputStr[3]

    def sort_by_name(self):
        self.actorList.sort(key=self.compareByName)

    def sort_by_salary(self):
        self.actorList.sort(key=self.compareBySalary)

    def sort_by_role(self):
        self.actorList.sort(key=self.compareByRole)

    def sort_by_film(self):
        self.actorList.sort(key=self.compareByFilm)

    def sort(self):

        if self.R1.select():
            self.sort_by_name()
        elif self.R2.select():
            self.sort_by_salary()
        elif self.R3.select():
            self.sort_by_role()
        elif self.R4.select():
            self.sort_by_film()

    def write_to_file(self):
        actor = Actor(self.txt.get(), self.txt1.get(), self.txt2.get(), self.txt3.get())
        self.actorList.append(actor.copy())
        file = open("./data.cvs", "a")
        file.write(f"""
            Name {self.txt.get()} 
            salary {self.txt1.get()} 
            role {self.txt2.get()} 
            film {self.txt3.get()}
            """)
        file.close()

    @staticmethod
    def delete_last(self):
        file = open("./data.cvs", 'rb')
        pos = next = 0
        for line in file:
            pos = next  # position of beginning of this line
            next += len(line)  # compute position of beginning of next line
        file = open("./data.cvs", 'ab')
        file.truncate(pos)
        self.actorList.pop()

    def clear_list(self):
        self.actorList.clear()
        file = open("./data.cvs", "r+")
        file.truncate(0)

    def show_btn_click(self):
        for x in self.actorList:
            print(f"""
            Name {x[0]} 
            salary {x[1]} 
            role {x[2]} 
            film {x[3]}
            """)

    @staticmethod
    def close():
        root1.quit()


if __name__ == '__main__':
    root1 = Tk()
    root1['bg'] = '#0319FC'
    root1.title('my son is gay')
    root1.geometry('300x200')
    a = FirstWindow(root1)
    root1.mainloop()


