# with open('test.txt', 'a+') as f:
#     f.write('123456\n')
#     f.seek(0)
#     print(f.read())

# with open('test.txt', 'r') as f:
#     print(f.read())

# import os

# fileName = 'test.txt'
# cwd = os.path.join(os.getcwd(), fileName)
# print(cwd)
# if os.path.exists(fileName):
#     print(f'{fileName} 파일을 찾았습니다.')
#     os.remove(fileName)
# else:
#     print(f'{fileName} 파일이 존재하지 않습니다.')

# print('나는 %s %d개를 먹었다' % ('사과', 1000000))

# text = "나는 자랑스러운 태극기 앞에 자유롭고 정의로운 대한민국의 무궁한 영광을 위하여 충성을 다할 것을 굳게 다짐합니다."

# print(text)
# print(text.split(" "))

# text = "+82-10-1234-5678"
# print(text.split('-',3))

# text = "\n\n\n\n토실토실 아기 돼지\n\n\n\n"
# print(text)
# print(text.strip('\n'))

# text = "Apple"
# print(f'{text:<10}칸 띄우기')
# print(f'{text:>10}칸 띄우기')
# print(f'{text:^10}칸 띄우기')
# print(f'{text:-^11}칸 띄우기')

# digit = 1
# digit =f'{digit:0>4}'
# print(digit)

# pi = 3.141592
# money = 1250000

# print(f'{pi:>10.2f}')
# print(f'{money:>20}')

# print('0123456789 : 12345')
# print('%-10s : %5d' % ('apple', 1500))
# print('%-10s : %5d' % ('banana', 2500))
# print('%-10s : %5d' % ('mango', 13000))

# print('0123456789 : 12345')
# print(f"{'apple':<10} : {1500:>5}")

# print(f'{pi:.2f}')

# print('그는 \'안녕\'이라고 말했다')


# path = r"C:\Users\test\Documents"
# print(path)

print("C:\\Users\\test\\Documents")
print(r"C:\Users\test\Documents")
print("C:/Users/test/Documents")
