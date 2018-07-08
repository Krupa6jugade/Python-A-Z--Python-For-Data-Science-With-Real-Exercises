
from numpy.random import randn
n = 100
counter = 0

for i in randn(n):
    if (i>-1 and i<1 ):
        counter = counter + 1
answear = counter/n

print(answear)

