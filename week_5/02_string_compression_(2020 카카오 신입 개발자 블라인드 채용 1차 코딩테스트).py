input = "abcabcabcabcdededededede"
#길이를 1? 2? 3?으로 잘라야 할지 결정
#반 이상을 자르면 반복될수가 없음
def string_compression(string):
    n=len(string)
    compression_length_array = [] # 1~len까지 압축했을때 길이 값

    for split_size in range(1,(n//2)+1):#문자열 압축이므로 n//2만큼 만 쪼개야함
        compressed = "" 
        #string 갯수 단위로 쪼개기
        splited=[
            string[i:i+split_size] for i in range(0,n,split_size)
        ]
        count = 1

        for j in range(1,len(splited)):
            prev,cur=splited[j - 1], splited[j]
            if prev == cur:
                count += 1
            else: #이전 문자와 다르다면
                if count > 1:
                    compressed += (str(count) + prev)
                else: # 문자가 반복되지 아늏아 한번만 나타난 경우 1은 생략함
                    compressed += prev
                count = 1 # 초기화
        
        if count > 1:
            compressed += (str(count) + splited[-1])
        else: # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
            compressed +=splited[-1]
        compression_length_array.append(len(compressed))
    return min(compression_length_array) #최솟값 리턴

print(string_compression(input))  # 14 가 출력되어야 합니다!