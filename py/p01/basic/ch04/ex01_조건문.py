weather = '맑음'
today_temp = -20

if weather == '맑음':
    if today_temp > 0:
        print('아이스 아메리카노')
    elif today_temp == 0:
        print('미지근한 아메리카노')
    else:
        print('따뜻한 아메리카노')
else:
    print('카푸치노')


eng = 75
math = 50

if eng >= 90 or math >= 90:
    print('용돈 인상')
elif eng >= 80 or math >= 80:
    print('동결')
else:
    print('용돈 삭감')

