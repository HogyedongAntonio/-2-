# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list)):
#         print(len(price_list) - 1 - i, price_list[i])

#         break
# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list)):
#     while i >= 0:
#         print(len(price_list)-1-i, price_list[i])

#         break
    

# for i in range(3):
#     j=0
#     while j<2-i:
#         print(' ',end='')
#         j+=1
#     j=0
#     while j<=i:
#             print('*',end='')
#             j+=1              
# print()       
# ????????????? 난 왜안돼???????????????????????
#숙제 2번



# low_prices = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]

# volatility = []

# for i in range(len(low_prices)):
#     j=0
#     while j<=i:
#         volatility.append(high_prices[i]-low_prices[i])
#         j+=1
    
# print(volatility)        



# i=0
# while i<3:
    
#     print(' ',end='')
#     j=0
#     while i >j-1:
#         print('*',end='')
#         i+=1
#         j+=1
# print() #내가푼거

# i=0
# while i<3:
#     j=3
#     while j>=0:
#         if(j>i):
#             print(' ',end='')
#         else:
#             print('*',end='')
#         j-=1
#     i+=1
#     print()      


# for i in range(3):
#     for j in range(3,-1,-1):
#         if j>i:
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print()


               
        


   
# price_list = [32100, 32150, 32000, 32500]
# i=0
# while i<len(price_list):
#     print(len(price_list)-1-i,price_list[i])
#     i+=1






# low_prices = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]

# volatility = []

# for i in range(len(low_prices)):
#         volatility.append(high_prices[i]-low_prices[i])
            

# print(volatility)

  
# low_prices = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]

# volatility = []

# i=0
# while i<len(low_prices):
#     volatility.append(high_prices[i]-low_prices[i] )
#     i+=1
# print(volatility)    

# list = ['intra.h', 'intra.c', 'defin.h', 'run.py']

# for i in list:
#     split=i.split(".")
#     # print(split)
#     # print(split[1])
#     if split[1] =="h" or split[1] =="c":
#         print(i)

# list = ['intra.h', 'intra.c', 'defin.h', 'run.py']

# i=0
# while i<len(list):
#     split=list[i].split(".")
#     if split[1]=="h" or split[1]=="c":
#         print(list[i])
#     i+=1    
    


# ""
# cacaca=[]
#i=0
#if 1<=i<=30
#print(cacaca.append[i]
print("숫자 추측 게임")
print("==========================")
small=int(input("최소값을 입력해주세요:"))
big=int(input("최대값을 입력해주세요:"))

attemps_limit=5
import random
random_num= random.randint(small,big)
print(f"{small}와{big}사이의 숫자를 {attemps_limit}회 안에 맞춰보세요!")
#추측 횟수
attemps = 0
while attemps<attemps_limit:
    #추측 횟수동안 사용자로부터 추측한 숫자 입력받음
    guess=int(input("추측한 숫자를 입력하세요:"))
    attemps+=1
    if guess<random_num:
        print("너무 작습니다")
    elif guess>random_num:
        print("너무 높습니다")
    else:
        print(f"축하합니다! {attemps}회 만에 맞혔습니다")
        break

if guess != random_num:
    print(f"실패! 정답은 {random_num}이었습니다~")  
print("게임 종료")      