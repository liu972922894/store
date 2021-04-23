a = [1,5,21,30,15,9,30,24]
b = 0
c = []

while b<len(a):
    if a[b] %5==0:
        c.append(a[b])
    b=b+1
print("5倍数和", sum(c))