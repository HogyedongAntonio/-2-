#12'
#너무 어려운 숙제. 현재시각 오후 11시 47분 젠장 난 졸리지만 숙제를 해내야돼

lotto=[]
print("상운이의 인생역전! 로또 추첨기!!")
print("============================")
count=0
import random
while True:
    randum_num=random.randint(1,45)
    
   
    if count>5:
        break
    if randum_num not in lotto:
       lotto.append(randum_num)
       count+=1
    #랜덤숫자값이 lotto 리스트에 없어야만 추가
    
lotto.sort()  
print(*lotto)




# a=int(input("첫 번째 정수 입력 >>"))
# b=int(input("두 번째 정수 입력>>"))
# c=int(input("배수 입력>>"))
# d= 0
# for i in range(a,b+1):
#     if i % c ==0:
#         d+=i #d= i+d
# print(f"{c}의 배수의 합: {d}")   

name=input("이름>> ")
code=input("주민번호>> ")
#년도,월,일,성별
year=code[:2]
month=code[2:4]
day=code[4:6]
gender=code[6]

if gender == "2" or gender =="4":
    gender="여자"
else: gender="남자"

print(f"{name}님은 {year}년 {month}월{day}일에 태어났고, 성별은{gender}입니다.")     


#1+2+3+1
#oooxo #a[1] a[2] #a[0] -> a[i]
# total=0
# a=input(":OX 입력>> ")
# b=0
# for i in range(len(a)):
#     if a[i] =="O":
#        b+=1
#        total += b
#     else:b=0    
        
# print(f"점수 : {total}점")

   









