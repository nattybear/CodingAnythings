def listplus_1(A): 
    for i in range(len(A)):
        A[i] = A[i] + 1

    return A 

def pythonic(xs):
    ys = []
    for x in xs:
        ys.append(x + 1)
    return ys

def list_comp(xs):
    return [x + 1 for x in xs]

def map_inc(xs):
    def inc(x): return x + 1
    return list(map(inc, xs))

makeA = input().split()
makeA = list(map(int, makeA))

print(listplus_1(makeA))
