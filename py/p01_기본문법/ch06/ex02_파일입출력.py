# f = open('test.txt', 'w')
# f.write('A B C D E F G\n')
# f.write('A B C D E F G\n')
# f.write('A B C D E F G\n')
# f.close()

# f = open('test.txt', 'a')
# f.write('Z Y Z\n')
# f.close()

# f = open('test.txt', 'r')
# print(f.read())
# f.close()

# f = open('test.txt', 'r')
# lines = f.readlines()
# print(lines)
# print(len(lines))
# line = [x.strip() for x in lines]
# print(type(line))
# print(line)
# print(' '.join(line))
# f.close()

# print('{1:,} 첫번째 값 {0} 두 번째 값'.format(1, 2000000))

# with open("일기.txt", 'w') as f:
#     f.write("2020년 3월 12일 금요일\n")
#     f.write("날씨: 맑음\n")
#     f.write("행복하자!!!\n")

# with open("일기.txt") as f:
#     print(f.read())

# with open("일기.txt", "r") as f:
#     lines = f.readlines()

#     for line in lines:
#         print(line)

for n in [1, 2, 4, 12, 365, 1000, 10000, 100000, 1000000]:
    x = 50*(1 + (1/n))**n
    print(x)
    