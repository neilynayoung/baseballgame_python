import random

# 정답을 먼저 랜덤으로 생성하기
answer = random.randint(1,100)
print("정답=", answer)

# 초기화
num = 0 #초기값
count = 0 #시도횟수 초기값

# 게임 시작멘트
print("1~100까지 숫자 up&down 게임을 시작합니다!")

# 게임 진행
while answer != num:  #같지않을동안 반복한다= 맞히면 빠져나온다
    num = int(input("1~100사이의 값을 입력하세요:"))   #입력값을 숫자로 받기 위해 int사용
    # 클경우, 작을경우, 같을경우 3가지있음. 같은경우는 while문에서 잡아주므로 생략
    if num > answer:
        print("더 작은 숫자를 입력하세요")
    else num < answer:
        print("더 큰 숫자를 입력하세요")
    count += 1

print("{}번만에 정답을 맞췄습니다.".format(count))




