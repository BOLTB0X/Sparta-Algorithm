top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    answer=[0]*len(heights)
    while heights:
        tmp=heights.pop()
        for idx in range(len(heights)-1,-1,-1): #거꾸로 돌려라
            if heights[idx]>tmp:
                answer[len(heights)]=idx+1 
                break #전파가 도달하는 인덱스를 찾았으니
    return answer
print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

#시간 복잡도 O(N^2)