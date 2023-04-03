from lxml import etree

import pandas
import requests

headers = {'Cookie': 'AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-1810458078%7CMCIDTS%7C19255%7CMCMID%7C63290459878625955163457491329760856461%7CMCAID%7CNONE%7CMCOPTOUT-1663568590s%7CNONE%7CMCAAMLH-1664166190%7C11%7CMCAAMB-1664166190%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19262%7CvVersion%7C5.4.0%7CMCCIDH%7C1963592016; mbox=session#dae01437eb084f8a978c7d29400a6c31#1663563258|PC#dae01437eb084f8a978c7d29400a6c31.37_0#1726806187; s_pers=%20v8%3D1663561398968%7C1758169398968%3B%20v8_s%3DFirst%2520Visit%7C1663563198968%3B%20c19%3Did%253Aerror%253Aapplication%2520error%7C1663563198970%3B%20v68%3D1663561397317%7C1663563198974%3B; _hp2_id.1083010732=%7B%22userId%22%3A%226075456315328296%22%2C%22pageviewId%22%3A%228971294433536739%22%2C%22sessionId%22%3A%224784018467654564%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga=GA1.3.584225894.1663561799; _hjSessionUser_1290436=eyJpZCI6ImNkNTg2YTY0LTUwNmQtNTg5My1iZjE3LWU4OTQ5MTYwZmI1MiIsImNyZWF0ZWQiOjE2NjM1NjE3OTkwOTUsImV4aXN0aW5nIjpmYWxzZX0=; sessionid=tzkq5rdombi12ebnvqqdhzk0zsjwx8bu',
'Host': 'gsadmission.bjtu.edu.cn',
'Referer': 'https://gsadmission.bjtu.edu.cn/phd/tutor/tutor_evaluation/',
'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'}

all_data = pandas.read_excel(
    r'C:\Users\29859\Desktop\研一下学期课程\模式识别\homework\3月31日\pattern recognition\from_mis_get_doctor_info\all_info.xlsx',
    header=0)
all_info_list = []
c = ['考生姓名', '考生姓名拼音', '证件类型', '证件号码', '考生编号', '出生日期', '民族', '性别', '婚否', '政治面貌', '现役军人',
     '出生地', '籍贯地', '口所在地', '考生档案所在地', '考生档案所在单位', '考生档案所在单位地址', '所在单位邮政编码', '考生来源',
     '现学习或工作单位性质', '现学习或工作单位', '学习或工作经历', '受过何种奖励或处分', '家庭主要成员', '发表的学术论文和著作',
     '除应试外语语种外，还掌握哪国语种，掌握程度', '硕士生学位论文题目', '硕士生指导教师姓名及职称', '答辩日期', '考生自述', '获学士学位的单位',
     '获学士学位专业', '获学士学位年月', '学士学位证书编号', '本科毕业单位', '本科毕业专业', '本科毕业年月',
     '本科毕业证书编号', '本科学历的学习形式', '获硕士学位的单位', '获硕士学位专业', '获硕士学位年月', '硕士学位证书编号',
     '硕士毕业单位', '硕士毕业专业', '硕士毕业年月', '硕士毕业证书编号', '获硕士学位方式', '最后学位', '最后学历', '在校生注册学号',
     '是否同等学力','报考院系所','报考专业','研究方向','导师','招生方式','报考类别','专项计划','定向单位所在地','定向单位','英语成绩证明','通讯地址',
     '通讯地址邮编','移动电话','电子邮箱','证件照','有效居民身份证','最后学历','学位证书及其认证报告','课程成绩单','学生证及其认证报告',
     '英语水平材料','基础水平材料','学科综述(研究计划书)']
all_info_list.append(c)
for i in all_data.values.tolist():
    name = i[3]
    print(name)
    basic_info = 'https://gsadmission.bjtu.edu.cn' + i[2]
    response = requests.get(basic_info,headers=headers, stream=True, timeout=20)
    tree = etree.HTML(response.text)

    name_charactor = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[1]/td[1]/text()')
    name_pinyin = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[1]/td[2]/text()')
    card_type = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[2]/td[1]/text()')
    card_num = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[2]/td[2]/text()')
    candidate_ID = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[3]/td[1]/text()')
    birth_date = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[3]/td[2]/text()')
    ethnicity = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[4]/td[1]/text()')
    gender = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[4]/td[2]/text()')
    married_or_not = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[5]/td[1]/text()')
    political_status = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[5]/td[2]/text()')
    soldier_not =tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[6]/td[1]/text()')
    birth_place = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[6]/td[2]/text()')
    native_place = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[7]/td[1]/text()')
    account = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[7]/td[2]/text()')
    file_place = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[8]/td[1]/text()')
    file_unit = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[8]/td[2]/text()')
    file_address = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[9]/td[1]/text()')
    file_post_code = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[9]/td[2]/text()')
    candidate_source = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[10]/td[1]/text()')
    unit_nature = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[10]/td[2]/text()')

    study_work_unit = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[11]/td[1]/text()')
    study_work_experience = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[12]/td[1]/text()')
    reward_punishment = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[13]/td[1]/text()')
    family_members = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[14]/td[1]/text()')
    academic_papers = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[15]/td[1]/text()')
    foreign_language = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[16]/td[1]/text()')
    aaster_thesis_title = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[17]/td[1]/text()')
    tutor_name = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[18]/td[1]/text()')
    defense_date = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[19]/td[1]/text()')
    candidate_self_report = tree.xpath('/html/body/div/div[2]/div[2]/div/table[1]/tr[20]/td[1]/text()')



    bachelor_unit = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[1]/td[1]/text()')
    bachelor_major = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[1]/td[2]/text()')
    bachelor_date = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[2]/td[1]/text()')
    bachelor_code = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[2]/td[2]/text()')
    undergraduate_unit = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[3]/td[1]/text()')
    undergraduate_major = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[3]/td[2]/text()')
    undergraduate_date = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[4]/td[1]/text()')
    undergraduate_code = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[4]/td[2]/text()')
    undergraduate_learning_way = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[5]/td[1]/text()')



    master_bachelor_unit = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[6]/td[1]/text()')
    master_bachelor_major = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[6]/td[2]/text()')
    master_bachelor_date = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[7]/td[1]/text()')
    master_bachelor_code = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[7]/td[2]/text()')
    master_undergraduate_unit = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[8]/td[1]/text()')
    master_undergraduate_major = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[8]/td[2]/text()')
    master_undergraduate_date = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[9]/td[1]/text()')
    master_undergraduate_code = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[9]/td[2]/text()')
    master_undergraduate_learning_way = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[10]/td[1]/text()')
    last_degree1 = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[11]/td[1]/text()')
    last_degree2 = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[11]/td[2]/text()')
    master_undestudent_ID = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[12]/td[1]/text()')
    equivalent_mechanicsrgraduate_code = tree.xpath('/html/body/div/div[2]/div[2]/div/table[2]/tr[12]/td[2]/text()')



    apply_department = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[1]/td[1]/text()')
    apply_major = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[1]/td[2]/text()')
    research_direction = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[2]/td[1]/text()')
    research_tutor = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[2]/td[2]/text()')
    enrollment_method = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[3]/td[1]/text()')
    type_appliction = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[3]/td[2]/text()')
    special_plan = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[4]/td[1]/text()')
    location_targeted_unit_place = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[4]/td[2]/text()')
    location_targeted_unit = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[5]/td[1]/text()')
    english_level = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[5]/td[2]/text()')
    mailing_address = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[6]/td[1]/text()')
    posting_address = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[6]/td[2]/text()')
    tele_nimber = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[7]/td[1]/text()')
    email_address = tree.xpath('/html/body/div/div[2]/div[2]/div/table[3]/tr[7]/td[2]/text()')


    id_photo = tree.xpath('/html/body/div/div[2]/div[2]/div/div/ul/li[1]/a/@href')
    id_card = tree.xpath('/html/body/div/div[2]/div[2]/div/div/ul/li[2]/a/@href')
    final_report = tree.xpath('/html/body/div/div[2]/div[2]/div/div/ul/li[3]/a/@href')
    transcript = tree.xpath('/html/body/div/div[2]/div[2]/div/div/ul/li[4]/a/@href')
    student_card = tree.xpath('/html/body/div/div[2]/div[2]/div/div/ul/li[5]/a/@href')
    english_material = tree.xpath('/html/body/div/div[2]/div[2]/div/div/ul/li[6]/a/@href')
    fundation_info = tree.xpath('/html/body/div/div[2]/div[2]/div/div/ul/li[7]/a/@href')
    research_proposal = tree.xpath('/html/body/div/div[2]/div[2]/div/div/ul/li[8]/a/@href')

    content = [name_charactor,name_pinyin,card_type,card_num,candidate_ID,birth_date,ethnicity,gender,married_or_not,
               political_status,soldier_not,birth_place,native_place,account,file_place,file_unit,file_address,
               file_post_code,candidate_source,unit_nature,study_work_unit,study_work_experience,reward_punishment,
               family_members,academic_papers,foreign_language,aaster_thesis_title,tutor_name,defense_date,
               candidate_self_report,bachelor_unit,bachelor_major,bachelor_date,bachelor_code,undergraduate_unit,
               undergraduate_major,undergraduate_date,undergraduate_code,undergraduate_learning_way,
               master_bachelor_unit,master_bachelor_major,master_bachelor_date,master_bachelor_code,master_undergraduate_unit,
               master_undergraduate_major,master_undergraduate_date,master_undergraduate_code,master_undergraduate_learning_way,
               last_degree1,last_degree2,master_undestudent_ID,equivalent_mechanicsrgraduate_code,apply_department,
               apply_major,research_direction,research_tutor,enrollment_method,type_appliction,special_plan,
               location_targeted_unit_place,location_targeted_unit,english_level,mailing_address,posting_address,
               tele_nimber,email_address,id_photo,id_card,final_report,transcript,student_card,english_material,
               fundation_info,research_proposal]
    all_info_list.append(content)
a = pandas.DataFrame(all_info_list)
a.to_excel('all_person_info.xlsx',sheet_name='sheet')