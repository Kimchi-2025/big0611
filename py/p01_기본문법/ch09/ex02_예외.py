# def get_valid_age():
#     num = 0
#     while True:
#         num += 1
#         try:
#             age = int(input('나이를 입력하세요: '))

#             if age < 0:
#                 print('나이는 0 이상이어야 합니다.')
#             elif age > 130:
#                 print('유효하지 않은 나이입니다.')
#             else:
#                 return age

#         except ValueError as e:
#             print('숫자만 입력해 주세요.')
#         except e:
#             print('예외 발생! 다시 나이를 입력해 주세요.')
#             print('에러 메세지')
#             print(e)
        
#         print(f'{num}차 재시도')

# age = get_valid_age()
# print(f'{age}세 입니다')

import math
# print(math.e)
# print(math.e**0)

# base = 2
# for i in [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]:
#     result = (base**i-1)/i
#     print(result)

# print(math.log(base))

print(2**6)
print((2**2)*(2**3))
print((2**2)**3)