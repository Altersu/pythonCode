# #
# # class Animal:
# #     def speak(self):
# #         pass
# #
# # class Dog(Animal):
# #     def speak(self):
# #         print("汪汪汪")
# #
# # class Cat(Animal):
# #     def speak(self):
# #         print("喵喵喵")
# #
# # def make_noise(animal:Animal):
# #     animal.speak( )
#
# class AC:
#     def cool_wind(self):
#         pass
#     def hot_wind(self):
#         pass
#     def swing_l_r(self):
#         pass
#
# class Midea_AC(AC):
#     def cool_wind(self):
#         print("Midea_AC: 冷风")
#     def hot_wind(self):
#         print("Midea_AC: TestHot")
#     def swing_l_r(self):
#         print("Midea_AC: TestHot")
#
# class Haier_AC(AC):
#     def cool_wind(self):
#         print("Haier_AC: 冷风")
#     def hot_wind(self):
#         print("Haier_AC: TestHot")
#     def swing_l_r(self):
#         print("Haier_AC: TestHot")
#
# def make_cool(ac:AC):
#     ac.cool_wind()
# def make_hot(ac:AC):
#     ac.hot_wind()
# def make_swing(ac:AC):
#     ac.swing_l_r()
#
# midea_ac = Midea_AC()
# haier_ac = Haier_AC()
#
# make_cool(midea_ac)
# make_cool(haier_ac)
# make_hot(midea_ac)
# make_hot(haier_ac)
# make_swing(midea_ac)
# make_swing(haier_ac)

# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         return "wangwangwang~"
# # dog= Dog()
# # print(dog.speak())
# class Cat(Animal):
#     def speak(self):
#         return "miaomiaomiao~"
# def make_sound(animal:Animal):
#     print(animal.speak())
#
# dog= Dog()
# cat= Cat()
# make_sound(dog)
# make_sound(cat)

class Person:
    def speak(self):
        return "我也会叫"

class Robot:
    def speak(self):
        return "机器声"

def make_sound(entity):
    print(entity.speak())

make_sound(Person())  # 我也会叫
make_sound(Robot())   # 机器声
