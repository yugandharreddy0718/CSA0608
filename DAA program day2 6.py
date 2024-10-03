def champagnetower(query_row =1,query_glass=1):
    glasses=[[0]*i for i in range(i,102)]
    glasses[0][0]=poured
    for i in range(0,101):
        for j in range(0,i+1):
            q=(glasses[i][j]-1.0)/2.0
            if q>0:
                glasses[i+1][j]+=q
                glasses[i+1][j+1]+=q
    return min(1,glasses[query_row][query_glass])
