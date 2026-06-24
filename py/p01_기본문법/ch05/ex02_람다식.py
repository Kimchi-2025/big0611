# weight = lambda height: (height - 100) * 0.9
# print(weight(170))

weight2 = lambda height, man=True: (height-100)*0.9 if man else (height-100)*0.85
print(weight2(170))

def weight_value2(man, height):
    if man:
        weight = (height-100)*0.9
    else:
        weight = (height-100)*0.85
    
    return weight

print(weight_value2(True, 170))

x = weight_value2
print("x함수: ", x(True, 170))