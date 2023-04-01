import pandas
from lxml import etree

import requests
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-1810458078%7CMCIDTS%7C19255%7CMCMID%7C63290459878625955163457491329760856461%7CMCAID%7CNONE%7CMCOPTOUT-1663568590s%7CNONE%7CMCAAMLH-1664166190%7C11%7CMCAAMB-1664166190%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19262%7CvVersion%7C5.4.0%7CMCCIDH%7C1963592016; mbox=session#dae01437eb084f8a978c7d29400a6c31#1663563258|PC#dae01437eb084f8a978c7d29400a6c31.37_0#1726806187; s_pers=%20v8%3D1663561398968%7C1758169398968%3B%20v8_s%3DFirst%2520Visit%7C1663563198968%3B%20c19%3Did%253Aerror%253Aapplication%2520error%7C1663563198970%3B%20v68%3D1663561397317%7C1663563198974%3B; _hp2_id.1083010732=%7B%22userId%22%3A%226075456315328296%22%2C%22pageviewId%22%3A%228971294433536739%22%2C%22sessionId%22%3A%224784018467654564%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga=GA1.3.584225894.1663561799; _hjSessionUser_1290436=eyJpZCI6ImNkNTg2YTY0LTUwNmQtNTg5My1iZjE3LWU4OTQ5MTYwZmI1MiIsImNyZWF0ZWQiOjE2NjM1NjE3OTkwOTUsImV4aXN0aW5nIjpmYWxzZX0=; sessionid=59w7pwyxdsnyor02u6so9dwgpv2mdv97',
'Host': 'gsadmission.bjtu.edu.cn',
'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'}
url = 'https://gsadmission.bjtu.edu.cn/phd/tutor/tutor_evaluation/'
response = requests.get(url=url, headers=headers, verify=False, timeout=10)
# print(response.text)
tree = etree.HTML(response.text)
headers_columns = []
for i in range(12):
    headers_columns.append(tree.xpath('/html/body/div/div[2]/div[2]/div/div/table/tr[1]/th[' + str(i + 1) + ']/text()'))
print(headers_columns)
info = tree.xpath('/html/body/div/div[2]/div[2]/div/div/table/tr')
persons_info = []
for j in range(2,len(info)):
    person_info = []
    for k in range(4):
        tem1 = tree.xpath('/html/body/div/div[2]/div[2]/div/div/table/tr['+str(j)+']/td[' + str(k + 1) + ']/a/text()')
        tem2 = tree.xpath('/html/body/div/div[2]/div[2]/div/div/table/tr['+str(j)+']/td[' + str(k + 1) + ']/a/@href')
        person_info.extend(tem1)
        person_info.extend(tem2)
    persons_info.append(person_info)
print(persons_info)
a = pandas.DataFrame(persons_info)
a.to_excel('all_info.xlsx',sheet_name='sheet')

