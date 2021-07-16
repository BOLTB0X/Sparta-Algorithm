input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}
# fibo(100) -> fibo(99) -> fibo(98) .... top down
# fibo(1) -> fibo(2) -> fibo(3) ... bottom down
def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    nth_fibo = fibo_dynamic_programming(n-1,fibo_memo) + fibo_dynamic_programming(n-2,fibo_memo)
    fibo_memo[n]=nth_fibo
    return nth_fibo

print(fibo_dynamic_programming(input, memo))