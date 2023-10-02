from collections import deque

def solution(n, wires):
    answer = 1e9
            
    tree = [[] for _ in range(n+1)]
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)
    
    
    # 시작점, 끊을 노드
    def bfs(start, cut):
        cnt = 1
        q = deque()
        q.append(start)
        
        visited = [False] * (n+1)
        visited[start] = True
        
        while q:
            now = q.popleft()
            for next in tree[now]:
                # now에 연결되어있는 노드 중 방문했거나 끊은 노드면 패스 
                if next == cut or visited[next]:
                    continue
                visited[next] = True
                q.append(next)
                cnt += 1
        
        return cnt
    
    
    for i, j in wires:
        cnt = bfs(i, j)
        answer = min(answer, abs(cnt - (n-cnt)))
    
    return answer