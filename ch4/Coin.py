money = int(input("교환할 돈은 얼마? :"))
m500 = money%500
m100 = m500%100
m50 = m100%50
m10 = m50%10

print("500원짜리 :",money//500)
print("100원짜리 :",m500//100)
print("50원짜리",m100//50)
print("10원짜리",m10//10)
print("바꾸지 못한 동전",m10%10)
