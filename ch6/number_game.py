import random

tries = 1
guess = 0
answr = random.randint(1,100)

print("1부터 100까지 숫자중에 10번의 기회 안에 맞춰라")
while guess != answr:
    if tries>10:
        print("기회가 10번이 넘어갔습니다......")
        break
    print(tries,"번째")
    guess = int(input("숫자를 입력하세요:"))
    tries +=1
    if guess<answr:
        print("UP")
    elif guess>answr:
        print("DOWN")
if guess == answr:
    print(tries-1,"번째만에 정답")


