
def outer(func):
    def inner():
        print("go to sleep")
        func()
        print("play the game")
    return inner

@outer
def sleep():
    import random
    import time
    print("slepping~~~~~~~~")
    time.sleep(random.randint(1,5))

# fn = outer(sleep)
# fn()
sleep()