from collections import defaultdict
def solution(genres, plays):
    plays_sum = defaultdict(int)
    plays_num = defaultdict(list)
    answer=[]
    for i in range(len(genres)):
        plays_sum[genres[i]]+=plays[i]
        plays_num[genres[i]].append([i,plays[i]])
        
    genre_sum = sorted(plays_sum.items(), key=lambda x : -x[1])
    # print(genre_sum)
    for arr in genre_sum:
        count = 0
        # print(plays_num[arr[0]])
        num_plays = plays_num[arr[0]]
        num_plays.sort(key = lambda x : (-x[1],x[0]))
        # print(num_plays)
        for i,j in num_plays:
            if count ==2:
                break
            answer.append(i)
            count+=1
    
    return answer