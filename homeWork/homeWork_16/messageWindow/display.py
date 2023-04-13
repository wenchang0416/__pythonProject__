import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import tkintermapview as tkmap     #pip install tkintermapview



class MapDisplay(Dialog):
    def __init__(self,master,data_dict,**kwargs):
        self.site_info = data_dict                      #一定要在super().__init__(master,**kwargs)
        super().__init__(master,**kwargs)


    #override
    def body(self, master):    
        #以下順序不能變
        map_widget = tkmap.TkinterMapView(self,width=800,height=600,corner_radius=0)
        map_widget.pack()
        marker_1 = map_widget.set_position(self.site_info['lat'], self.site_info['lng'],marker=True) #台北市位置        
        map_widget.set_zoom(20)    #設定顯示大小
        marker_1.set_text(self.site_info['sna'])        


    #override: button'ok','cancel'不見
    def buttonbox(self) -> None:    
        '''add standard button box
           override if you do not want the standard button
        '''
        boxFrame = ttk.Frame(self)
        button = ttk.Button(boxFrame,text='關閉',width=10,command=self.ok,default=tk.ACTIVE)  #self.ok方法是繼承來的
        button.pack(side=tk.LEFT,padx=5,pady=5)
        self.bind('<Return>',self.ok)
        boxFrame.pack()
 