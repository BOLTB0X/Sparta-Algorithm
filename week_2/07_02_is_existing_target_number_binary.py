finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#시간 복잡도 분석
def is_exist_target_number_binary(target, numbers):
    find_count=0
    current_min=0
    current_max=len(finding_numbers)-1
    current_guess=(current_min+current_max)//2
    while current_min <= current_max: #1~N까지
        find_count+=1 #1번 탐색하면 반절이 줄어듬 즉 N/(2^find_count)
        if target == numbers[current_guess]:
            print("연산 횟수",find_count)
            return current_guess
        elif target > numbers[current_guess]:
            current_min=current_guess+1
        else:
            current_max=current_guess-1
        current_guess=(current_min+current_max)//2
        
    return False

# N/(2^find_count) ===> O(logN)

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)