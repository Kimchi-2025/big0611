# import diet

# diet.get_recommend_weight(160,False)
# diet.print_valid_menu()

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def take_damage(self, damage):
        self.hp -= damage
        print(f'{self.name}이 {damage}의 데미지를 입었습니다.')
        print(f'현재 hp는 {self.hp}입니다.')

player = Character('user1', 100)
player.take_damage(30)

print(player.name)

# from diet import get_recommend_weight
# import math
# import numpy as np

# get_recommend_weight(170)

# ln = np.log(0.1)

# print(ln)

# e = np.exp(ln)

# print(e)