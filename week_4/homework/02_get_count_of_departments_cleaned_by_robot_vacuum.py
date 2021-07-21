from collections import deque

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dx=[-1,0,1,0] # 하 상
dy=[0,1,0,-1] # 우 좌

#  0
# 3  1
#  2

def turn_dir(d):
    if d==0:
        return 3
    elif d==1:
        return 0
    elif d==2:
        return 1
    elif d==3:
        return 2

def turn_back(d): #방향 전환
    if d==0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    cnt=1
    room_map[r][c]
    que = deque([[r,c,d]])

    while que: # 큐가 빌때가지
        row,col,direction = que.popleft()
        tmp_direction=direction
        for i in range(4):
            tmp_direction = turn_dir(tmp_direction) #왼쪽방향부터 확인
            new_row=row+dx[tmp_direction]
            new_col=col+dy[tmp_direction]

            # 범위에 해당하고 청소하지 않았다면
            if  0 <= new_row < len(room_map[0]) and 0 <= new_col < len(room_map) and room_map[new_row][new_col] == 0:
                cnt+=1
                room_map[new_row][new_col] = 2
                que.append([new_row, new_col, tmp_direction])
                break

            elif i == 3: # 위 반복문이 다 반복할 동안 갈곳을 찾지 못한다면
                #후진
                new_row=row+dx[turn_back(direction)]
                new_col=col+dy[turn_back(direction)]
                # 첫 번째 단계로 돌아감
                que.append([new_row,new_col,direction])
                
                # 만약 후진을 해도 꽉 막혔다면
                if room_map[new_row][new_col] == 1:
                    return cnt
# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))