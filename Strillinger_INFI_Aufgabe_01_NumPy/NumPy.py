import numpy as np

#1.1.1

print()
print("1.1.1")
print()

a1 = np.arange(100,201)
print("Zahlen von 100 bis 200:")
print(a1)
print("==============================")

#1.1.2

print()
print("1.1.2")
print()

a2 = np.linspace(100,200,num=51)
#a2 = np.arange(100,200,2)
print("Zahlen von 100 bis 200 in 2er Schritten:")
print(a2)
print("==============================")

#1.1.3

print()
print("1.1.3")
print()

a3 = np.linspace(100,110,num=21)
#a3 = np.arange(100,110.5,0.5)
print("Zahlen von 100 bis 110 in 0.5er Schritten:")
print(a3)
print("==============================")

#1.1.4
print()
print("1.1.4")
print()

#Gleichverteilt:
a4 = np.random.randint(100, 200, 10)
print(a4)

#Normalverteilt:
a5 = np.random.normal(0, 100, 100)
a5.sort()
print(a5)

#2.1
print()
print("2.1")
#Mittelwert
print("==============================")
print("Mittelwert:")
print(np.mean(a5))

#Median
print("==============================")
print("Median:")
print(np.median(a5))

#Minimum
print("==============================")
print("Minimum:")
print(np.amin(a5))

#Maximum
print("==============================")
print("Maximum:")
print(np.amax(a5))

#Standardabweichung
print("==============================")
print("Standardabweichung:")
print(np.std(a5))

#2.2
print("==============================")
print("2.2")
print(np.mean(a1) - np.std(a1)*2, np.mean(a1) + np.std(a1)*2)

#2.3
print("==============================")
print("2.3")
print(a5*100)

#2.4
print("==============================")
print("2.4")
print(a5[:10])

#2.5
print("==============================")
print("2.5")
print(a5[np.argwhere(a5>=0)])