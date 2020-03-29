import requests
from bs4 import BeautifulSoup
import xlwt

#将二维列表写入Excel表
def WriteExcel(List,Name,SmallName):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet(SmallName)
    for i in range(0, len(List)):
        for j in range(0, len(List[i])):
            worksheet.write(i, j, label=List[i][j])
    workbook.save(Name)

Final=[]

for i in range(2,52):
    try:
        url='https://frontapp.com/blog/page/{}/'.format(i)
        resp = requests.get(url)
        a = resp.content.decode('utf-8')
        soup = BeautifulSoup(a)

        List=soup.find_all("h2",class_="fa-post-title")

        for list in List:
            Final.append([list.find("a").string,"https://frontapp.com"+list.find("a")['href']])
    except:
        print("",end="")

WriteExcel(Final,"Front.xls",'FrontBlog')