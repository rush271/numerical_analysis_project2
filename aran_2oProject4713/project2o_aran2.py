import numpy as np


# ΑΣΚΗΣΗ 6


a=0
b=np.pi/2
I=1

n=10
h=(b-a)/n

x=np.linspace(a, b, n+1)
f=np.sin(x)


#simpson 
sumA=0
sumP=0

for i in range(1,n):
    if i%2==0:
        sumA += f[i]
    else:
        sumP += f[i]
        
S = (h/3) * (f[0] + 4*sumP + 2*sumA + f[n])

#αριθμητικο σφαλμα - simpson
error_AS = abs(I-S)

#θεωρητικο σφαλμα - simpson
theory_AS = (b-a) / 180 * h**4


#τραπεζιο
sum=0
for i in range(1,n):
    sum += f[i]

T = h*(0.5*f[0] + sum +0.5*f[n])

#αριθμητικο σφαλμα - τραπεζιο
error_AT = (I-T)

#θεωρητικο σφαλμα - τραπεζιο
theory_AT = (b-a) / 12 * h**2


print("SIMPSON")
print("  Προσεγγιση = ", S)
print("  Αριθμητικο Σφαλμα = ", error_AS)
print("  Θεωρητικο Σφαλμα = ", theory_AS)

print()
print()

print("ΤΡΑΠΕΖΙΟ")
print("  Προσεγγιση = ", T)
print("  Αριθμητικο Σφαλμα = ", error_AT)
print("  Θεωρητικο Σφαλμα = ", theory_AT)







