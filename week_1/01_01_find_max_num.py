#내 풀이
def find_max_num(array):
    # 이 부분을 채워보세요!
    max=0
    for arr in array:
        if (max<arr):
            max=arr
    return max
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

#풀이1
def find_max_num(array):
    for num in array: 
        for compare_num in array: #비교대상을 잡기 위한 for문
            if num < compare_num:
                break
        else:
            return num