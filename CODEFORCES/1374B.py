def mul2div6(n):
    
    if n == 1:
        return 0
    
    elif n%6==0:
        return 1 + mul2div6(n/6)
    
    elif n%6!=0:
        n = n * 2
        if n%6==0:
            return 2 + mul2div6(n/6)
        else:
            return -1+ 'not divisible by 6'
        
t = int(input())
for i in range(t):
    n = int(input())
    try:
        result = mul2div6(n)
        print(result)
    except:
        print(-1)
    