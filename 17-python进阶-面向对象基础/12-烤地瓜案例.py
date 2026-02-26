# # class SweetPotato:
# #     def __init__(self):
# #         self.cook_time = 0
# #         self.cook_state = '生的'
# #         self.condiments = []
# #
# #     def cook(self,time):
# #         self.cook_time += time
# #         if  0< self.cook_time <3:
# #             self.cook_state = '生的'
# #         elif 3<= self.cook_time <5:
# #             self.cook_state = '半生不熟'
# #         elif 5<= self.cook_time <8:
# #             self.cook_state = '熟了'
# #         elif self.cook_time >=8:
# #             self.cook_state = '烤糊了'
# #     def add_condiments(self,condiments):
# #         self.condiments.append(condiments)
# #
# #     def __str__(self):
# #         return f'这个地瓜的被烤过的时间是{self.cook_time},状态是{self.cook_state},添加的调料有{self.condiments}'
# # digua1 = SweetPotato()
# # print(digua1)
# # digua1.cook(9)
# # digua1.add_condiments('芝士')
# # print(digua1)
#
# class kaodigua:
#     def __init__(self):
#         self.cook_time = 0
#         self.cook_state = '生的'
#         self.condiments = []
#
#     def cook(self,time):
#
#         if time <=0:
#             print('时间不能小于0')
#         else:
#             self.cook_time += time
#             if 0<= self.cook_time <3:
#                self.cook_state ='生的'
#             elif 3<=self.cook_time <7:
#                 self.cook_state ='半生不熟'
#             elif 7<=self.cook_time <12:
#                 self.cook_state ='熟了'
#             else:
#                 self.cook_state ='烤糊了'
#
#     def add_condiments(self,condiment):
#         self.condiments.append(condiment)
#
#     def __str__(self):
#         return f'这个地瓜被烤了{self.cook_time}分钟，状态是{self.cook_state},添加的调料有{self.condiments}'
#
# if __name__ == '__main__':
#    dg = kaodigua()
#    dg.cook(14)
#    dg.add_condiments('孜然')
#    print(dg)
"""
案例: 烤地瓜案例.

需求:
    1. 定义地瓜类 -&gt; SweetPotato
    2. 属性: 被烤时间cook_time, 烘焙状态 cook_state, 调料 condiments
    3. 行为: 烘烤cook(), 添加调料 add_condiment()
    4. 魔法方法: init() -&gt; 初始化属性,  str() -&gt; 打印地瓜信息.
    5. 规则:
        烘烤时间        地瓜状态
        [0, 3)          生的          包左不包右, 前闭后开.
        [3, 7)          半生不熟
        [7, 12)         熟了
        [12, ∞]         糊了
"""
# 1. 定义地瓜类 -&gt; SweetPotato
class SweetPotato:
    # 2. 在魔法方法__init__()中, 初始化地瓜的属性.
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiments = []

    # 3.具体的烘烤动作.
    def cook(self, time):
        # 3.1 根据烘烤时间, 修改地瓜的烘烤状态.
        if time <0:
            print('无效值!')
        else:
            # 3.2 修改地瓜的 烘烤时间.
            self.cook_time += time
            # 3.3 根据烘烤时间, 修改地瓜的烘烤状态.
            if 0 <= self.cook_time < 3:
                self.cook_state = '生的'
            elif 3 <= self.cook_time < 7:
                self.cook_state = '半生不熟'
            elif 7 <= self.cook_time < 12:
                self.cook_state = '熟了'
            else:
                self.cook_state = '糊了'

    # 4. 添加调料 add_condiment()
    def add_condiment(self, condiment):
        self.condiments.append(condiment)

    # 5. 重写str()方法, 打印地瓜信息.
    def __str__(self):
        return f'烘烤时间: {self.cook_time}, 地瓜状态: {self.cook_state}, 调料: {self.condiments}'

# 6.测试.
if __name__ == '__main__':
    # 7. 创建地瓜对象
    dg = SweetPotato()

    # 8. 具体的烘烤动作.
    # dg.cook(-3)
    dg.cook(3)
    dg.cook(5)
    dg.cook(7)

    # 9. 添加调料
    dg.add_condiment('芥末/辣根')
    dg.add_condiment('折耳根')
    dg.add_condiment('豆汁')
    dg.add_condiment('鲱鱼罐头')

    # 10. 打印地瓜状态.
    print(dg)