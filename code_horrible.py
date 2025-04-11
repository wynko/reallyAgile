def doStuff(a, b):
    if a > 0:
        if b > 0:
            c = a + b
            print("Sum:", c)
            if c > 10:
                print("Big sum")
            else:
                print("Small sum")
        elif b == 0:
            print("b is zero")
        else:
            print("b is negative")
    elif a == 0:
        print("a is zero")
    else:
        if b > 0:
            print("a is negative, b is positive")
        elif b == 0:
            print("Both zero-ish")
        else:
            print("Everything is negative")

    # Code mort
    return
    print("Ceci ne sera jamais exécuté")

    # Complexité inutile
    for i in range(5):
        for j in range(3):
            for k in range(2):
                print(i + j + k)

    # Variable inutilisée
    x = 42

def helper():
    try:
        f = open("somefile.txt", "r")
        data = f.read()
        f.close()
    except:
        pass  # Silence total

doStuff(1, 2)
doStuff(3, 4)
doStuff(5, 6)
helper()
