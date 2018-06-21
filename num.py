import random
from SQL import FOOD, FOOD_NUM_HIGH, FOOD_HEAT_LIST


class Food(object):

    def beans(self):
        beans = []
        # 获取豆类 所有食材
        beans_list = list(FOOD['beans'])
        # 随机选择 一种豆类
        beans_num = random.randint(0, len(beans_list) - 1)
        beans = beans_list[beans_num]

        return beans

    def egg(self):
        egg = []
        egg_list = list(FOOD['egg'])
        egg_num = random.randint(0, len(egg_list) - 1)
        egg = egg_list[egg_num]
        return egg

    def fruits(self):
        fruits = []
        fruits_list = list(FOOD['fruits'])
        fruits_num = random.randint(0, len(fruits_list) - 1)
        fruits = fruits_list[fruits_num]
        return fruits

    def meat(self):
        meat = []
        meat_list = list(FOOD['meat'])
        meat_num = random.randint(0, len(meat_list) - 1)
        meat = meat_list[meat_num]
        return meat

    def nut(self):
        nut = []
        nut_list = list(FOOD['nut'])
        nut_num = random.randint(0, len(nut_list) - 1)
        nut = nut_list[nut_num]
        return nut

    def milk(self):
        milk = []
        milk_list = list(FOOD['milk'])
        milk_num = random.randint(0, len(milk_list) - 1)
        milk = milk_list[milk_num]
        return milk

    def oil(self):
        oil = []
        oil_list = list(FOOD['oil'])
        oil_num = random.randint(0, len(oil_list) - 1)
        oil = oil_list[oil_num]
        return oil

    def starch_A(self):
        starch_A = []
        starch_A_list = list(FOOD['starch_A'])
        starch_A_num = random.randint(0, len(starch_A_list) - 1)
        starch_A = starch_A_list[starch_A_num]
        return starch_A

    def starch_B(self):
        starch_B = []
        starch_B_list = list(FOOD['starch_B'])
        starch_B_num = random.randint(0, len(starch_B_list) - 1)
        starch_B = starch_B_list[starch_B_num]
        return starch_B

    def vegetable(self):
        vegetable = []
        vegetable_list = list(FOOD['vegetable'])
        vegetable_num = random.randint(0, len(vegetable_list) - 1)
        vegetable = vegetable_list[vegetable_num]
        return vegetable


# beans:豆类-3
# egg:蛋类-2
# fruits:水果类-2
# meat:肉类-1
# nut:坚果类-2
# milk:奶类-none
# oil:油类-3
# starch_A:主食A-none
# starch_B:主食B-2
# vegetable:蔬菜类-3


s = Food()


def food_list(FOOD_DICT, FOOD_HEAT):
    # 随机筛取需要的食材类份数 并且将每份大卡添加到food列表里

    food = []

    if FOOD_DICT['vegetable'][0] != 0:
        print("-----蔬菜类-----")
    for i in range(FOOD_DICT['vegetable'][0]):
        print(s.vegetable())
        food.append(FOOD_HEAT['vegetable'])

    if FOOD_DICT['beans'][0] != 0:
        print("-----豆制类-----")
    # 获取 种类份数 循环 获取 食材
    for i in range(FOOD_DICT['beans'][0]):
        print(s.beans())
        food.append(FOOD_HEAT['beans'])

    if FOOD_DICT['egg'][0] != 0:
        print("-----鸡蛋类-----")
    for i in range(FOOD_DICT['egg'][0]):
        print(s.egg())
        food.append(FOOD_HEAT['egg'])

    if FOOD_DICT['fruits'][0] != 0:
        print("-----水果类-----")
    for i in range(FOOD_DICT['fruits'][0]):
        print(s.fruits())
        food.append(FOOD_HEAT['fruits'])

    if FOOD_DICT['meat'][0] != 0:
        print("-----动物肉-----")
    for i in range(FOOD_DICT['meat'][0]):
        print(s.meat())
        food.append(FOOD_HEAT['meat'])

    if FOOD_DICT['milk'][0] != 0:
        print("-----牛奶/酸奶-----")
    for i in range(FOOD_DICT['milk'][0]):
        print(s.milk())
        food.append(FOOD_HEAT['milk'])

    if FOOD_DICT['nut'][0] != 0:
        print("-----坚果类-----")
    for i in range(FOOD_DICT['nut'][0]):
        print(s.nut())
        food.append(FOOD_HEAT['nut'])

    if FOOD_DICT['oil'][0] != 0:
        print("-----植物油-----")
    for i in range(FOOD_DICT['oil'][0]):
        print(s.oil())
        food.append(FOOD_HEAT['oil'])

    # if FOOD_DICT['starch_A'][0] != 0:
    #     print("-----主食A-----")
    # for i in range(FOOD_DICT['starch_A'][0]):
    #     print(s.starch_A())
    #     food.append(FOOD_HEAT['starch_A'])

    if FOOD_DICT['starch_B'][0] != 0:
        print("-----主食B-----")
    for i in range(FOOD_DICT['starch_B'][0]):
        print(s.starch_B())
        food.append(FOOD_HEAT['starch_B'])

    return sum(food)

# a = food_list(FOOD_NUM_LIST, FOOD_HEAT_LIST)
# # print(a)
# # print(sum(a))
