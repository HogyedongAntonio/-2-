# # def 함수(a, b) :
# #     print(a + b)

# # 함수("안녕", 3)

# #오류 이유: 안녕 과 3을 더할순 없잖아???? 상식적으로 생각해보자 그치그치
# #a와b 를 더해야 하지만 결과를 보면 오류가 난다.
# #아마 3에 ""를 안붙여서 인듯? 다시해보면


# def 함수(a,b):
#     print(a+b)

# 함수("안녕","3")

# #역시 내말이 맞았어 ㅋ

# #지금까지 2번이였습니다.





# def message():
#     print("A")
#     print("B")

# message()
# print("C")
# message()
# #이미 돌려버려서 예측은 커녕 답지보고 베끼는 수준 ㅜㅜ
# #이제 def 에 대해 이해한 것 같다.
# # 이해한 것에 대해 설명해보자면, 예를 들어 
# def 상운():
#    print("잘생김")
#    print("진짜로")

# print("상운이는")
# 상운()

#이러면 상운이는
#       잘생김
#       진짜로
#이렇게 출력된다. 신기할것 까진 없고 약간 이정도 까진 아~ 당연하지~ 이런느낌?

#이상 1번 클리어.


# def print_score(score_list):
#     print(sum(score_list)/len(score_list))
    
# print_score([1,2,3])

# def make_url(site):
#     print("www."+(site)+".com")

# make_url("naver")

# def make_url(site):
#     return "www." + site + ".com"

# answer=make_url("naver")
# print(answer)

A,B=(input().split())
print(A,B)

amola1=int(A[::-1])
amola2=int(B[::-1])

if amola1 > amola2:
    print(amola1)
else:
    print(amola2)
    