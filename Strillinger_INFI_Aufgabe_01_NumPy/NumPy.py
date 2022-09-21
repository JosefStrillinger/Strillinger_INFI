import numpy as np

#1.1.1
a1 = np.arange(100,201)
print("Zahlen von 100 bis 200:")
print(a1)
print("==============================")

#1.1.2

a2 = np.arange(100,201,2)
print("Zahlen von 100 bis 200 in 2er Schritten:")
print(a2)
print("==============================")

#1.1.3

a3 = np.arange(100,201,0.5)
print("Zahlen von 100 bis 200 in 0.5er Schritten:")
print(a3)
print("==============================")

#1.1.4

#Gleichverteilt:
a4 = np.random.randint(100, 200, 10)
print(a4)

#Normalverteilt:
a5 = np.random.normal(0, 100, 100)
print(a5)
