finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#업다운 게임 개념 이용
#    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 1. 최소                 시도                           최대
# 2.                         최소        시도            최대
# 3.                                        최소 시도    최대

def is_existing_target_number_binary(target, array):
    current_min=0
    current_max=len(array)-1
    current_guess=(current_max+current_min)//2 #추측값

    while current_min<=current_max:
        if current_guess==target:
            return True
        elif current_guess<target:
            current_min=current_guess+1 #추측값이 타겟보다 작다면
        else:
            current_max=current_guess-1 #추측값이 타켓보다 크다면
        current_guess=(current_min+current_max)//2
        
    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)