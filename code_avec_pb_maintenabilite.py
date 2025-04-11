def x(a):
    if a == 1:
        return 1
    if a == 2:
        return 1
    else:
        return x(a - 1) + x(a - 2)

def y():
    z = []
    for i in range(1, 20):
        z.append(x(i))
    for j in z:
        if j % 2 == 0:
            print("Even: " + str(j))
        else:
            print("Odd: " + str(j))
    k = 0
    while k < len(z):
        if z[k] > 10:
            print("Big: " + str(z[k]))
        k += 1
    for i in range(5):
        for j in range(3):
            print("Nested loop madness")

y()
