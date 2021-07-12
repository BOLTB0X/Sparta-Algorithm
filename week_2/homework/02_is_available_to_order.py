shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]
#1차 시도 코드
def is_available_to_order(menus, orders):
    for order in orders:
        if not order in menus:
            return False
    return True

result = is_available_to_order(shop_menus, shop_orders)
print(result)

#답안코드 정렬이용
def is_available_to_order(menus, orders):
    menus.sort() # menus 정렬! 
    for order in orders: #주문서 원소 하나씩 확인
        if not is_existing_target_number_binary(order, menus): #함수 호출
            return False
    return True

def is_existing_target_number_binary(target,array): #이진탐색 이용
    current_min=0
    current_max=len(array)-1
    current_guess=(current_min+current_max)//2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
            current_guess = (current_min + current_max) // 2
    return False