def digital_root(n):
    if n//10==0: return n
    else:
        k=sum([int(x) for x in  str(n)])
        return digital_root(k)
