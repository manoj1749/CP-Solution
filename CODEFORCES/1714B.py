test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    step = 0
    while len(a) != len(set(a)):
        a=a[1:]
        step+=1
    print(step)