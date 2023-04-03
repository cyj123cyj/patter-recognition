# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import openpyxl


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


c = ['考生姓名', '考生姓名拼音', '证件类型', '证件号码', '考生编号', '出生日期', '民族', '性别', '婚否', '政治面貌', '现役军人',
     '出生地', '籍贯地', '口所在地', '考生档案所在地', '考生档案所在单位', '考生档案所在单位地址', '所在单位邮政编码', '考生来源',
     '现学习或工作单位性质', '现学习或工作单位', '学习或工作经历', '受过何种奖励或处分', '家庭主要成员', '发表的学术论文和著作',
     '除应试外语语种外，还掌握哪国语种，掌握程度', '硕士生学位论文题目', '硕士生指导教师姓名及职称', '答辩日期', '考生自述', '获学士学位的单位',
     '获学士学位专业', '获学士学位年月', '学士学位证书编号', '本科毕业单位', '本科毕业专业', '本科毕业年月',
     '本科毕业证书编号', '本科学历的学习形式', '获硕士学位的单位', '获硕士学位专业', '获硕士学位年月', '硕士学位证书编号',
     '硕士毕业单位', '硕士毕业专业', '硕士毕业年月', '硕士毕业证书编号', '获硕士学位方式', '最后学位', '最后学历', '在校生注册学号',
     '是否同等学力','报考院系所','报考专业','研究方向','导师','招生方式','报考类别','专项计划','定向单位所在地','定向单位','英语成绩证明','通讯地址',
     '通讯地址邮编','移动电话','电子邮箱','证件照','有效居民身份证','最后学历、学位证书及其认证报告','课程成绩单','学生证及其认证报告',
     '英语水平材料','基础水平材料','学科综述(研究计划书)']
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wb = openpyxl.Workbook()  # 创建工作簿对象
    ws = wb['Sheet']  # 创建子表
    ws.append(c)  # 添加表头
    wb.save('test.xlsx')
