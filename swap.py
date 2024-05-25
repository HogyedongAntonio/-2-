# # #swap
# # a=3
# # b=5
# # tmp=b
# # b=a
# # a=tmp
# # print(a)
# # print(b)

# # a=[1,2,4,5]
# # b=(1,2,4,5)
# # c=(1,2,4)
# # print(b[0])
# # print(b[1:])
# # print(b+c)
# # print(b*2)
# # b[0]=0 #X

# # '돈이 있으면 택시를 타고 가고, 돈이 없으면 걸어간다.'
# # money=True
# # if money:#돈이있다
# #     print("택시타세요")
# # else:#돈이없다
# #     print("걸어가세요")

# # if 조건문:
# #     수행할 문장1
# #     수행할 문장2
# # else:
# #     수행할 문장1
# #     수행할 문장2
# # x=3
# # y=2
# # x<y
# # x>y
# # print(x<y)
# # print(x>y)
# # print(x==y)
# # print(x!=y)
# # money= 5000
# # if money==5000:
# #     print("택시타세요")
# # else:
# #     print("걸어가세요")

# # x=True
# # y=False
# #and, or, not
# #and -> x랑 y가 모두 참이어야 참이다
# #or -> x랑 y 둘 중에 하나만 참이어도 참이다
# #not -> x가 거짓이면 참이다
# # print(x and y)
# # print(x or y)
# # print(not x)

# # money=5000
# # card=True
# # if money==5000 and not card:
# #     print("택시타세요")
# # else:
# #     print("걸어가세요")
# #in, not, in
# # x in 리스트, 튜플
# # x not in 리스트, 튜플

# # print(1 in[1,2,3])
# # print(1 in (1,2,3))
# # print(1 not in [1,2,3])
# # print('a' in ('a','b','c'))
# # print('j' not in 'python')
# # pocket=['paper','cellphone']
# # if 'money' in pocket:
# #     pass #개백수
# # else:
# #     print("카드꺼내")
# pocket=['paper','cellphone','money']
# card=True
# if 'money' in pocket:
#     print("미스터택시")
# else: #주머니에 돈이 없는 상황
#     if card:#주머니에 돈은 없지만 카드는 있음
#         print("미스터택시")
#     else:#주머니에 돈도 카드도 없음
#         print("걸어가기")
# #elif=> 다중 조건 판단 else-if
# pocket=['paper','cellphone','money']
# card=True
# if 'money' in pocket:
#     print("미스터택시")
# elif card:
#     print("미스터택시")
# else:
#     print("걸어가기")

# grade=int(input("성적 입력: "))
# if grade>=90:
#     print("A등급")
# elif grade>=80 and grade<90:
#     print("B등급")
# elif grade>=70 and grade<80:
#     print("C등급")
# else:
#     print("F등급")
#딕셔너리
#baseball=>야구
#{key, value}

dic={'name':'sangwoon','phone': '010-9983-2774','birth':'01312003'}
print(dic['name'])
print(dic['phone'])
a={1: 'a'} #a[key] = value
a[2] ='b'
print(a) 
a[3]=[1,2,3]

a={1:'a', 2:'b'}
print(a)
