import datasource
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        topFrame = ttk.LabelFrame(self,text='台北市行政區')
        length = len(datasource.sarea_list)
        self.RadiobuttonVar = tk.StringVar()
        for i in range(length):
            cols = i % 3
            rows = i// 3
            ttk.Radiobutton(topFrame,text=datasource.sarea_list[i],value=datasource.sarea_list[i],variable=self.RadiobuttonVar,command=self.radioEvent).grid(row=rows,column=cols,sticky=tk.W,padx=10,pady=6)
        topFrame.pack()

        self.RadiobuttonVar.set('中山區')
        self.area_data = datasource.getInfoDataFromArea('中山區')
        bottomFrame = ttk.LabelFrame(self,text='各區站點資訊')
        bottomFrame.pack()
        # build ttk.Treeview
        columns = ('#1', '#2', '#3', '#5', '#6', '#7', '#8')
        tree = ttk.Treeview(bottomFrame, columns=columns, show='headings')
        # define headings
        tree.heading('#1', text='站點')
        tree.column('#1', minwidth=0, width=200)
        tree.heading('#2', text='時間')
        tree.column('#2', minwidth=0, width=150)
        tree.heading('#3', text='總車數')
        tree.column('#3', minwidth=0, width=75)
        tree.heading('#4', text='可借')
        tree.column('#4', minwidth=0, width=50)
        tree.heading('#5', text='可還')
        tree.column('#5', minwidth=0, width=50)
        tree.heading('#6', text='地址')
        tree.column('#6', minwidth=0, width=200)
        tree.heading('#7', text='狀態')
        tree.column('#7', minwidth=0, width=50)
        tree.pack()
        for item in self.area_data:
            tree.insert('', tk.END, values=[item['sna'],item['mday'],item['tot'],item['sbi'],item['bemp'],item['ar'],item['act']])

    def radioEvent(self):
        area_name = self.RadiobuttonVar.get()
        area_data = datasource.getInfoDataFromArea(area_name)
        #print(area_data)

def main():
    #print(datasource.sarea_list)
    window = Window()
    window.title("台北市YouBike2.0資訊")
    window.mainloop()


if __name__=="__main__":
    main()

