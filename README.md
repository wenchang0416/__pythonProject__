# __PythonProject__
---
## HomeWork_13

![產生圖片](./homeWork/images/homework_13.PNG)

檔名及路徑 : HomeWork_13.py
- https://github.com/wenchang0416/__pythonProject__/blob/master/homeWork/homework_13.py

```
from datetime import datetime
def Age_Cst(self,birthValue):
        date_now = datetime.now()        
        date_birth = datetime.strptime(birthValue, '%Y/%m/%d')
        age=date_now.year-date_birth.year

        if   datetime(date_birth.year,3,21)<=date_birth<=datetime(date_birth.year,4,20):
            Constellation="牡羊座"   
        elif datetime(date_birth.year,4,21)<=date_birth<=datetime(date_birth.year,5,21): 
            Constellation="金牛座"
        |
        elif datetime(date_birth.year,2,19)<=date_birth<=datetime(date_birth.year,3,20): 
            Constellation="雙魚座"
        else:
            Constellation="摩羯座"
        return (age,Constellation)    
```
---

## HomeWork_12

檔名及路徑 : HomeWork_12_Wgrid.py
- https://github.com/wenchang0416/__pythonProject__/blob/master/homeWork/homework_12_Wgrid.py

---
