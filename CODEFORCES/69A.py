n = int(input())
a, b, c = 0, 0, 0
for i in range(n):
    x, y, z = map(int, input().split())
    a, b, c = a + x, b + y, c + z
if a == b == c == 0:
    print("YES")
else:
    print("NO")
    