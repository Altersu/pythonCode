# class Master:
#     def __init__(self):
#         self.kongfu = '古法煎饼配方'
#
#     def make_cake(self):
#         print(f'使用{self.kongfu}制作煎饼果子')
#
# class School:
#     def __init__(self):
#         self.kongfu = '黑马AI煎饼配方'
#     def make_cake(self):
#         print(f'使用{self.kongfu}制作煎饼果子')
# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu = '独创煎饼配方'
#     def make_cake(self):
#
#         print(f'使用{self.kongfu}制作煎饼果子')
#     def make_master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#     def make_school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
#
# if __name__ == '__main__':
#
#     p = Prentice()
#     print(p.kongfu)
#     p.make_cake()
#     p.make_master_cake()
#     p.make_school_cake()
#     print('-'*50)
#     p.make_cake()
"""
案例: 子类重写父类功能后, 继续访问父类功能.

思路:
    1. 父类名.父类函数名(self)      精准访问, 想找哪个父类, 就调哪个父类.
    2. super().父类函数名()        只能访问最近的那个父类, 有就用, 没有就往后继续查找.
"""

# 故事4: 很多顾客都希望能吃到徒弟做出的有自己独立品牌的煎饼果子，也有黑马配方技术的煎饼果子味道。
# 1. 老师父类.
class Master:
    # def __init__(self):
    #     self.kongfu = '古法煎饼配方'
    #
    # def make_cake(self):
    #     print(f'使用{self.kongfu}制作煎饼果子')
    pass

class School:
    def __init__(self):
        self.kongfu = '黑马AI煎饼配方'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')
class Prentice(Master,School):
    def __init__(self):
        self.kongfu = '独创煎饼配方'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

    # def master_make_cake(self):
    #     Master.__init__(self)
    #     Master.make_cake(self)
    # def school_make_cake(self):
    #     School.__init__(self)
    #     School.make_cake(self)

    def make_old_cake(self):
        super().__init__()
        super().make_cake()
if __name__ == '__main__':
    p = Prentice()
    print(p.kongfu)
    p.make_cake()
    # p.master_make_cake()
    # p.school_make_cake()
    print('-'*50)

    p.make_old_cake()
