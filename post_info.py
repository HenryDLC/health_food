class info():
    def __init__(self):
        self.A = "A 休息,坐卧为主 比如:不能自理的老年人或残疾人等\n"
        self.B = "B 静态生活/工作方式 比如:办公室职员或坐着工作的职业从业\n"
        self.C = "C 坐姿生活方式为主,偶尔活动 比如:学生/司机/装配工人等\n"
        self.D = "D 站/走为主的生活方式 比如:家庭主妇/销售人员/服务员/接待员\n"
        self.E = "E 重体力生活或工作方式 比如:建筑工人/农民/旷工/运动员或运动爱好者\n"

    def index(self):
        print("请输入个人信息:\n")
        while 1:
            while 1:
                gender = input('请输入您的性别:')
                if gender.lower() in ['男', 'nan', 'man']:
                    gender = '男'
                    sex = 0
                    break
                elif gender.lower() in ['女', 'nv', 'woman']:
                    gender = '女'
                    sex = 1
                    break
                else:
                    print('输入错误请重新输入:\n')
            while 1:
                try:
                    weight = float(input("请输入您的体重:(单位KG)"))
                    break
                except ValueError:
                    print("体重输入错误请重新输入:\n")
            ny = input("您的性别是:%s,体重是%.2f公斤,请确认以上信息:(回车键确认)\n" % (gender, weight))
            if ny == '':
                break
            else:
                print("请重新输入个人信息:")

        return sex, weight

    def Body_Senso_Data(self, body_Senso):
        if body_Senso.upper() == 'A':
            body_Senso = 1.2
        elif body_Senso.upper() == 'B':
            body_Senso = 1.45
        elif body_Senso.upper() == 'C':
            body_Senso = 1.65
        elif body_Senso.upper() == 'D':
            body_Senso = 1.85
        elif body_Senso.upper() == 'E':
            body_Senso = 2.2

        return body_Senso

    def Body_Senso(self):
        sex, weight = self.index()
        print("请问您一周的运动量是多少:\n")
        while 1:
            print(self.A, self.B, self.C, self.D, self.E)
            body_Senso = input("请输入对应字母代码:")

            if body_Senso.upper() in ['A', 'B', 'C', 'D', 'E']:
                body_Senso2 = input("您是否有明显体的育活动(每周4~5次,每次30~60分钟):")
                YES = ['Y', 'YES', 'SHI', 'y', 'yes', 'shi', '是', '有']
                NO = ['N', 'no', 'BU', 'N', 'no', 'bu', '不', '没有']
                if body_Senso2 in YES:
                    body_Senso = self.Body_Senso_Data(body_Senso)
                    body_Senso += 0.3
                    return sex, weight, body_Senso
                elif body_Senso2 in NO:
                    body_Senso = self.Body_Senso_Data(body_Senso)
                    return sex, weight, body_Senso
                else:
                    print('输入错误请重新输入:\n')
            else:
                print("输入错误请重新输入:\n")
