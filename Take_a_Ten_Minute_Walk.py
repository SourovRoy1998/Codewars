def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk)!=10: return False
    ix,iy=0,0
    for x in walk:
        if x=='n': iy+=1
        if x=='s': iy-=1
        if x=='e': ix+=1
        if x=='w': ix-=1
    if ix==0 and iy==0:
        return True
    return False
