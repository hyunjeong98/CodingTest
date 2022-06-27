n, k = map(int, input().split())
coin_list = []
coin_count = 0

for i in range(n):
    coin_list.append(int(input()))

for coin in coin_list[::-1]:
    if k == 0:
        break
    if coin <= k:
        coin_count += k // coin
        k = k % coin

print(coin_count)