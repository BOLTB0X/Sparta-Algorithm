from collections import deque
game_map = [
["#", "#", "#", "#", "#"],
["#", ".", ".", "B", "#"],
["#", ".", "#", ".", "#"],
["#", "R", "O", ".", "#"],
["#", "#", "#", "#", "#"],
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0 # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while game_map[r + diff_r][c + diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count

def is_available_to_take_out_only_red_marble(game_map):
    n,m=len(game_map),len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    red_row,red_col,blue_row,blue_col = -1,-1,-1,-1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == 'R':
                red_row,red_col = i,j
            elif game_map[i][j] == 'B':
                blue_row,blue_col = i,j
    queue.append((red_row,red_col,blue_row,blue_col,1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft() # FIFO
        if try_count > 10: # 10 이하여야 한다.
            break

        for i in range(4):
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == 'O': # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if game_map[next_red_row][next_red_col] == 'O': # 빨간 구슬이 구멍에 떨어진다면(성공)
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col: # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_count > b_count: # 이동 거리가 많은 구슬을 한칸 뒤로
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]
        # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    return False

print(is_available_to_take_out_only_red_marble(game_map)) # True 를 반환해야 합니다