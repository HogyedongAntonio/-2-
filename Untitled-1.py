# #while
# while 조건문:
#     수행할 문장1
#     수행할 문장2
#     수행할 문장3
#     ...
#조건문이 참인 동안 계속 반복!

#'열 번 찍어 안 넘어가는 나무 없다'

# treehit=0
# while treehit<10:
#     treehit=treehit+1
#     print("나무를 %d번 찍었습니다."%treehit)
#     if treehit==10:
#         print("나무 넘어갑니다.")


#while문 안에서 숫자 입력
#입력받은 숫자가 3이면 while문 중지
# num=0
# while num!=3:
#     num=int(input())


#while문 강제로 빠져나가기
#커피 자판기
#남은 커피양
coffee=10
#money=300
# while money:# 계속 반복
#     print("돈을 받았습니다. 커피를 줍니다")
#     coffee=coffee-1
#     print("남은 커피의 양은 %d개입니다."%coffee)
#     if coffee ==0:
#         print("커피가 다 떨어졌습니다. 판매중지")
#         break
# while True:
#     money=int(input("돈을 넣어 주세요:"))
#     if money ==300:
#         print("커피를 준다")
#         coffee=coffee-1
#     elif money>300:
#         coffee=coffee-1
#         print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
#         print("남은 커피의 양은 %d개" %coffee)
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않는다.")
#         print("남은 커피의 양은 %d개" %coffee)
#     if coffee ==0:
#         print("커피가 다 떨어졌습니다. 판매 중지")
#         break


#while문 처음으로 돌아가기
#1~10까지 수 중에 홀수만 출력하기
a=0
while a<10:
    a=a+1
    if a%2==0:
        continue
    print(a)