'''
這是專案
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from datetime import datetime
import re

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')                         #print(ttStyle.theme_names())
        ttkStyle.configure('red.TFrame',background="red")     #一要有.TFrame,red,white,yellow可以自改
        ttkStyle.configure('white.TFrame',background="white")
        ttkStyle.configure('yellow.TFrame',background="yellow")
        ttkStyle.configure('gdLabel.TLabel',font=('Helvetica','16'),foreground="#666666")
        ttkStyle.configure('gdEntry.TEntry',font=('Helvetica','16'))

        mainFrame=ttk.Frame(self)
        mainFrame.pack(expand=True,fill=tk.BOTH,padx=30,pady=30)  
        
        topFrame=ttk.Frame(mainFrame,height=100)
        topFrame.pack(fill=tk.X)          
        ttk.Label(topFrame,text="BMI試算",font=('Helvetica','20')).pack(pady=(70,20))

        #bottomFrame=ttk.Frame(mainFrame,style='yellow.TFrame')
        bottomFrame=ttk.Frame(mainFrame)
        bottomFrame.pack(expand=True,fill=tk.BOTH)
        bottomFrame.columnconfigure(0,weight=3,pad=20)
        bottomFrame.columnconfigure(1,weight=5,pad=20)
        bottomFrame.rowconfigure(0,weight=1,pad=15)
        bottomFrame.rowconfigure(3,weight=1,pad=15)
        bottomFrame.rowconfigure(4,weight=1,pad=15)
        bottomFrame.rowconfigure(5,weight=1,pad=15)
        bottomFrame.rowconfigure(6,weight=1,pad=15)
        
        #---設定變數----
        self.nameVar = tk.StringVar()        
        self.birthVar = tk.StringVar()       
        self.heightVar = tk.IntVar()      
        self.weightVar = tk.IntVar()

        ttk.Label(bottomFrame,text="姓名:",style='gdLabel.TLabel').grid(row=0,column=0,sticky=tk.E)
        nameEntry=ttk.Entry(bottomFrame,style='gdEntry.TEntry',textvariable=self.nameVar)
        nameEntry.grid(row=0,column=1,sticky=tk.W,padx=10)

        ttk.Label(bottomFrame,text="出生年月日:",style='gdLabel.TLabel').grid(row=1,column=0,sticky=tk.E)
        ttk.Label(bottomFrame,text="(2000/03/01)",style='gdLabel.TLabel').grid(row=2,column=0,sticky=tk.E)
        birthEntry=ttk.Entry(bottomFrame,style='gdEntry.TEntry',textvariable=self.birthVar)
        birthEntry.grid(row=1,column=1,sticky=tk.W,rowspan=2,padx=10)

        ttk.Label(bottomFrame,text="身高(cm):",style='gdLabel.TLabel').grid(row=3,column=0,sticky=tk.E)
        heightEntry=ttk.Entry(bottomFrame,style="gdEntry.TEntry",textvariable=self.heightVar)
        heightEntry.grid(row=3,column=1,sticky=tk.W,padx=10)

        ttk.Label(bottomFrame,text="體重(kg):",style='gdLabel.TLabel').grid(row=4,column=0,sticky=tk.E)
        weightEntry=ttk.Entry(bottomFrame,style="gdEntry.TEntry",textvariable=self.weightVar)
        weightEntry.grid(row=4,column=1,sticky=tk.W,padx=10)

        self.messageText=tk.Text(bottomFrame,height=7,width=38,state=tk.DISABLED) 
        self.messageText.grid(row=5,column=0,sticky=tk.N+tk.S,columnspan=2)

        #---------commitFrame:start--------
        commitFrame= ttk.Frame(bottomFrame)
        commitFrame.grid(row=6,column=0,columnspan=2)
        commitFrame.columnconfigure(0,pad=10)                       #方法2
        
        comitButton=ttk.Button(commitFrame,text="計算",command=self.press_commit)
        #comitButton.grid(row=0,column=0,sticky=tk.E,padx=(0,10))   #方法1:無commitFrame.columnconfigure
        comitButton.grid(row=0,column=0,sticky=tk.W)                #方法2
        clearButton=ttk.Button(commitFrame,text="清除",command=self.press_clear)
        #clearButton.grid(row=0,column=1,padx=(10,0))               #方法1    
        clearButton.grid(row=0,column=1,sticky=tk.E)                #方法2

        #---------Image:start--------
        logoImg=Image.open('./images/homework_133.jpg')
        logoImg_N=logoImg.resize((300,50),Image.LANCZOS)
        self.logoTkImg=ImageTk.PhotoImage(logoImg_N)                
        logoLabel=ttk.Label(self,image=self.logoTkImg,width=180)
        logoLabel.place(x=42,y=40)

    def press_clear(self,*args) ->None:
        self.nameVar.set("")
        self.birthVar.set("")
        self.heightVar.set(0)
        self.weightVar.set(0)
        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete('1.0',tk.END)        
        self.messageText.configure(state=tk.DISABLED)
        print("清除")  

    def Bmi_msg(self,bmi) ->None:
        if   bmi<18.5:
            bmiMsg="體重過輕"
        elif bmi<24:
            bmiMsg="正常範圍"
        elif bmi<27:
            bmiMsg="異常範圍-過重"
        elif bmi<30:
            bmiMsg="異常範圍-輕度肥胖"
        elif bmi<35:
            bmiMsg="異常範圍-中度肥胖"
        else:
            bmiMsg="異常範圍-重度肥胖"

        return bmiMsg
    
    def Age_Cst(self,birthValue):
        date_now = datetime.now()        
        date_birth = datetime.strptime(birthValue, '%Y/%m/%d')
        age=date_now.year-date_birth.year

        if   datetime(date_birth.year,3,21)<=date_birth<=datetime(date_birth.year,4,20):
            Constellation="牡羊座"   
        elif datetime(date_birth.year,4,21)<=date_birth<=datetime(date_birth.year,5,21): 
            Constellation="金牛座"
        elif datetime(date_birth.year,5,22)<=date_birth<=datetime(date_birth.year,6,21): 
            Constellation="雙子座"
        elif datetime(date_birth.year,6,22)<=date_birth<=datetime(date_birth.year,7,22): 
            Constellation="巨蟹座"
        elif datetime(date_birth.year,7,23)<=date_birth<=datetime(date_birth.year,8,22): 
            Constellation="獅子座"
        elif datetime(date_birth.year,8,23)<=date_birth<=datetime(date_birth.year,9,22): 
            Constellation="處女座"
        elif datetime(date_birth.year,9,23)<=date_birth<=datetime(date_birth.year,10,23): 
            Constellation="天秤座"
        elif datetime(date_birth.year,10,24)<=date_birth<=datetime(date_birth.year,11,22): 
            Constellation="天蠍座"
        elif datetime(date_birth.year,11,23)<=date_birth<=datetime(date_birth.year,12,21): 
            Constellation="射手座"
        elif datetime(date_birth.year,1,21)<=date_birth<=datetime(date_birth.year,2,18): 
            Constellation="水瓶座"
        elif datetime(date_birth.year,2,19)<=date_birth<=datetime(date_birth.year,3,20): 
            Constellation="雙魚座"
        else:
            Constellation="摩羯座"
        return (age,Constellation)


    def press_commit(self) ->None: 
        nameValue=self.nameVar.get()

        dataRegex=re.compile(r"^\d\d\d\d/\d\d/\d\d$")        
        birthValue=self.birthVar.get()
        birthMatch= re.match(dataRegex,birthValue)
        if birthMatch is None:            
            birthValue=""
        try:
            heightValue=self.heightVar.get()
        except:
            heightValue=0
        try:
            weightValue=self.weightVar.get()
        except:
            weightValue=0

        if nameValue=="" or birthValue=="" or heightValue==0 or weightValue==0:            
            self.messageText.configure(state=tk.NORMAL)
            self.messageText.delete('1.0', tk.END)
            self.messageText.insert(tk.END,"有欄位沒填或資格式有誤") 
            self.messageText.configure(state=tk.DISABLED) 
        else:    
            bmi =  weightValue /  (heightValue/100)**2
            bmiMsg=self.Bmi_msg(bmi)
            age,Constellation=self.Age_Cst(birthValue)

            message  = f"{nameValue} 您好:\n"
            message += f"  出生年月日: {birthValue}\n"
            message += f"  目前的年紀: {age} 歲\n"
            message += f"  星座      : {Constellation}\n"
            message += f"  BMI值     : {bmi:.2f}\n"
            message += f"  狀態      : {bmiMsg}"
            self.messageText.configure(state=tk.NORMAL)
            self.messageText.delete('1.0', tk.END)
            self.messageText.insert(tk.END,message) 
            self.messageText.configure(state=tk.DISABLED)     


def close_window(w):
    w.destroy()

def main():
    window = Window()
    window.title("BMI計算")
    #window.geometry("400x500")
    window.resizable(width=False,height=False)    #螢幕不能自動拉動
    #---方法1---
    #window.protocol("WM_DELETE_WINDOW",lambda: window.destroy())
    #---方法2---
    window.protocol("WM_DELETE_WINDOW",lambda: close_window(window))
    
    window.mainloop()


if __name__=='__main__':
    main()