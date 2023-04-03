import pandas

all_data = pandas.read_excel(
    r'C:\Users\29859\Desktop\研一下学期课程\模式识别\homework\3月31日\pattern recognition\from_mis_get_doctor_info\all_person_info.xlsx',
    header=0)
new_data = []
new_data.append(all_data.columns)
for i in all_data.values.tolist():
    tem = [j.replace('[','').replace(']','').replace("'",'') for j in i ]
    new_data.append(tem)
a = pandas.DataFrame(new_data)
a.to_excel('all_doctor_info.xlsx',sheet_name='sheet')
