#거스름돈 1460(n)원을 거슬러주는 프로그램

n = 1460       # 거스름돈(n)
count = 0      # 동전의 개수
result = 0     # 동전의 최소 개수
coins = [500,100,50,10]  # 동전의 종류
for coin in coins:
    count += n // coin   # count = count + n//coin(몫)
    result += n // coin
    n %= coin            # 거스름돈(n)을 coin으로 나눈 나머지를 다시 저장
    print("{}원 {}개".format(coin,count))
    count = 0     
print("최소 값:%d개" %result)