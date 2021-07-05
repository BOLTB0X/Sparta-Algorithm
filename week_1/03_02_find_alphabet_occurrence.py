def find_max_occurred_alphabet(string):
    alphabet_occurence_array=[0]*26 #알파벳 빈도수를 담는 배열

    for char in string:
        if not char.isalpha(): #만약 알파벳이 아니라면
            continue
        arr_idx=ord(char) - ord('a') #아스키 코드를 이용하여 인덱스를 구함
        alphabet_occurence_array[arr_idx] += 1 #그 인덱스에 맞는 알파벳 카운트

        #이제 알파벳별 빈도수 체크
        max_occurrence = 0
        max_alphabet_index = 0
        for i in range(len(alphabet_occurence_array)):
            alphabet_occurrence=alphabet_occurence_array[i] #알파벳 빈도
            if alphabet_occurrence > max_occurrence:
                max_occurrence = alphabet_occurrence
                max_alphabet_index=i #최빈 알파벳 인덱스 교체
    return chr(max_alphabet_index+ord('a'))
    
result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))
