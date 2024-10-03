def climbstairs(n):
    if n==1:
        return 1
    first,second=1,2
    for i in range(3,n+1):
        third =first+second
        first =second
        second=third
    return second
n=5
print(climbstairs(n))
