import datasource
import datetime
import tkinter as tk
from tkinter    import ttk
from tkinter.simpledialog   import askinteger,askstring
from PIL import Image,ImageTk
from messageWindow import MapDisplay



sbi_numbers = 3
bemp_numbers = 3

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        #add menubar that contains a menu---------------------------
        
        self.menubar = tk.Menu(self)
        self.configure(menu = self.menubar)
        # add command menu in menubar
        self.command_menu = tk.Menu(self.menubar,tearoff=0)
        self.command_menu.add_command(label='設定',command=self.menu_setting_click)   
        self.command_menu.add_command(label="離開",command=self.destroy)
        self.menubar.add_cascade(label='File',menu=self.command_menu)

        self.command02_menu = tk.Menu(self.menubar,tearoff=0)
        self.command02_menu.add_command(label='查詢',command=self.menu_search_click)
        self.menubar.add_cascade(label='查詢',menu=self.command02_menu)
        
        # Mainframe:------------------------------------------------
        mainFrame = ttk.Frame(self)
        mainFrame.pack(padx=30,pady=(10,20))

        # Logoframe:------------------------------------------------        
        logoImage = Image.open('./images/bgMountain_1.jpg')
        logoImgaeNew = logoImage.resize((950,100))
        self.logoPhoto = ImageTk.PhotoImage(logoImgaeNew)
        logoLabel = ttk.Label(mainFrame,image=self.logoPhoto)
        logoLabel.pack(pady=10)
        

        # top_wrapperframe:-----------------------------------------
        top_wrapperframe = ttk.Frame(mainFrame)
        top_wrapperframe.pack(fill=tk.X)
        # topFrame:-------------------------------------------------
        topFrame = ttk.LabelFrame(top_wrapperframe,text='台北市行政區')
        length = len(datasource.sarea_list)
        self.RadiobuttonVar = tk.StringVar()
        for i in range(length):
            cols = i % 3
            rows = i// 3
            ttk.Radiobutton(topFrame,text=datasource.sarea_list[i],value=datasource.sarea_list[i],variable=self.RadiobuttonVar,command=self.radioEvent).grid(row=rows,column=cols,sticky=tk.W,padx=10,pady=10) 
        
        topFrame.pack(side=tk.LEFT)
        #topFrame.pack(side=tk.TOP, anchor='nw')
        self.RadiobuttonVar.set('信義區')
        self.area_data = datasource.getInfoDataFromArea('信義區')
        
        # sbi_warningFrame--------------------------------------
        self.sbi_warningFrame = ttk.LabelFrame(top_wrapperframe)
        columns = ('#1', '#2', '#3')
        self.sbi_tree = ttk.Treeview(self.sbi_warningFrame, columns=columns, show='headings')
        ## define headings
        self.sbi_tree.heading('#1', text='站點')
        self.sbi_tree.column('#1', minwidth=0, width=200)
        self.sbi_tree.heading('#2', text='可借')
        self.sbi_tree.column('#2', minwidth=0, width=40)
        self.sbi_tree.heading('#3', text='可還')
        self.sbi_tree.column('#3', minwidth=0, width=40)
        self.sbi_tree.pack(side=tk.LEFT)

        self.sbi_warning_data = datasource.filter_sbi_warning_data(self.area_data,sbi_numbers)  
        self.sbi_sites_numbers = len(self.sbi_warning_data)
        self.sbi_warningFrame.configure(text=f"可借不足站點數:{self.sbi_sites_numbers}")
        for item in self.sbi_warning_data: 
            self.sbi_tree.insert('', tk.END, values=[item['sna'][11:],item['sbi'],item['bemp']]) 

        self.sbi_warningFrame.pack(side=tk.LEFT,padx=20)  


        # bemp_warningFrame--------------------------------------
        self.bemp_warningFrame = ttk.LabelFrame(top_wrapperframe)
        columns = ('#1', '#2', '#3')
        self.bemp_tree = ttk.Treeview(self.bemp_warningFrame, columns=columns, show='headings')
        ## define headings
        self.bemp_tree.heading('#1', text='站點')
        self.bemp_tree.column('#1', minwidth=0, width=200)
        self.bemp_tree.heading('#2', text='可借')
        self.bemp_tree.column('#2', minwidth=0, width=40)
        self.bemp_tree.heading('#3', text='可還')
        self.bemp_tree.column('#3', minwidth=0, width=40)
        self.bemp_tree.pack(side=tk.LEFT)

        self.bemp_warning_data = datasource.filter_bemp_warning_data(self.area_data,bemp_numbers)  
        self.bemp_sites_numbers = len(self.bemp_warning_data)        
        self.bemp_warningFrame.configure(text=f"可還不足站點數:{self.bemp_sites_numbers}")
        for item in self.bemp_warning_data:
            self.bemp_tree.insert('', tk.END, values=[item['sna'][11:],item['sbi'],item['bemp']]) 
            
        self.bemp_warningFrame.pack(side=tk.LEFT)
        
        # bottomFrame-------------------------------------------
        now =datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")

        self.bottomFrame = ttk.LabelFrame(mainFrame,text=f'信義區-{nowString}')
        self.bottomFrame.pack()
        # ttk.Treeview
        columns = ('#1', '#2', '#3', '#5', '#6', '#7', '#8')
        self.tree = ttk.Treeview(self.bottomFrame, columns=columns, show='headings')
        ## define headings
        self.tree.heading('#1', text='站點')
        self.tree.column('#1', minwidth=0, width=200)
        self.tree.heading('#2', text='時間')
        self.tree.column('#2', minwidth=0, width=200)
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
        self.tree.pack(side=tk.LEFT)

        for item in self.area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:],item['mday'],item['tot'],item['sbi'],item['bemp'],item['ar'],item['act']],tags=item['sna'])           #加入tags:指向'sna'

        #self.tree bind event
        self.tree.bind('<<TreeviewSelect>>',self.treeSelected)          #資料點選時,觸動event

        #幫treeview加scrollbar------------------------------------------------
        scrollBarY = ttk.Scrollbar(self.bottomFrame,orient='vertical',command=self.tree.yview)
        scrollBarY.pack(side=tk.RIGHT,fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollBarY.set)

        sbi_scrollBarY = ttk.Scrollbar(self.sbi_warningFrame,orient='vertical',command=self.sbi_tree.yview)
        sbi_scrollBarY.pack(side=tk.RIGHT,fill=tk.Y)
        self.sbi_tree.configure(yscrollcommand=sbi_scrollBarY.set)

        bemp_scrollBarY = ttk.Scrollbar(self.bemp_warningFrame,orient='vertical',command=self.bemp_tree.yview)
        bemp_scrollBarY.pack(side=tk.RIGHT,fill=tk.Y)
        self.bemp_tree.configure(yscrollcommand=bemp_scrollBarY.set)


    def treeSelected(self,event):
        selectedTree = event.widget  
        if len(selectedTree.selection()) ==0: return       #正常selectedTree出現tuple('I001',),但有時會0
        itemTage = selectedTree.selection()[0]
        itemDic = selectedTree.item(itemTage)
        siteName = itemDic['tags'][0]   
        for item in self.area_data:
            if siteName == item['sna']:
                select_Data = item
                break  
        #顯示地圖
        mapDisplay = MapDisplay(self,select_Data)


    def menu_setting_click(self):
        global sbi_numbers,bemp_numbers
        retVal = askinteger(f"目前設定不足數量:{sbi_numbers}",
                             "請輸入不足可借/可還的數量0~5",
                             minvalue=0,maxvalue=5)
        sbi_numbers = retVal
        bemp_numbers = retVal  


    def menu_search_click(self):
        siteStr = askstring("查詢的站點名",
                            "請輸入欲查詢的站點名")
        for item in self.tree.get_children():
            self.tree.delete(item)  
        for item in self.area_data:
            if siteStr in item['sna'] or siteStr in item['ar']:
                self.tree.insert('', tk.END, values=[item['sna'][11:],item['mday'],item['tot'],item['sbi'],item['bemp'],item['ar'],item['act']],tags=item['sna'])
        
             
        for item in self.sbi_tree.get_children():
            self.sbi_tree.delete(item)
        sbi_sites_numbers = 0
        for item in self.sbi_warning_data: 
            if siteStr in item['sna']:
                self.sbi_tree.insert('', tk.END, values=[item['sna'][11:],item['sbi'],item['bemp']]) 
                sbi_sites_numbers += 1
        self.sbi_warningFrame.configure(text=f"可借不足站點數:{sbi_sites_numbers}")


    def radioEvent(self):
         #get current datetime
        now =datetime.datetime.now()
         #display current datetime
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")   
        # Clear tree view
        for item in self.tree.get_children():
            self.tree.delete(item)        
        for item in self.sbi_tree.get_children():
            self.sbi_tree.delete(item)
        for item in self.bemp_tree.get_children():
            self.bemp_tree.delete(item)

        # Get selected radio button value
        area_name = self.RadiobuttonVar.get()
   
        self.bottomFrame.configure(text=f'{area_name}-{nowString}')

        # Get all station data from selected area
        self.area_data = datasource.getInfoDataFromArea(area_name) 
        # Filter data with sbi warning number
        sbi_warning_data = datasource.filter_sbi_warning_data(self.area_data,sbi_numbers)  
        self.sbi_sites_numbers = len(sbi_warning_data)
        self.sbi_warningFrame.configure(text=f"可借不足站點數:{self.sbi_sites_numbers}")
        # Filter data with bemp warning number
        bemp_warning_data = datasource.filter_bemp_warning_data(self.area_data,bemp_numbers) 
        self.bemp_sites_numbers = len(bemp_warning_data)
        self.bemp_warningFrame.configure(text=f"可還不足站點數:{self.bemp_sites_numbers}")

        # Display data in tree view
        for item in self.area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:],item['mday'],item['tot'],item['sbi'],item['bemp'],item['ar'],item['act']],tags=item['sna'])
        for item in sbi_warning_data:
            self.sbi_tree.insert('', tk.END, values=[item['sna'][11:],item['sbi'],item['bemp']])        
        for item in bemp_warning_data:
            self.bemp_tree.insert('', tk.END, values=[item['sna'][11:],item['sbi'],item['bemp']])



def main():
    #print(datasource.sarea_list)
    window = Window()
    window.title("台北市YouBike2.0資訊")
    window.mainloop()


if __name__=="__main__":
    main()