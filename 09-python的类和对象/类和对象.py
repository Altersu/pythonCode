
class clock:
    name = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)


clock1 = clock()
clock1.name = '闹钟1'
clock1.price = 10
print(clock1.name,clock1.price)
clock1.ring()
