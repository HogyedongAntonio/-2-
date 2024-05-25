# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list)):
#     while i >= 0:
#         print(len(price_list) - 1 - i, price_list[i])
#         break



#숙제 3번

low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []  # 변동폭을 저장할 빈 리스트를 생성합니다.

i = 0
while i < len(low_prices):  # 리스트의 길이만큼 반복합니다.
    # 각 날의 변동폭을 계산하여 변동폭 리스트에 추가합니다.
    volatility.append(high_prices[i] - low_prices[i])
    i += 1

print(volatility)
