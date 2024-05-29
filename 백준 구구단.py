Q=input(int())
for i in range(0,9):#1부터 시작되야되서 범위를 0으로 설정한 대신에 +1을 붙임.
    print(int(Q),"*",i+1,"=",(int(Q)*(i+1)))#그냥Q로만 쓰면 출력이 이상하게 됨.ex.Q*(Q+1)=QQQQQQQQQQQ 이런식으로. int로 감싸니까 정상적으로 출력됨.
