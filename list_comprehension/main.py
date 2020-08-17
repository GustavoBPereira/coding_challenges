def comprehensions(x, y, z, n):
    return [[a, b, c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c != n]
