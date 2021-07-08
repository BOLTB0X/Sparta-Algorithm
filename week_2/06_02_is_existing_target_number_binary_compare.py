finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#업다운 게임 개념 이용
#    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 1. 최소                  시도                              최대
# 2.

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

##순차 탐색
def is_existing_target_number_sequential(target, array):
    find_count=0
    for number in array:
        if target == number:
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True

def is_existing_target_number_binary(target, array):
    current_min=0
    current_max=len(array)-1
    current_guess = (current_min+current_max)

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min=current_guess+1
        else:
            current_max=current_guess-1
        current_guess=(current_max+current_min)//2
   
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)