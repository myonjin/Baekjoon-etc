def solution(word):
    arr = []
    words = "AEIOU"
    answer = 0

    def f(cnt, w):
        if cnt == 5:
            return 0
        for i in range(5):
            arr.append(w+words[i])
            f(cnt + 1, w+words[i])

    f(0, "")
 
    
    return arr.index(word)+1