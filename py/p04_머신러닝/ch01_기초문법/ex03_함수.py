def calculator(x,y,op):
    err = 0
    result = 0

    try:
        if op == '+':
            result = x + y
        elif op == '-':
            result = x - y
        elif op == '*':
            result = x * y
        elif op == '/':
            if y != 0:
                result = x / y
        else:
            err = -1
            print('계산 실패')

        return err, result

    except:
        print('에러 발생')
        err = -1
        return err, result

print(calculator(5,2, '/'))


