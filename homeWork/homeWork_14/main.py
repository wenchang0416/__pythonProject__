import tkinter as tk
from parts import TopFrame,MedianFrame


class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        topFrame = TopFrame(self)
        topFrame.pack()
        medianFrame = MedianFrame(self)
        medianFrame.pack(fill=tk.X)
    def radioEventOfMedianFrame(self,radioEventValue):
        print(radioEventValue)


def main():
    window = Window()
    window.title('This is Widgets')
    window.mainloop()


if __name__=='__main__':
    main()