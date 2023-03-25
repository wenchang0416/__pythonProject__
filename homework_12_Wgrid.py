'''
這是專案
'''
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')                         #print(ttStyle.theme_names())
        ttkStyle.configure('yellow.TFrame',background="yellow")                 #一要有.TFrame,red可自改
        ttkStyle.configure('gdLabel.TLabel',font=('Helvetica','16'),foreground="#666666")
        ttkStyle.configure('gdEntry.TEntry',font=('Helvetica','16'))

        mainFrame=ttk.Frame(self)
        mainFrame.pack(expand=True,fill=tk.BOTH,padx=30,pady=30)  
        
        topFrame=ttk.Frame(mainFrame,height=100)
        topFrame.pack(fill=tk.X)          
        ttk.Label(topFrame,text="BMI試算",font=('Helvetica','20')).pack(pady=20)

        #self.bottomFrame=ttk.Frame(mainFrame,style='yellow.TFrame')
        self.bottomFrame=ttk.Frame(mainFrame)
        self.bottomFrame.pack(expand=True,fill=tk.BOTH)
        self.bottomFrame.columnconfigure(0,weight=3,pad=20)
        self.bottomFrame.columnconfigure(1,weight=5,pad=20)
        self.bottomFrame.rowconfigure(0,weight=1,pad=20)
        self.bottomFrame.rowconfigure(3,weight=1,pad=20)
        self.bottomFrame.rowconfigure(4,weight=1,pad=20)
        self.bottomFrame.rowconfigure(5,weight=1,pad=20)
        self.bottomFrame.rowconfigure(6,weight=1,pad=20)

        ttk.Label(self.bottomFrame,text="姓名:",style='gdLabel.TLabel').grid(row=0,column=0,sticky=tk.E)
        self.nameEntry=ttk.Entry(self.bottomFrame,style='gdEntry.TEntry')
        self.nameEntry.grid(row=0,column=1,sticky=tk.W,padx=10)

        ttk.Label(self.bottomFrame,text="出生年月日:",style='gdLabel.TLabel').grid(row=1,column=0,sticky=tk.E)
        ttk.Label(self.bottomFrame,text="(2000/03/01)",style='gdLabel.TLabel').grid(row=2,column=0,sticky=tk.E)
        birthEntry=ttk.Entry(self.bottomFrame,style='gdEntry.TEntry')
        birthEntry.grid(row=1,column=1,sticky=tk.W,rowspan=2,padx=10)

        ttk.Label(self.bottomFrame,text="身高(cm):",style='gdLabel.TLabel').grid(row=3,column=0,sticky=tk.E)        
        self.heightVar = tk.StringVar()
        self.heightEntry=ttk.Entry(self.bottomFrame,textvariable=self.heightVar,style="gdEntry.TEntry")
        self.heightEntry.grid(row=3,column=1,sticky=tk.W,padx=10)

        ttk.Label(self.bottomFrame,text="體重(kg):",style='gdLabel.TLabel').grid(row=4,column=0,sticky=tk.E)             
        self.weightVar = tk.StringVar()
        self.weightEntry=ttk.Entry(self.bottomFrame,textvariable=self.weightVar,style="gdEntry.TEntry")
        self.weightEntry.grid(row=4,column=1,sticky=tk.W,padx=10)

        self.messageText=tk.Text(self.bottomFrame,height=5,width=38,state=tk.DISABLED)       
        self.messageText.grid(row=5,column=0,sticky=tk.N+tk.S,columnspan=2)

        comitButton=ttk.Button(self.bottomFrame,text="計算",command=self.Data_click)
        comitButton.grid(row=6,column=1,sticky=tk.W)
    
    
    def Bmi(self,height,weight):
        bmi=float(weight)/(float(height)/100)**2
        if   bmi<18.5:
            message="體重過輕"
        elif bmi<24:
            message="正常範圍"
        elif bmi<27:
            message="異常範圍 : 過重"
        elif bmi<30:
            message="異常範圍 : 輕度肥胖"
        elif bmi<35:
            message="異常範圍 : 中度肥胖"
        else:
            message="異常範圍 : 重度肥胖"

        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete('1.0', tk.END)
        self.messageText.insert("insert",f"BMI:{bmi: .5f}, {message}") 
        self.messageText.configure(state=tk.DISABLED)  

    def Data_wrong(self,height,weight):
        self.messageText.configure(state=tk.NORMAL)                  
        self.messageText.delete('1.0', tk.END)
        if not height.isdigit():
            self.messageText.insert("insert",f"身高:'{height}', 輸入錯誤\n")   
            self.heightVar.set('')
        if not weight.isdigit():
            self.messageText.insert("insert",f"體重:'{weight}', 輸入錯誤\n") 
            self.weightVar.set('')        
        self.messageText.configure(state=tk.DISABLED)  

    def Data_click(self): 
        if self.heightVar.get().isdigit() and self.weightVar.get().isdigit():
            self.Bmi( self.heightVar.get(), self.weightVar.get() ) 
        else:
            self.Data_wrong( self.heightVar.get(), self.weightVar.get() )  





def main():
    window = Window()
    window.title("BMI計算")
    #window.geometry("400x500")
    window.mainloop()


if __name__=='__main__':
    main()