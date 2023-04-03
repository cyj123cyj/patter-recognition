import time

import pandas
import requests

pdf_url = 'https://gsadmission.bjtu.edu.cn/media/phd/user_doc7/2022/11/22/025739.pdf'
# res_size = requests.head(pdf_url)
# content_length = res_size.headers['Content-Length']

# 再用 pdf的大小去构建请求头
# headers = {
#     'Connection': 'keep-alive',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Range': f'bytes=0-{content_length}',
# }

# resp = requests.get(pdf_url, stream=True, timeout=20)
# print(resp.content)
all_data = pandas.read_excel(
    r'C:\Users\29859\Desktop\研一下学期课程\模式识别\homework\3月31日\pattern recognition\from_mis_get_doctor_info\all_info.xlsx',
    header=0)
for i in all_data.values.tolist():
    name = i[3]
    print(name)
    foundation_level_materials_url = 'https://gsadmission.bjtu.edu.cn' + i[6]
    subject_review = 'https://gsadmission.bjtu.edu.cn' + i[8]
    # resp1 = requests.get(foundation_level_materials_url, stream=True, timeout=20)
    # time.sleep(3)
    resp2 = requests.get(subject_review, stream=True, timeout=20)
    time.sleep(4)
    # with open(name + '基础水平材料.pdf', 'wb') as fd:
    #     fd.write(resp1.content)
    with open(name + '学科综述（研究计划书）.pdf', 'wb') as f:
        f.write(resp2.content)
