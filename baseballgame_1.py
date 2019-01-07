import random

#랜덤으로 정답 생성
answer = random.randint(1,100)
print("정답은=", answer)

# 초기화
num = 0
count = 0

# 게임 진행
while answer !=num:
    num = int(input("1~100중에 한 숫자를 입력하세요:"))
    if answer < num:
        print("더 작은 값을 입력하세요")
    elif answer > num:
        print("더 큰 값을 입력하세요")
    count +=1

print ("{}번 만에 정답을 맞췄습니다.".format(count))



