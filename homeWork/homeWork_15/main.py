import datasource
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        topFrame = ttk.LabelFrame(self,text='台北市行政區')
        topFrame.pack()
        length = len(datasource.sarea_list)
        self.RadiobuttonVar = tk.StringVar()
        for i in range(length):
            cols = i % 4
            rows = i// 4
            ttk.Radiobutton(topFrame,text=datasource.sarea_list[i],value=datasource.sarea_list[i],variable=self.RadiobuttonVar,command=self.radioEvent).grid(row=rows,column=cols,sticky=tk.W,padx=10,pady=6) 
        self.RadiobuttonVar.set('信義區')
        self.area_data = datasource.getInfoDataFromArea('信義區')

        # build bottomFrame-------------------------------------------
        bottomFrame = ttk.LabelFrame(self,text='各區站點資訊',width=500)
        bottomFrame.pack()
        # build ttk.Treeview
        columns = ('#1', '#2', '#3', '#5', '#6', '#7', '#8')
        self.tree = ttk.Treeview(bottomFrame, columns=columns, show='headings')
        ## define headings
        self.tree.heading('#1', text='站點')
        self.tree.column('#1', minwidth=0, width=240)
        self.tree.heading('#2', text='時間')
        self.tree.column('#2', minwidth=0, width=140)
        self.tree.heading('#3', text='總車數')
        self.tree.column('#3', minwidth=0, width=50)
        self.tree.heading('#4', text='可借')
        self.tree.column('#4', minwidth=0, width=40)
        self.tree.heading('#5', text='可還')
        self.tree.column('#5', minwidth=0, width=40)
        self.tree.heading('#6', text='地址')
        self.tree.column('#6', minwidth=0, width=330)
        self.tree.heading('#7', text='狀態')
        self.tree.column('#7', minwidth=0, width=40)
        for item in self.area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:],item['mday'],item['tot'],item['sbi'],item['bemp'],item['ar'],item['act']])
        # build scrollbar
        self.scrollBarY = ttk.Scrollbar(bottomFrame,orient='vertical',command=self.tree.yview)
        self.scrollBarY.pack(side=tk.RIGHT,fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scrollBarY.set)
        self.tree.pack()


    def radioEvent(self):
        area_name = self.RadiobuttonVar.get()
        area_data = datasource.getInfoDataFromArea(area_name)
        for item in self.tree.get_children():
            self.tree.delete(item)
        for item in area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:],item['mday'],item['tot'],item['sbi'],item['bemp'],item['ar'],item['act']])



def main():
    #print(datasource.sarea_list)
    window = Window()
    window.title("台北市YouBike2.0資訊")
    window.mainloop()


if __name__=="__main__":
    main()

