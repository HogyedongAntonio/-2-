#for 변수 in 리스트(또는 튜플,문자열):
# ....수행할 문장1
# ....수행할 문장2
#     ...
# list=['one','two','three']

for i in list:
    print(i)


a=[(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first)
    print(last)

#5명의 학생 시험 점수를 리스트로 받아서, 60점이상이면 합격
#else 불합격 출력

# score=[90,25,67,45,60]
# for i in score:

#     if i>=60:
#         print('합격')
#     else:
#         print('불합격')

# num=0
# score=[90,25,67,45,60]
# for i in score:
#     num += 1
#     if i>=60:
#         print('%d번 학생 합격'%num )
#     else:
#         print('%d번 학생 불합격'%num)


# num=0
# score=[90,25,67,45,60]
# for i in score:
#     num += 1
#     if i<60:
#        continue

#     print('%d번 학생 합격'%num)

#for 변수 in range(시작_숫자, 끝_숫자)
#range(0,10) 0,1,2,3.....9
#range(10) -> range(0,10)
#range(1,11)->1~10

#1~10까지 더하는 코드
add=0
for i in range(1,11):
    add=add+i
print(add)    

i=0
score=[90,25,67,45,60]
for i in range(len(score)):
    if score[i]<60:
       continue

    print('%d번 학생 합격' %(i+1))

#리스트 컴프리핸션
#리스트 a의 각 항목에 3 곱한 결과를 result 리스트에 담기
a=[1,2,3,4]
#리스트에 추가 -> append
#리스트.append(추가할 값)
result=[num*3 for num in a]#=result=[]
# for num in a:
#     result.append(num*3)

# print(result)
print(result)
result=[num*3 for num in a if num%2==0]# 짝수만 출력
