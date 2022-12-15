# Question 1


def f(x):
    return 3*x + 1


def g(x):
    return 2*x - 3


print(f(g(3)))

# Question 2

jtm = []
k = 0
while k < 5:
    jtm.append(k*5)
    jtm.sort()
    k = k+1
print(jtm[-1])

# Question 3

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(A)):
    for j in range(len(A[i])):
        B[i][j] = A[j][i]
print(B[0])

# Question 4

def r(x, y):
    while x < y:
        x, y = x*2, y+3
    return x+y
print(r(4, 9))

# Question 5

res = 1
L = [x%5 for x in range(10)]
for i in range(len(L)):
    if i in L:
        res *= i
print(res)

# Question 6

def tmp(i):
    while (i < 4):
        print("bonjour")
        i += 1
    return 2*i
i, j = 0, 0
while (i < 7):
    tmp(i)
    i += 1
print(tmp(i))

# Question 7:

l = ["Bonjour", "Bonsoir"]
print(l[1][5])

# Question 8:

m = []
for i in range (10):
    m.append([3*x for x in range(i)])
print(m[4][2])

# Question 9

l = [2, 3, 2, 4]
l.remove(2)
print(l[2])

# Question 10

cpt = 1


def f():
    global cpt
    L = [3, 6, 1, 2]
    for e in L:
        cpt += 1


f()
print(cpt)

# Question 12


def func(x):
    t = 1
    for i in range(2, x+1):
        t = t*i
    return  t


def exo(liste):
    ll = []
    for i in range(len(liste)):
        ll.append(func(liste[i]))
    return ll


print(exo([6, 1, 2, 4]))

# Question 13

"""
def diviseListe(L):
    for i in L:
        L[i] = L[i]//2


print(diviseListe([15, 7, 89]))
"""
# Question 14


def g(n):
    a = 0
    for i in range (1, n , 2):
        a = a + i
    return a


print(g(10))

# Question 15


def f(L):
    cpt = 0
    for i in range(len(L)):
        cpt += 1
        L[cpt] += 2
        return L
print(f([1, 2, 3, 4]))

# Question 16
"""
L1 = [1, 2, 3, 4, 5, 6]
L2 = [e**2 for e in L1]
L2.extend(L1[len(L2)//2])
"""
# Question 18

a, b, c = 5, True, False
if (a >= 30 or 12/4==3):
    a = a + 25
else :
    a = -a 
if (b or 12/5==2):
    b = not(b != c)
print(a,b)

# Question 19


def f(liste):
    c = 1
    for x in liste:
        c = c*2
    print(c)
f([1, 2, 3, 4])