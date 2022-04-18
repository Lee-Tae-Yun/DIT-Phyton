data = {
    "철수":98,
    "영희":80,
    "순이":100,
    "돌이":70
}
sum =0

for i,j in data.items():
    print(i,j)
    sum +=j
sum = int(sum/len(data))
print("=========")
print("평균",sum)

