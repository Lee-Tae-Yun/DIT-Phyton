#더하기 함수
def add(a,b):
    c=a+b
    return c
#빼기 함수
def minus(a,b):
    c=a-b
    return c
#곱하기 함수
def mulit(a,b):
    c=a*b
    return c
#나누기 함수
def divide(a,b):
    c=a/b
    return c

print("1 = +","2 = -","3 = *","4 = /","5 = END")
i = input()
while True:    
    if i == "1":
        print("더하기")
        a = int(input("첫번째 숫자? "))
        b = int(input("두번째 숫자? "))
        result = add(a,b)
        print("result =",result)
        print("1 = +","2 = -","3 = *","4 = /","5 = END")
        i = input()
    elif i == "2":
        print("빼기")
        a = int(input("첫번째 숫자? "))
        b = int(input("두번째 숫자? "))
        result = minus(a,b)
        print("result =",result)
        print("1 = +","2 = -","3 = *","4 = /","5 = END")
        i = input()
    elif i == "3":
        print("곱하기")
        a = int(input("첫번째 숫자? "))
        b = int(input("두번째 숫자? "))
        result = mulit(a,b)
        print("result =",result)
        print("1 = +","2 = -","3 = *","4 = /","5 = END")
        i = input()

    elif i == "4":
        print("나누기")
        a = int(input("첫번째 숫자? "))
        b = int(input("두번째 숫자? "))
        result = divide(a,b)
        print("result =",result)
        print("1 = +","2 = -","3 = *","4 = /","5 = END")
        i = input()

    else:
        print("END")
        break

