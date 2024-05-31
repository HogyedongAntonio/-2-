
import random #랜덤 생성
rockpaperscissors=["가위","바위","보"]
print("가위,바위,보 중 하나를 입력해주세요.")


def game(me,com): #함수생성?
    if me == com:
        return "비겼습니다."
    elif (me=="가위" and com=="보"):
         (me=="바위" and com=="가위")
         (me=="보" and com=="바위")
         return "이겼습니다!"
    else:
        return"졌습니다ㅠㅠ"#여기서 print 말고 return을 쓰는 이유.print를 쓰면 함수값이 반환?되지않음
#.........
   

