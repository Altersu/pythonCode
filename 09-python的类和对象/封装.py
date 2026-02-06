#
#
# class phone:
#
#     __current_voltage = 0
#
#     def __keep_single_core(self):
#         print("保持单核运行")
#
#     def call_by_5g(self):
#         if self.__current_voltage >=1:
#             print("5G通话")
#         else:
#             self.__keep_single_core()
#             print("电量不足，无法使用5g童话")
#
# phone = phone()
# phone.call_by_5g()

class Phone:
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5G通话")
        else:
            print("5g关闭，使用4g通话")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")
phone = Phone()
phone.call_by_5g()
