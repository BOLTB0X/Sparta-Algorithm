# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

#시작 노드(루트 노드)인 1부터 탐색
#현재 방문한 노도를 visited_array에 추가
#현재 방문한 노드와 인전한 보드 중 반문하지 않은 노드에 방문
def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for adjacent_node in adjacent_graph:
        if adjacent_node not in visited_array:
            dfs_recursion(adjacent_graph,adjacent_node,visited_array)
    return


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!