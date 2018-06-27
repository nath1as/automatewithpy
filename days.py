import math

C = 50
H = 30

X = []
Y = [i for i in input('give me a number: ').split(',')]

for d in Y:
    X.append(str(int(round(math.sqrt(2*C*float(d)/H)))))

print(','.join(X))
