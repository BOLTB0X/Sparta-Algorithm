import math

# def is_prime_number(n):
#     for i in range(2,int(math.sqrt(n))+1):
#         if n % i ==0:
#             return False
#         return True
# def find_prime_list_under_number(number):
#     answer=[]
#     for i in range(1,number+1):
#         if 1<i<=3:
#             answer.append(i)
#         elif is_prime_number(i):
#             answer.append(i)
#     return answer

input = 20

#1차 해결
def find_prime_list_under_number(number):
    prime_list=[]
    for n in range(2,number+1): #n의 범위
        # n=19
        # i=2,3,5,7....
        # 2 -> X / 3 -> X / 6 -> X
        for i in prime_list:
            if n % i == 0 and i*i<=n:
                break
        else:
            prime_list.append(n)
    return prime_list

#2차 해결
#소수는 자기 자신과 1외 에는 아무것도 나눌 수없음
#주어진 자연수 N이 소수이기 위한 필요충분 조건
#N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
#범위는 제곱근이 n보다 작거나 같을때 까지만 확인하면 됨


result = find_prime_list_under_number(input)
print(result)

result = find_prime_list_under_number(input)
print(result)