# num=int(input())


# for j in range(num):
#     hahaha=(input())
#     print(hahaha[0]+hahaha[-1])

# number=int(input())
# def num(number):
#     for j in range(number):
#         word=input()
#         return word[0] + word[-1]
   

# num(number)


    
# n=31
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(i*2-1))
# for j in range(n-1,0,-1):
#     print(" "*(n-j)+"*"*(j*2-1))    



# n=int(input())

# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(i*2-1))
# for j in range(1,n+1):
#     print(" "*(n-j)+"*"*(j*2-1))        


# def print_arithmetic_operation(a,b,op):
#     print(a,"+",b,"=",a+b)
#     print(a,"-",b,"=",a-b)
#     print(a,"*",b,"=",a*b)
#     print(a,"/",b,"=",a/b)
# print_arithmetic_operation(3,4,op)

# N=int(input())
# X=int(input()) ->
N,X=map(int,input().split())
#map(값의 타입, 적용할 값)
A=list(map(int,input().split()))
for i in A:
    if i<X:
        print(i)
       


