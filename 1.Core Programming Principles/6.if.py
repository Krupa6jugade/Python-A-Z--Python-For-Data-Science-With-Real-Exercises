import numpy as np
from numpy.random import randn

print(randn())

f = randn()

answer = None
print("\n If ")
if f > 1:
    answer ='Greater than 1'

print(f)

print(answer)




print("\n if Else ")

eli = randn()

if eli > 1:
    answer ='Greater than 1'
else:
    answer = 'Less Than 1 '


print(eli)

print(answer)














print("\n\n If Else elif ")

x = randn()

if x > 1:
    answer ='Greater than 1'
else:
    if x >= -1:
        answer = 'Between -1 and 1'
    else:
        answer = "Less than - 1"




print(x)

print(answer)

print("Elif ")

y = randn()

if y > 1:
    answer ='Greater than 1'
elif y >= -1:
    answer = 'Between -1 and 1'
else:
        answer = "Less than - 1"



print(x)

print(answer)

