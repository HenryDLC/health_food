from post_info import *
from user import *

if __name__ == '__main__':
    # 获取用户:性别 体重 活动因数数据
    sex, weight, body_Senso = info().Body_Senso()
    # 计算用户:基础代谢 活动代谢
    metabolism_data = int(User(sex, weight, body_Senso).metabolism())

    for i in range(3):
        print('')
    print('您的每日代谢大约为:', metabolism_data)
    print('')


    # 如果大于1550大卡 随机分配
    if metabolism_data > 1550:
        high_calorie = Calorie()
        calorie_sums = high_calorie.food_list_high()
        second_random = Tools(metabolism_data, calorie_sums).second_random()

    # 如果等于1550大卡 分配标准数量食材
    elif metabolism_data == 1550:
        calorie = Calorie()
        calorie.food_list()

    # 如果低于1550但高于1200 随机分配
    elif (metabolism_data < 1550) and (metabolism_data > 1200):
        high_calorie = Calorie()
        calorie_sums = high_calorie.food_list_interval()
        second_random = Tools(metabolism_data, calorie_sums).second_random()

    # 如果低于1200 分配最低数量食材
    elif metabolism_data <= 1200:
        print("由于您的基础代谢低于1200大卡,所以我们无法为您提健康的简直餐饮计划")
        print("以下列出为1200大卡饮食计划,希望您能勤加锻炼,增加基础代谢")
        low_calorie = Calorie()
        low_calorie.food_list_low()
