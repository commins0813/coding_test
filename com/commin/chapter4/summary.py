"""
1. 논리 연산자/ 비트 연산자 활용하기
 a,b = 10,20
 if a > b:
    if a % 10 == 0:
        print(a)
 -> 이런 코드를 작성할때는 깊게 반복되게 반복문이 들어가는것을 지양하자.

 if a>b and a% 10 == 0:
    print(a)

 # and/or/not


 1 <<2
 1 & 1
 1 | 1
 1 ^



 # 방향 벡터
 위 아래 왼쪽 오른쪽 등등
 BFS / DFS 탐색 문제
 2/3차원 배열
 5X5 맵
 상하좌우, 상화좌우대각선, 나이트/말
 예시) 상하좌우
 (2,2) 가 처음 위치일때
 if way == 'N':
    x += -1
    y += 0
 elif way == 'S':
    x += 1
    y += 0
 elif way == 'E':
    x += 0
    y += 1
 else:
    x += 0
    y += -1

위를 표로 정리하면..
    N   S   E   W
x   -1  1   0   0
y   0   0   1   -1

위 표를 파이썬 코드로 정리하면..

쓰기편한 버전
dx = [-1,1,0,0]
dy = [0,0,1,-1]

반시계 방향
dx = [0,-1,0,1]
dy = [1,0,-1,0]

시계 방향
dx = [0,1,0,-1]
dy = [1,0,-1,0]

활용하는 법
x += dx['ENSW'.index(way)]
y += dx['ENSW'.index(way)]

for i in range(4):
    dfs(x+dx[i], y+dy[i])
    
"""