def primeFactors(n):
    spf = [0 for i in range(n+1)]
    spf[1] = 1
    for i in range(2, n+1):
        spf[i] = i
    for i in range(4, n+1, 2):
        spf[i] = 2
 
    for i in range(3, int(n**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i
                     
    while n != 1:
        print(spf[n], end=" ")
        n = n // spf[n]
 
# example usage
n = 315
primeFactors(n)