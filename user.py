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

class Tools():
    def __init__(self, metabolism_data, calorie_sums):
        self.metabolism_data = metabolism_data
        self.calorie_sums = calorie_sums

    def food_random(self, items):
        # 随机找取各类食物
        total = sum(w for _, w in items)
        n = uniform(0, total)  # 在饼图扔骰子
        for x, w in items:  # 遍历找出骰子所在的区间
            if n < w:
                break
            n = n - w
        return x

    def second_random(self):
        # 二次分配
        print("二次分配测试")
        metabolism_surplus = self.metabolism_data - self.calorie_sums
        metabolism_surplus = round(metabolism_surplus / 100) * 100

        # 随机每次查找一种食物 相加直到符合基础代谢

        food_random_name = ''

        while metabolism_surplus >= 0:
            food_random_name = self.food_random(FOOD_HEAT_LIST_ALLOT)
            metabolism_surplus -= FOOD_HEAT_LIST_ALLOT_B[food_random_name]
            FOOD_NUM_LIST_TEMP[food_random_name][0] += 1

            if FOOD_NUM_LIST_TEMP['milk'][0] >3:
                FOOD_NUM_LIST_TEMP['milk'][0] -= 1
                metabolism_surplus += FOOD_HEAT_LIST_ALLOT_B['milk']

            if FOOD_NUM_LIST_TEMP['fruits'][0] >3:
                FOOD_NUM_LIST_TEMP['fruits'][0] -= 1
                metabolism_surplus += FOOD_HEAT_LIST_ALLOT_B['fruits']

        print(metabolism_surplus)
        # FOOD_NUM_LIST_TEMP[food_random_name][0] -= 1
        food_list(FOOD_NUM_LIST_TEMP, FOOD_HEAT_LIST_ALLOT_B)


class Calorie():

    def food_list(self):
        # 标准分配1550大卡
        # calorie_sums第一次分配食材大卡总量
        # metabolism_data 基础代谢率
        # metabolism_surplus 剩余未分配代谢量
        calorie_sums = food_list(FOOD_NUM_HIGH, FOOD_HEAT_LIST)
        return calorie_sums

    def food_list_high(self):
        # 大于1550大卡 二次分配
        # calorie_sums第一次分配食材大卡总量
        # metabolism_data 基础代谢率
        # metabolism_surplus 剩余未分配代谢量

        calorie_sums = food_list(FOOD_NUM_HIGH, FOOD_HEAT_LIST)
        return calorie_sums

    def food_list_low(self):
        # 低于1200大卡
        # calorie_sums第一次分配食材大卡总量
        # metabolism_data 基础代谢率
        # metabolism_surplus 剩余未分配代谢量
        calorie_sums = food_list(FOOD_NUM_LIST_LOW, FOOD_HEAT_LIST)
        return calorie_sums

    def food_list_interval(self):
        calorie_sums = food_list(FOOD_NUM_LIST_LOW, FOOD_HEAT_LIST)
        return calorie_sums
