#y= 2x+3
# def 함수_이름(매개변수):
#     수행할_문장1
#     수행할_문장2
#     ...

#함수 이름 add, 입력으로 2개의 값을 받아서 입력값의 합을 출력
# def add(a,b):
#     #result=a+b
#     #return result
#     return a + b
#매개변수->함수에 입력으로 전달된 값을 받는 변수

# a=3
# b=4
# #add(3,4)의 리턴값을 c에 대입
# #a,b 는 인수->함수를 호출할 때 전달하는 입력값
# c=add(a,b)
# print(c)

# def say():
#     return "Hi"

# a=say()
# #리턴값을 받을 변수=함수이름()

# #리턴값이 없는 함수
# def add(a,b):
#     print("%d,%d의 합은 %d입니다."%(a,b,a+b))

# add(3,4)
# #함수이름(입력인수1,입력인수2, ...)
# a=add(3,4)
# print(a)
# #입력값이 몇 개가 될지 모를때
#def 함수_이름(*매개변수):
#    수행할_문장
#    ...

#여러 개의 입력값을 받는 함수
#여러 개의 입력값을 모두 더하는 함수
#여러 개의 입력값을 모두 더하기,곱하기 수행하는 함수
# def add_many(*args):
#     result=0
#     for i in args:
#         result += i
#     return result    

# result=add_many(1,2,3)
# print(result)
# result=add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)




def add_many(choice,*args):
    if choice =="add":
     result=0
     for i in args:
        result += i
    elif choice == "mul": 
       result=1
       for i in args:
            result*=i
    return  result
       
# #더하기
result=add_many('add',1,2,3)
print(result)
# #곱하기
result=add_many('mul',1,2,3,4,5,6,7,8,9,10)
print(result)
