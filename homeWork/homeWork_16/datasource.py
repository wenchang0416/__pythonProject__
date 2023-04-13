import requests

sarea_list = None
data_List = None

def getInfo():
    global sarea_list,data_List
    url='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(url)
    data_List = response.json()             #轉成json格式
    sarea_tmp = set()
    for item in data_List:
        sarea_tmp.add(item['sarea'])
    sarea_list = sorted(list(sarea_tmp))

def getInfoDataFromArea(area_name):
    filter_data=filter(lambda n: n['sarea']==area_name ,data_List)
    return list(filter_data)

def filter_sbi_warning_data(area_data,numbers)  ->list:
    filter_data = filter(lambda n:n['sbi']<=numbers,area_data)
    return list(filter_data)

def filter_bemp_warning_data(area_data,nubmers)  ->list:
    filter_data = filter(lambda n:n['bemp']<=nubmers,area_data)
    return list(filter_data)






getInfo()


