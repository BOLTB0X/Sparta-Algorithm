input = "011110"
#내 풀이
#모두 1으로 만드는 방범 최소로 뒤집는다
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    cnt_1_trans=0 #0->1 
    cnt_0_trans=0 #1->0

    #연속된 것을 한번에 뒤집어야 하므로 문자열 첫번째를 잡는다.
    if string[0]=='1':
        cnt_0_trans += 1
    else:
        cnt_1_trans += 1

    for i in range(1,len(string)):
        if string[i-1] !=string[i]: #앞 뒤 문자열이 다른 경우
            if string[i]=='1': #뒤 문자열이 1인 경우
                cnt_0_trans+=1
            else: #뒤 문자열이 0인 경우
                cnt_1_trans+=1
    return min(cnt_0_trans,cnt_1_trans)

#답안 코드
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)