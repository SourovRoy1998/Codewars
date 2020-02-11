def min_num_taxis(requests):
    V=[0]*10002
    for x in requests:
        V[x[0]]+=1
        V[x[1]+1]-=1
    ans=0
    count=0
    for x in V:
        count+=x
        ans=max(ans,count)
    return ans
