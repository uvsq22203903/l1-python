def insertion_tableau(L, v, i):
    for x in range(len(L)):
        if x == i :
            L.append(v)


liste = [0, 1, 2, 3]
print(insertion_tableau(liste, 42, 1))