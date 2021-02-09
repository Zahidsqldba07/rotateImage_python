def rotateImage(a):
    
    rotated = []
    answer = [[0]*len(a) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            rotated.append(a[len(a)-j-1][i])
            answer[i][j] = rotated[i*len(a)+j]
            
    return(answer)
