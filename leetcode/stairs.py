def stairs(n):
    l, r = 1, 1
    for i in range(1, n):
        l, r = r, l + r
    return r
  
def stairs_comb(n):
    dp = [[]]*(n+1)
    for i in range(2, n):
        lst = []
        print dp[i-1]
        for prev in dp[i-1]:
            lst.append(prev.append(1))
            for i in range(len(prev)):
                if prev[i] == 1:
                    curr = prev[:i] + [2] + prev[i:]
                    if curr not in lst:
                        lst.append()    
    
print stairs(5)
