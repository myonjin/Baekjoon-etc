def solution(sizes):
    sizes.sort(key = lambda x : -x[0]*x[1])
    print(sizes)
    max_row = sizes[0][0] # 가로
    max_col = sizes[0][1] # 세로
    for size in sizes:
        x,y = size
        if max_row>=y and max_col>=x:
            continue

        if x>= max_row or y>=max_col:
            dx = max(max_row,x)
            dy = max(max_col,y)
            
            dx2 = max(max_row,y)
            dy2 = max(max_col,x)
            if dx*dy >= dx2*dy2:
                max_row, max_col = dx2,dy2
            else:
                max_row, max_col = dx,dy
            
    answer = max_row * max_col    
    return answer