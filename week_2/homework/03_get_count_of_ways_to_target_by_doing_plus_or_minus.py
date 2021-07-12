numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    answer=[0]
    for i in array:
        tmp=[]
        for j in answer:
            tmp.append(j+i)
            tmp.append(j-i)
        answer=tmp
    return answer.count(target)
    
print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))

#답안
numbers = [2, 3, 1]
target_number = 0
result = [] # 모든 경우의 수를 담기 위한 배열
def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(array): # 탈출조건!
        all_ways.append(current_sum) # 마지막 인덱스에 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index], all_ways)
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index], all_ways)

get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result)
print(result)

##수정 답안
numbers = [2, 3, 1]
target_number = 0
result_count = 0 # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(array): # 탈출조건!
        if current_sum == target:
            global result_count
            result_count += 1 # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
current_sum + array[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
current_sum - array[current_index])

get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
print(result_count) # 2가 반환됩니다!
