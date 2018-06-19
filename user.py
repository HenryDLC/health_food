'''
获取性别
获取体重
获取运动因数

算出基础代谢率
算出每日消耗

每日食物量(每日消耗-300~500)
配比:2:3:3:1:2:2:0:3:2 (每日实物量 / 18)
算出 每类食物卡路里数
算出 每类食物 份数

随机 找出相应分数 食物种类
'''

from random import uniform
from post_info import *
from num import food_list
from SQL import *


# 使用用户的性别/体重/活动因数 进行计算
class User():
    def __init__(self, sex, weight, body_Senso):
        self.sex = sex
        self.weight = weight
        self.body_Senso = body_Senso

    # 计算每日活动代谢
    # metabolism: 基础代谢
    # metabolism_data: 日常代谢
    def metabolism(self):
        metabolism_data = 0
        if self.sex == 0:
            metabolism = (48.5 * self.weight + 2954.7) / 4.184
            metabolism_data = metabolism * self.body_Senso
        elif self.sex == 1:
            metabolism = (41.9 * self.weight + 2869.1) / 4.184
            metabolism_data = metabolism * self.body_Senso
        return metabolism_data


# FOOD_NUM2 = {'fruits': [0], 'milk': [0], 'starch_A': [0], 'starch_B': [0], 'vegetable': [0]}
# FOOD_HEAT2 = {'fruits': (100), 'milk': (100), 'starch_A': (350), 'starch_B': (150), 'vegetable': (50)}


# fruits:水果类-2
# vegetable:蔬菜类-3
# starch_B:主食B-2
# milk:奶类-none
# starch_A:主食A-none

def food_random(items):
    # 随机找取各类食物
    total = sum(w for _, w in items)
    n = uniform(0, total)  # 在饼图扔骰子
    for x, w in items:  # 遍历找出骰子所在的区间
        if n < w:
            break
        n = n - w
    return x

class Calorie():
    def __init__(self, metabolism_data):
        self.metabolism_data = metabolism_data

    def food_list(self):
        # 标准分配1550大卡
        # calorie_sums第一次分配食材大卡总量
        # metabolism_data 基础代谢率
        # metabolism_surplus 剩余未分配代谢量
        calorie_sums = food_list(FOOD_NUM_LIST, FOOD_HEAT_LIST)

    def food_list_high(self):
        # 大于1550大卡 二次分配
        # calorie_sums第一次分配食材大卡总量
        # metabolism_data 基础代谢率
        # metabolism_surplus 剩余未分配代谢量
        calorie_sums = food_list(FOOD_NUM_LIST, FOOD_HEAT_LIST)

        # 二次分配
        print("二次分配测试")
        metabolism_surplus = self.metabolism_data - calorie_sums
        metabolism_surplus = round(metabolism_surplus / 100) * 100

        # 随机每次查找一种食物 相加直到符合基础代谢
        food_random_name_list = []
        food_random_name_surplus_list = []

        random_num = 0
        while 1:
            if random_num <= metabolism_surplus:
                food_random_name = food_random(FOOD_HEAT_LIST_ALLOT)
                food_random_name_list.append(food_random_name)

                food_random_name_surplus_list.append(FOOD_HEAT_LIST_ALLOT_B[food_random_name])
                random_num = sum(food_random_name_surplus_list)

            elif random_num >= metabolism_surplus:
                food_random_name_list = []
                food_random_name_surplus_list = []
                random_num = 0

            elif random_num == metabolism_surplus:
                break

        print(food_random_name_list)






    def food_list_low(self):
        # 大于1200大卡,二次分配
        # calorie_sums第一次分配食材大卡总量
        # metabolism_data 基础代谢率
        # metabolism_surplus 剩余未分配代谢量
        calorie_sums = food_list(FOOD_NUM_LIST_LOW, FOOD_HEAT_LIST)


if __name__ == '__main__':
    # 获取用户:性别 体重 活动因数数据
    sex, weight, body_Senso = info().Body_Senso()
    # 计算用户:基础代谢 活动代谢
    metabolism_data = int(User(sex, weight, body_Senso).metabolism())
    print('您的基础代谢率为:', metabolism_data)

    # 如果大于1550大卡 随机分配
    if metabolism_data > 1550:
        high_calorie = Calorie(metabolism_data)
        high_calorie.food_list_high()

    # 如果等于1550大卡 分配标准数量食材
    elif metabolism_data == 1550:
        high_calorie = Calorie(metabolism_data)
        high_calorie.food_list()

    # 如果低于1550但高于1100 随机分配
    elif (metabolism_data < 1550) and (metabolism_data > 1200):
        pass

    # 如果低于1200 分配最低数量食材
    elif metabolism_data < 1200:
        high_calorie = Calorie(metabolism_data)
        high_calorie.food_list_low()
