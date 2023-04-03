import time

import pandas
import requests

all_data = pandas.read_excel(
    r'C:\Users\29859\Desktop\研一下学期课程\模式识别\homework\3月31日\pattern recognition\from_mis_get_doctor_info\all_person_info.xlsx' ,
    header=0)
label = 0
for i in all_data.values.tolist():
    if label<32:
        pass
    else:
        name = i[0].replace('[','').replace(']','').replace("'",'')
        print(name)
        subject_review = 'https://gsadmission.bjtu.edu.cn' + i[66].replace('[','').replace(']','').replace("'",'')
        print(subject_review)
        resp2 = requests.get(subject_review, verify=False,stream=True, timeout=30)
        time.sleep(3)
        with open(name + '证件照.jpg', 'wb') as f:
            f.write(resp2.content)
    label += 1
