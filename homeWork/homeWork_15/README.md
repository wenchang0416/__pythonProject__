### homeWork_15
1.檔案名稱: main.py、datasource.py

2-1.預設區: 信義區

![產出圖片](./images/homework_15_011.jpg)

2-2.變更區: 士林區

![產出圖片](./images/homework_15_021.jpg)

3-1.程式-資料刪除
```
for item in self.tree.get_children():
    self.tree.delete(item)
```

3-2.程式-scrollBar
```
self.scrollBarY = ttk.Scrollbar(bottomFrame,orient='vertical',command=self.tree.yview)
self.scrollBarY.pack(side=tk.RIGHT,fill=tk.Y)
self.tree.configure(yscrollcommand=self.scrollBarY.set)
self.tree.pack()
```