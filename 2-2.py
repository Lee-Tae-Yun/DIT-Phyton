
while True:
    a = (input("1st input? "))
    if a=="0000":
        break
    a=int(a)
    b = int(input("2nd input? "))
    print(type(a),type(b))
    result=a+b
    print(a,"+",b,"=",result)
    result=a-b
    print(a,"-",b,"=",result)
    result=a*b
    print(a,"*",b,"=",result)
    result=a/b
    print(a,"/",b,"=",result)
    result=a%b
    print(a,"%",b,"=",result)

print("exit")
