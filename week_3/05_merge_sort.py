array = [5, 3, 2, 1, 6, 8, 7, 4]

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid] #왼쪽 배열 생성
    right_array = array[mid:] #오른쪽 배열 생성
    print(array)
    print('left_arary', left_array)
    print('right_arary', right_array)
    return merge(merge_sort(left_array), merge_sort(right_array))

def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result

print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
# 시간 복잡도: O(NlogN)