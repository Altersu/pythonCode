class Father( object):
    def __init__(self):
        self.gender = 'male'

    def walk(self):
        print('I can walk')

    def eat(self):
        print('I can eat')

class Son(Father):
    pass

s = Son()
print(s.gender)
s.walk()
s.eat()