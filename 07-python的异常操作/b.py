# from a import hello
# hello()
# print("b.py:", __name__)


# import a
# print("main.py __name__ =", __name__)

# import a
# print("b.py 顶层代码执行")
# a.greet()

# import my_package.my_model1
# import my_package.my_model2
#
# my_package.my_model1.info_print1()
# my_package.my_model2.info_print2()


# from my_package import my_model1
# from my_package import my_model2
# my_model1.info_print1()
# my_model2.info_print2()

from my_package.my_model1 import info_print1
from my_package.my_model2 import info_print2
info_print1()
info_print2()