input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for n in array: #array 길이만큼 연산
        if n==number: #1번 연산
            return True
    return False

result = is_number_exist(9, input)
print(result)