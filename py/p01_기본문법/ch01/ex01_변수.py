# 변수
# 5를 a에 할당(대입)
# =는 대입 연산자
# ==(같다)
# alt + 위아래방향키
a = 5
if a == 5:
    print(a, "Same")
else:
    print(a, "different")

b = (lambda x: x+5)
print(b(10))

weight = lambda height: (height-100)*0.9
print(weight(175))

weight2 = lambda man, height: (height-100) if man == "man" else (height-100)*0.9
print(weight2("man", 175))

temp = lambda tf,a,b,c,d: a+b+c+d if tf else a*b*c*d
print("True", temp(True, 10,20,30,40))
print("False", temp(False, 10,20,30,40))

temp = lambda *args: sum(args)
print(temp(1,1,1,1,1,1,1))

temp = lambda a,b,c="fixed": f"city: {a}\nlocation: {b}\nlast: {c}"
print(temp("a", 10))

names = ["kim", "lee", "park"]
print([map(lambda x: x.upper(), names)])

names = [x.upper() for x in names]
print(names)

num = [1,2,-1,-2,3,4,5]
result = list(filter(lambda x: x>0, num))
print(num)
print(result)

result = [x for x in num if x>0]
print(result)
result = [x if x>0 else x*(-1) for x in num]
print(result)

x, y, z = "사과", "바나나", 10
print(x,y,z)

result = [1 if x>0 else 0 for x in num]
print(result)

result = list(map(lambda x: 1 if x>0 else 0, num))
print(result)

a = 1_000_000_000
print(int(a))

result1, result2 = zip(*map(lambda x: (x, x*2), num))
print(list(result1))
print(result2)

names = ['kim', 'lee', 'park']
ages = [20,30,40]
result = zip(names, ages)
print(list(result))

result = [list(x) for x in zip(names, ages)]
print(result)


for name, age in zip(names, ages):
    print(name, age)

result = dict(zip(names, ages))
print(result['lee'])

