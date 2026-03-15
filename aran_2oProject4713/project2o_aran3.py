import numpy as np

#οι 10 τιμες κλεισιματος
y1 = [2.5300, 2.4400, 2.5000, 2.5000, 2.4400, 2.4400, 2.5000, 2.4900, 2.5200, 2.5400]
y2 = [14.1200, 13.8200, 14.1400, 13.9500, 14.1500, 14.2500, 14.1100, 14.0500, 14.0800, 14.3500]

x = np.arange(10)

def elaxistaTetragona(x, y, vathmos):
    n=len(x)
    A=np.zeros((n,vathmos+1)) #πινακα συντελεστων

    for i in range(n):
        for j in range(vathmos+1):
            A[i][j] = x[i]**j

    a = np.linalg.solve(A.T @ A, A.T @ y) #βρισκω τους συντελεστες του πολυωνυμου 
    return a

#υπολογιζω την τιμη του πολυωνυμου για x
def polyonymo_ans(a, x): 
    s=0    
    lena = len(a)
    for i in range (lena):
        s+= a[i] * x ** i
    return s

#υπολογιζω το μεγιστο απολυτο σφαλμα
def maxSfalma(a, x, y):
    maxError=0
    lenx = len(x)
    for i in range (lenx):
        error=abs(polyonymo_ans(a,x[i]) - y[i])
        if error > maxError:
            maxError = error
    return maxError


a1_2ou = elaxistaTetragona(x, y1, 2)
a2_2ou = elaxistaTetragona(x, y2, 2)

a1_3ou = elaxistaTetragona(x, y1, 3)
a2_3ou = elaxistaTetragona(x, y2, 3)

a1_4ou = elaxistaTetragona(x, y1, 4)
a2_4ou = elaxistaTetragona(x, y2, 4)



print("ΜΕΤΟΧΗ 1")
print()
print("Σφαλματα:")
print("2ου βαθμου: ", maxSfalma(a1_2ou, x, y1))
print("3ου βαθμου: ", maxSfalma(a1_3ou, x, y1))
print("4ου βαθμου: ", maxSfalma(a1_4ou, x, y1))
print()
print()
print("Συντελεστες 2ου βαθμου", a1_2ou)
print("Συντελεστες 3ου βαθμου", a1_3ou)
print("Συντελεστες 4ου βαθμου", a1_4ou)
print()
print()
print("2ου βαθμού:", polyonymo_ans(a1_2ou, 10))
print("3ου βαθμού:", polyonymo_ans(a1_3ou, 10))
print("4ου βαθμού:", polyonymo_ans(a1_4ou, 10))
print()
print()
print("Οι επόμενες 5 προβλέψεις")
print("η 11η = ", polyonymo_ans(a1_2ou,11))
print("η 12η = ", polyonymo_ans(a1_2ou,12))
print("η 13η = ", polyonymo_ans(a1_2ou,13))
print("η 14η = ", polyonymo_ans(a1_2ou,14))
print("η 15η = ", polyonymo_ans(a1_2ou,15))





print()
print("ΜΕΤΟΧΗ 2")
print()
print("Σφαλματα:")
print("2ου βαθμου: ", maxSfalma(a2_2ou, x, y2))
print("3ου βαθμου: ", maxSfalma(a2_3ou, x, y2))
print("4ου βαθμου: ", maxSfalma(a2_4ou, x, y2))
print()
print()
print("Συντελεστες 2ου βαθμου", a2_2ou)
print("Συντελεστες 3ου βαθμου", a2_3ou)
print("Συντελεστες 4ου βαθμου", a2_4ou)
print()
print()
print("2ου βαθμού:", polyonymo_ans(a2_2ou, 10))
print("3ου βαθμού:", polyonymo_ans(a2_3ou, 10))
print("4ου βαθμού:", polyonymo_ans(a2_4ou, 10))
print()
print()
print("Οι επόμενες 5 προβλέψεις")
print("η 11η = ", polyonymo_ans(a2_2ou,11))
print("η 12η = ", polyonymo_ans(a2_2ou,12))
print("η 13η = ", polyonymo_ans(a2_2ou,13))
print("η 14η = ", polyonymo_ans(a2_2ou,14))
print("η 15η = ", polyonymo_ans(a2_2ou,15))




