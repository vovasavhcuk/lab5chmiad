# from tkinter import *
# from FirstWindow import FirstWindow

# class SecondWindow(FirstWindow):
#     array = []
#
#     def __init__(self,master):
#         master.protocol('WM_DELETE_WINDOW', self.close)
#         var1 = StringVar()
#
#         frame_top = Frame(master)
#         frame_top.pack()
#         frame1 = Frame(master)
#         frame1.pack(side = TOP, fill = BOTH)
#
#         self.label = Label(frame_top, text = 'Actor\'s name')
#         self.label.grid(row = 0, coolumn = 0, sticy = E)
#         self.label1 = Label(frame_top, text = 'Actor\'s salary')
#         self.label1.grid(row = 1, column = 0, sticy = E )
#         self.label2 = Label(frame_top, text='Actor\'s role')
#         self.label2.grid(row=2, column=0, sticy=E)
#         self.label3 = Label(frame_top, text='Actor\'s film')
#         self.label3.grid(row=3, column=0, sticy=E)
#
#         self.txt = Entry(frame_top)
#         self.txt.grid(row = 0, column = 1)
#         self.txt1 = Entry(frame_top)
#         self.txt1.grid(row=1, column=1)
#         self.txt2 = Entry(frame_top)
#         self.txt2.grid(row=2, column=1)
#         self.txt3 = Entry(frame_top)
#         self.txt3.grid(row=3, column=1)
#
#         self.btn1 = Button(frame1, text='ok', command = self.write_to_file)
#         self.btn1.pack(fill = X)
#         self.showBtn = Button(frame1, text='Show list', command=self.show_btn_click)
#         self.showBtn.pack(fill=X)
#         self.clearBtn = Button(frame1, text='Clear list', command=self.clear_list)
#         self.clearBtn.pack(fill=X)
#         self.delBtn = Button(frame1, text='delete last object', command=self.delete_last)
#         self.delBtn.pack(fill=X)
#
#     def delete_last(self):
#         self.array.pop()
#
#     def write_to_file(self):
#         self.array.append()
#
#     def clear_list(self):
#         self.array.clear()
#
#     def show_btn_click(self):
#         i = 0
#         for x in self.array:
#             print(x[i])
#             i += 1
#
#     def close(self):
#         root1.quit()


