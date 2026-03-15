import numpy as np
import matplotlib.pyplot as plt


# ΑΣΚΗΣΗ 5


x = np.linspace(-np.pi, np.pi, 10) #διαλεγω 10 ισαπεχοντα τυχαια σημεια στο [-π, π]
y = np.sin(x) #υπολογιζω το sin των 10 σημειων


# ΜΕ ΠΟΛΥΩΝΥΜΙΚΗ ΠΡΟΣΕΓΓΙΣΗ


def lagrange(x, xp, yp):
    p=0 #τελικη τιμη πολυωνυμου
    n=len(xp) #πληθος σημειων παρεμβολης
    

    for i in range(n):
        Li = 1
        for j in range(n):
            if (j!=i):
                Li = Li * (x - xp[j])/(xp[i]-xp[j]) #τυπος lagrange
        p += yp[i]*Li

    return p


# ΜΕ SPLINES


taksinom = np.argsort(x) #ταξινομω τα σημεια ως προς τον αξονα x
xs = x[taksinom]
ys = y[taksinom]

def splines(x, xp, yp):
    n=len(xp)

    for i in range(n-1):
        if ((xp[i] <= x) and (x <= xp[i+1])): #ελεγχω σε ποιο διαστημα ανηκει το x
            k = (x-xp[i])/(xp[i+1] - xp[i])
            z =  (1-k) * yp[i] + k* yp[i+1]
            return z


# ΜΕ ΕΛΑΧΙΣΤΑ ΤΕΤΡΑΓΩΝΑ


def elaxistaTetragona(x, xp, yp, vathmos):
    n=len(xp)
    A=np.zeros((n,vathmos+1))

    for i in range(n):
        for j in range(vathmos+1):
            A[i][j] = xp[i]**j

    a = np.linalg.solve(A.T @ A, A.T @ yp) #βρισκω τους συντελεστες του πολυωνυμου

    s=0    
    lena = len(a);
    for i in range (lena):
        s+= a[i] * x ** i

    return s


            
# GRAPHS AND ERRORS


xx = np.linspace(-np.pi, np.pi, 200) #δημιουργω 200 σημεια
y2 = np.sin(xx)

v_lagrange = np.zeros(len(xx))
v_splines = np.zeros(len(xx))
v_elaxistaTetragona = np.zeros(len(xx))

for i in range (len(xx)):
    v_lagrange[i] = lagrange(xx[i], x, y)
    v_splines[i] = splines(xx[i], xs, ys)
    v_elaxistaTetragona[i] = elaxistaTetragona(xx[i], x, y, 3)


#γραφημα συγκρισης προσεγγισεων
plt.plot(xx, v_lagrange, label="Lagrange")
plt.plot(xx, v_splines, label="Splines")
plt.plot(xx, v_elaxistaTetragona, label="Ελαχιστα Τετράγωνα")

plt.title("Συγκριση προσεγγίσεων της sin(x)")
plt.xlabel("ΑΞΟΝΑΣ Χ")
plt.ylabel("ΑΞΟΝΑΣ Υ")  

plt.grid()
plt.legend()
plt.xlim(-np.pi, np.pi)
plt.savefig("graph5.png", dpi=300)
plt.show()


#βρισκω τα σφαλματα για τη καθε μεθοδο
error_lagrange = np.abs(y2 - v_lagrange)
error_splines = np.abs(y2 - v_splines)
error_elaxistaTetragona = np.abs(y2 - v_elaxistaTetragona)


#γραφημα σφαλματων
plt.plot(xx, error_lagrange, color="blue", label="Lagragne")
plt.plot(xx, error_splines, color="green", label="Spline")
plt.plot(xx, error_elaxistaTetragona, color="red" , label="Ελαχιστα Τετράγωνα")

plt.title("Σφαλμα προσεγγισης της sin(x)")
plt.xlabel("ΑΞΟΝΑΣ Χ")
plt.ylabel("ΑΞΟΝΑΣ Υ")

plt.grid()
plt.legend()
plt.xlim(-4,4)
plt.savefig("graph6.png", dpi=300)
plt.show()


#βρισκω το μεγιστο σφαλμα και επειτα την εκτιμιση των ψηφιων
E1 = np.max(error_lagrange)
E2 = np.max(error_splines)
E3 = np.max(error_elaxistaTetragona)

print("Lagrange ψηφεια ακριβειας = ", -np.log10(E1))
print("Spline ψηφεια ακριβειας = ", -np.log10(E2))
print("Ελαχιστα Τετραγωνα ψηφεια ακριβειας = ", -np.log10(E3))






    


            
        
        
    
