from collections import deque
c = 11
b = 2

#코니의 위치변화
#코니는 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리의 +1만큼

#그럼 브라운의 위치?
# B-1, B+1, 2*B

#모든 겅우의 수를 나열해야함 ==> BFS
#시간+1
#위치는 자유자재로 증가
#규칙적 -> 배열, 자유자재-> 딕셔너리

def catch_me(cony_loc, brown_loc):
    time=0
    queue=deque()
    queue.append((brown_loc,0))
    visited=[{} for _ in range(200001)] #위치마다 브라운이 방문한 시간을 적기 위해 배열 안에 딕셔너리를 넣음
    #각 visited[위치][시간]

    while cony_loc < 200000:
        cony_loc +=time #시간만큼
        
        if time in visited[cony_loc]:
            return time

        for i in range(0,len(queue)):
            current_position,current_time=queue.popleft()

            new_position = current_position - 1
            new_time = current_time + 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
                
            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
        time += 1

print(catch_me(c, b)) # 5 출력
