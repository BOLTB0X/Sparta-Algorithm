finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#순차 탐색의 시간복잡도
def is_existing_target_number_sequential(target, array):
    found_count=0 #연산 횟수
    for number in array:
        found_count+=1
        if target == number:
            print("연산 횟수: ",found_count)
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True