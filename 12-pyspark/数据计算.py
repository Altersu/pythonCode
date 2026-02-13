# # from pyspark import SparkConf,SparkContext
# # import os
# # os.environ['PYSPARK_PYTHON']="D:/software/Develop/Python314/python.exe"
# #
# # conf = SparkConf().setMaster("local[*]").setAppName("test")
# # sc = SparkContext(conf=conf)
# #
# # rdd = sc.parallelize([1,2,3,4,5,6])
# #
# # def func(data):
# #     return data *10
# # rdd2 =rdd.map(func)
# # print(rdd2.collect())
#
# """
# 演示RDD的map成员方法的使用
# """
#
# from pyspark import SparkConf, SparkContext
#
# import sys
# print("当前Driver Python:", sys.executable)
# print("当前Driver版本:", sys.version)
#
# import os
# os.environ['PYSPARK_PYTHON'] = r"D:/software/Code/PythonCode/python-learn/.venv/Scripts/python.exe"
# os.environ['PYSPARK_DRIVER_PYTHON'] = r"D:/software/Code/PythonCode/python-learn/.venv/Scripts/python.exe"
#
# # import os
# # os.environ['PYSPARK_PYTHON'] = "C:/Users/sumen/AppData/Local/Programs/Python/Python312/python.exe"
# # 开启更详细的 Python 崩溃信息
#
#
# conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# conf.set("spark.python.worker.faulthandler.enabled", "true")
# sc = SparkContext(conf=conf)
#
# # 准备一个RDD
# rdd = sc.parallelize([1, 2, 3, 4, 5])
# # 通过map方法将全部数据都乘以10
# # def func(data):
# #     return data * 10
#
# rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)
#
# print(rdd2.collect())
# # (T) -> U
# # (T) -> T
#
# # 链式调用
#
"""
Windows + PySpark + 虚拟环境模板
说明：
1. 必须在导入 pyspark 之前设置环境变量
2. Driver 和 Worker 使用同一个虚拟环境 Python
3. faulthandler 可以在 Worker crash 时显示详细 traceback
"""

# import os
#
# # 1️⃣ 设置 Python 路径（必须在导入 pyspark 前）
# os.environ['PYSPARK_PYTHON'] = r"C:/Users/sumen/AppData/Local/Programs/Python/Python312/python.exe"
# os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:/Users/sumen/AppData/Local/Programs/Python/Python312/python.exe"
#
# # 2️⃣ 导入 PySpark
# from pyspark import SparkConf, SparkContext
#
# conf = SparkConf() \
#     .setMaster("local[*]") \
#     .setAppName("test_pyspark") \
#     .set("spark.python.worker.faulthandler.enabled", "true")  # Worker crash 输出 traceback
#
# sc = SparkContext(conf=conf)
#
# # 3️⃣ 测试 RDD
# rdd = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)
# print(rdd2.collect())
#
# sc.stop()
# 文件名：test_pyspark.py
import os

# ===============================
# 1. 指定 PySpark 使用的 Python
# ===============================
python_path = r"C:/Users/sumen/AppData/Local/Programs/Python/Python312/python.exe"

os.environ['PYSPARK_PYTHON'] = python_path        # Worker Python
os.environ['PYSPARK_DRIVER_PYTHON'] = python_path # Driver Python

# ===============================
# 2. 导入 PySpark
# ===============================
from pyspark import SparkConf, SparkContext

# ===============================
# 3. 创建 SparkContext
# ===============================
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark") \
    .set("spark.python.worker.faulthandler.enabled", "true")  # 开启 worker crash traceback

sc = SparkContext(conf=conf)

# ===============================
# 4. 测试 RDD
# ===============================
try:
    rdd = sc.parallelize([1, 2, 3, 4, 5])
    rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)

    print("RDD结果:", rdd2.collect())

finally:
    sc.stop()  # 一定要关闭 SparkContext
