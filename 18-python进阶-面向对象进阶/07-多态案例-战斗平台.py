# class HeroFighter:
#     def power(self):
#         return 60
# class AdvHeroFighter(HeroFighter):
#     def power(self):
#         return 80
# class EnemyFighter:
#     def power(self):
#         return 70
#
# if __name__ == '__main__':
#     h1 = HeroFighter()
#     h2 = AdvHeroFighter()
#     e1 = EnemyFighter()
#
#     if h1.power() >= e1.power():
#        print('Hero win')
#     else:
#         print('Enemy win')
#
#     print('-'* 36)
#
#     if h2.power() >= e1.power():
#        print('Hero win')
#     else:
#         print('Enemy win')

class HeroFighter:
    def power(self):
        return 60
class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80
class EnemyFighter:
    def power(self):
        return 70

def fight(hero,enemy):
    if hero.power()>=enemy.power():
        print('Hero win')
    else:
        print('Enemy win')

if __name__ == '__main__':
    h1 = HeroFighter()
    h2 = AdvHeroFighter()
    e1 = EnemyFighter()
    fight(h1,e1)
    fight(h2,e1)
    # fight(h1,h2)

