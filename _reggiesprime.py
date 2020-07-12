 
# not my cleanest or most legible code but its also not super complicated. Also transcribed from Jupiters


datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

#get y, this was just lumped into the next function
def gy(m, b, x):
    return m*x + b

#calculate all errors from a point X,Y
def cae(m, b, point):
    trg = 0
    for (r,y) in point:
        xp, yp = (r,y)
        y = m*xp + b
        cae = abs(y - yp)
        trg += cae
    return trg

possible_ms = [m * 0.1 for m in range(-100, 101)]
possible_bs = [b * 0.1 for b in range(-200, 201)]

#find smallest error
def smlr(possible_ms, possible_bs):
    smlrx = (float("inf"))
    best_m = 0
    best_b = 0
    for m in possible_ms:
        for b in possible_bs:
            error = cae(m, b, datapoints)
            if error < smlrx:
                best_m = m
                best_b = b
                smlrx = error
    return best_m, best_b, smlrx

#from a data set get smallest errors
smlrs = smlr(possible_ms, possible_bs)
smlr = smlrs [2]
best_m = smlrs [0] 
best_b = smlrs [1]

#just makes the floats look nice
def mnf(op):
    gp = len([op])
    if gp == 1:
        gimme = '%.1f' %(op) 
        it = float(gimme)
        return it
    else: 
        just = ['%.1f' %(n) for n in op] 
        gimme = [float(n) for n in just] 
        return gimme
    


smlr = mnf(smlr)
best_m = mnf(best_m)
best_b = mnf(best_b)

#returns best ball bounce based off standard deviation.
m = 0.3
b = 1.7
x = 6
print(' this is it')
print('x is equal to ball width')
print(gy(m, b, x))
