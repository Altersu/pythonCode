# def hello():
#     print("Hello from a.py")
#
# print("a.py:", __name__)
#
# if __name__ == '__main__':
#     print("a.py is being run directly")

# def greet():
#     print("Hello from example.py")
#
# print("example.py __name__ =", __name__)
#
# if __name__ == "__main__":
#     print("example.py is running directly")
#     greet()


print("a.py 顶层代码执行")
def greet():
    print("Hello from a.py")
print("a.py:", __name__)

if __name__ == "__main__":
    print("a.py 是主程序，直接运行")
    greet()
