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
from post_info import *
from num import food_list
from SQL import FOOD_NUM_LIST, FOOD_HEAT_LIST


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


FOOD_NUM2 = {'fruits': [0], 'milk': [0], 'starch_A': [0], 'starch_B': [0], 'vegetable': [0]}
FOOD_HEAT2 = {'fruits': (100), 'milk': (100), 'starch_A': (350), 'starch_B': (150), 'vegetable': (50)}


# fruits:水果类-2
# vegetable:蔬菜类-3
# starch_B:主食B-2
# milk:奶类-none
# starch_A:主食A-none

class high_calorie():
    def __init__(self, metabolism_data):
        self.metabolism_data = metabolism_data

    def food_list(self):
        sums = food_list(FOOD_NUM_LIST, FOOD_HEAT_LIST)
        metabolism_data = int(self.metabolism_data - sums)
        print(sums)
        print(metabolism_data)


class low_calorie():
    # 低于1450大卡 分配最低热量配比 保证营养摄入
    def __init__(self):
        pass

    def food_list(self):
        food_list(FOOD_NUM_LIST, FOOD_HEAT_LIST)


if __name__ == '__main__':
    # 获取用户:性别 体重 活动因数数据
    sex, weight, body_Senso = info().Body_Senso()
    # 计算用户:基础代谢 活动代谢
    metabolism_data = User(sex, weight, body_Senso).metabolism()

    # 高于不分配最高热量 只分配无限制类食物
    # 低于不分配最高热量 分配所有类食物
    if metabolism_data >= 1450:
        high_calorie = high_calorie(metabolism_data)
        high_calorie.food_list()

    elif metabolism_data < 1450:
        low_calorie = low_calorie()
        low_calorie.food_list()
