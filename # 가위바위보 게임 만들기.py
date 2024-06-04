list=["가위","바위","보"]
import random
vic=0
defeat=0
draw=0

while True:
    user=input("가위,바위,보 중 하나를 입력하세요: ")
    if user not in list:
        print("잘못 냈습니다")
        continue
    computer=random.choice(list)
    print(f"컴퓨터: {computer}")
    if user == computer:
        draw += 1
        print("비겼습니다.")
    elif (user == "가위" and computer == "보")or\
    (user == "바위" and computer == "가위")or\
    (user == "보" and computer == "바위"):
        vic += 1
        print("이겼습니다.")

    else:
        defeat += 1
        print("졌습니다.")



    while True:
        restart=input("게임을 계속하시겠습니까?(Y/N)")
        if restart =="Y":
            break
        elif restart =="N":
            print("종료시마스")
            print(f"{vic}승 {defeat}패 {draw}무")
            exit()
        else:
            print("잘못된 입력입니다.")


