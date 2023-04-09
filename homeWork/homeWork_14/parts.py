import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

class TopFrame(ttk.LabelFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        ttkStyle = ttk.Style()
        ttkStyle.theme_use('clam')
        ttkStyle.configure('TLabelframe',borderwidth=0)
        
        canvas = tk.Canvas(self,width=290,height=150,scrollregion=(0,0,350,190))
        bgMountainImg = Image.open('./images/bgMountain_1.jpg')
        houseImg1New = bgMountainImg.resize((2000,200))
        self.bgMountainPhoto1 = ImageTk.PhotoImage(bgMountainImg)
        canvas.create_image(10,0,image=self.bgMountainPhoto1,anchor='nw') 

        houseImg1 = Image.open('./images/House_1.jpg')
        houseImgNew = houseImg1.resize((50,50))
        self.housePhoto = ImageTk.PhotoImage(houseImgNew)
        canvas.create_image(100,160,image=self.housePhoto,anchor='se')

        canvas.create_text(175,165,text='Mountains and House',anchor='n')

        scrollBarX = ttk.Scrollbar(self,orient='horizontal',command=canvas.xview)
        scrollBarX.pack(side='bottom',fill='x')
        scrollBarY = ttk.Scrollbar(self,orient='vertical',command=canvas.yview)
        scrollBarY.pack(side='right',fill='y')
        canvas.configure(xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)   
        #canvas.configure(xscrollcommand=scrollBarX.set)        
        canvas.pack()

class MedianFrame(ttk.LabelFrame):
    def __init__(self,master,**kwagrs):
        super().__init__(master,**kwagrs)
        self.w = master

        ttkStyle = ttk.Style()
        ttkStyle.theme_use('clam')  
        #               
        radionFrame = ttk.LabelFrame(self, text='Radio Buttons')
        radionFrame.pack(side=tk.LEFT, padx=30, pady=(0,10))
        self.RadioButtonVar = tk.StringVar()
        radioButton1 = ttk.Radiobutton(radionFrame,variable=self.RadioButtonVar,text='option-1',value='1-red',command=self.radioEvent)
        radioButton1.pack()
        radioButton2 = ttk.Radiobutton(radionFrame,variable=self.RadioButtonVar,text='option-2',value='2-green',command=self.radioEvent)
        radioButton2.pack()
        radioButton3 = ttk.Radiobutton(radionFrame,variable=self.RadioButtonVar,text='option-3',value='3-yellow',command=self.radioEvent)
        radioButton3.pack()
        radioButton4 = ttk.Radiobutton(radionFrame,variable=self.RadioButtonVar,text='option-4',value='4-blue',command=self.radioEvent)
        radioButton4.pack()
        self.RadioButtonVar.set('option-1')
        #
        checkFrame = ttk.LabelFrame(self, text='Check Buttons')
        checkFrame.pack(side=tk.LEFT, padx=30, pady=(0,10))
        self.checkButtonVar1 = tk.StringVar()
        self.checkButtonVar2 = tk.StringVar()
        self.checkButtonVar3 = tk.StringVar()
        self.checkButtonVar4 = tk.StringVar()
        checkButton1 = ttk.Checkbutton(checkFrame,variable=self.checkButtonVar1,text='option-A',onvalue='A-red',offvalue='A-off',command=self.checkEvent)
        checkButton1.pack()
        checkButton2 = ttk.Checkbutton(checkFrame,variable=self.checkButtonVar2,text='option-B',onvalue='B-green',offvalue='B-off',command=self.checkEvent)
        checkButton2.pack()
        checkButton3 = ttk.Checkbutton(checkFrame,variable=self.checkButtonVar3,text='option-C',onvalue='C-yellow',offvalue='C-off',command=self.checkEvent)
        checkButton3.pack()
        checkButton4 = ttk.Checkbutton(checkFrame,variable=self.checkButtonVar4,text='option-D',onvalue='D-blue',offvalue='D-off',command=self.checkEvent)
        checkButton4.pack()


    def radioEvent(self):
        #print(self.RadioButtonVar.get())
        self.w.radioEventOfMedianFrame(self.RadioButtonVar.get())

    def checkEvent(self):
        print(self.checkButtonVar1.get())
        print(self.checkButtonVar2.get())
        print(self.checkButtonVar3.get())
        print(self.checkButtonVar4.get())


        









