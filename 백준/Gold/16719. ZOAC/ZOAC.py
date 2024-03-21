arr = list(input())
visited=[0]*len(arr)
def search(word, s):
    if not word:
        return
    w=min(word)
    i=word.index(w)
    visited[i+s]=1
    for j in range(len(visited)):
        if visited[j]==1:
            print(arr[j],end="")
    print()
    search(word[i+1:],s+i+1)
    search(word[:i],s)
search(arr,0)