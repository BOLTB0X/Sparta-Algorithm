def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

print("정답 = [3, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =", find_alphabet_occurrence_array("Hello my name is sparta"))
print("정답 = [2, 1, 2, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0] \n현재 풀이 값 =", find_alphabet_occurrence_array("Sparta coding club"))
print("정답 = [2, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 3, 3, 0, 0, 0, 0, 0, 0] \n현재 풀이 값 =", find_alphabet_occurrence_array("best of best sparta"))