# N = int(input())
# N_list = list(map(int,input().split()))
# V= int(input())
# print(N_list.count(V))


N = int(input())
N_list = list(map(int,input().split()))
V= int(input())
count=0


for i in N_list:
    if i==V:
        count+=1

    print(count)
        
    

   