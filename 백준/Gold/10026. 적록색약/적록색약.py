import sys
from collections import deque

test = int(input())
arr= []
for _ in range(test):
    arr.append(list(input()))
visited = [ [0]*test for _ in range(test)]
q=deque()

count1=0
count2=0

for i in range(test):
    for j in range(test):
        if visited[i][j] == 0:
            q.append([i,j])
            visited[i][j]=1
            count1+=1
            while q:
                si,sj = q.popleft()
                for di,dj in [ [-1,0],[1,0],[0,-1],[0,1] ]:
                    di= si + di
                    dj= sj + dj
                    if 0<=di<test and 0<=dj<test and visited[di][dj]==0 and arr[di][dj]==arr[i][j]:
                        q.append([di,dj])
                        visited[di][dj]=1
visited = [ [0]*test for _ in range(test)]
q=deque()
for i in range(test):
    for j in range(test):
        if visited[i][j] == 0:
            q.append([i,j])
            visited[i][j]=1
            count2+=1
            while q:
                si,sj = q.popleft()
                for di,dj in [ [-1,0],[1,0],[0,-1],[0,1] ]:
                    di= si + di
                    dj= sj + dj
                    if 0<=di<test and 0<=dj<test and visited[di][dj]==0 and (arr[i][j] == 'R' or arr[i][j] == 'G'):
                        if arr[di][dj] == 'R' or arr[di][dj] == 'G' :
                            q.append([di,dj])
                            visited[di][dj]=1
                    elif 0<=di<test and 0<=dj<test and visited[di][dj]==0 and arr[di][dj]==arr[i][j]:
                        q.append([di, dj])
                        visited[di][dj] = 1
print(count1,count2)