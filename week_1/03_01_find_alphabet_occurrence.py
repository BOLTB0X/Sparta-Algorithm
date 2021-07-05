def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    
    max_occurrence=0 #최빈 변수
    max_alphabet=alphabet_array[0] #가장 많이 나온 알파벳

    for alphabet in alphabet_array:
        occurrence=0 #각 알파벳 배열이 바뀔때 마다 0으로 초기화
        for char in string:
            if alphabet == char:
                occurrence += 1
        
        if max_occurrence < occurrence: #최대 빈도수 보다 큰 빈도수가 생기면
            max_occurrence=occurrence 
            max_alphabet=alphabet
    return max_alphabet

result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))
