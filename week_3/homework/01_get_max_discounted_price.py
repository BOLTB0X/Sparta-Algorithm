shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def get_max_discounted_price(prices, coupons):
    prices.sort(reverse = True)
    coupons.sort(reverse = True)
    answer=0
    check=0
    for i in range(len(coupons)):
        tmp=int(((100 - coupons[i]) / 100)* prices[i])
        check+=1
        answer+=tmp
    if len(prices)!=check:
        for i in range(check,len(prices)):
            answer+=prices[i]
    return answer

print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.