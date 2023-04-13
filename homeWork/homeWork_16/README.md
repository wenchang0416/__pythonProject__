### homeWork_16
1.檔案名稱: main.py, datasource.py, messageWindow(display.py, __init__.py)

2-1.輸入

![產出圖片](./images/homework_16_011.jpg)

2-2.變更:

![產出圖片](./images/homework_15_021.jpg)

3-1.程式
```
from tkinter.simpledialog   import askinteger,askstring

self.command02_menu = tk.Menu(self.menubar,tearoff=0)
self.command02_menu.add_command(label='查詢',command=self.menu_search_click)
self.menubar.add_cascade(label='查詢',menu=self.command02_menu)

def menu_search_click(self):
    siteStr = askstring("查詢的站點名",
                        "請輸入欲查詢的站點名")
    for item in self.tree.get_children():
        self.tree.delete(item)  
    for item in self.area_data:
        if siteStr in item['sna'] or siteStr in item['ar']:
            self.tree.insert('', tk.END, values=[item['sna'][11:],item['mday'],item['tot'],item['sbi'],item['bemp'],item['ar'],item['act']],tags=item['sna'])
```
