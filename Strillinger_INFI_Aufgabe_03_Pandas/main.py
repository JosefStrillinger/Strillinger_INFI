import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tabulate import tabulate
import seaborn as sns

df = pd.read_excel('data\Zeitreihe-Winter-2022092012.xlsx', skiprows=2)

base = ['Bezirk','Gemnr','Gemeinde']
years = df.columns[3:].astype(str)
base.extend('x' + years)
df.columns = base
#print(df.describe())


# 2.1
groth_ibk = df.values[2,3:]
plt.title("Nächtigungen in Ibk: ")
plt.plot(groth_ibk, "m.")
plt.xlabel("Year")
plt.ylabel("Anzahl Nächtigungen")
plt.savefig("img/2_1.png")
plt.show()

# 2.2
bezirk = df[df.Bezirk == "KU"]
groth_bezirk = bezirk[df.columns[0:]].values[:,3:].sum(axis=0)
print(groth_bezirk)
plt.title("Nachtigungen in Bezirk Kufstein")
plt.plot(groth_bezirk, "m-")
plt.xlabel("Jahr")
plt.ylabel("Anzahl Nächtigungen")
plt.savefig("img/2_2.png")
plt.show()

# 3.1
min_arr = []
max_arr = []
range_arr = []
avg_arr = []

for i in range(278):
    minimum = min(df.values[i,3:])
    maximum = max(df.values[i,3:])
    ranges = maximum-minimum
    average = df.values[i,3:].mean()
    min_arr.append(minimum)
    max_arr.append(maximum)
    range_arr.append(ranges)
    avg_arr.append(average)
    
df["minimum"] = min_arr
df["maximum"] = max_arr
df["range"] = range_arr
df["avg"] = avg_arr

# 3.1.1
standard_range = []

for i in range(len(range_arr)):
    standard_range.append(range_arr[i]/avg_arr[i])
    
df["standard_range"] = standard_range

# 3.2
tourists_per_year = df[df.columns[3:]].values[1:,:].sum(axis=0)
print("Touristen pro Jahr: ")
print(tourists_per_year)
print("---------------------------------")
tourists_overall = np.sum(tourists_per_year)
print("Touristen gesamt: ")
print(tourists_overall)
print("---------------------------------")
all_districts = ["I", "IM", "IL", "KB", "KU", "LA", "LZ", "RE", "SZ"]
tourists_per_disctricts = []
for i in range(len(all_districts)):
    tourists_per_disctricts.append(df[df.Bezirk == all_districts[i]].values[:,3:].sum())
print(tourists_per_disctricts)

# 4

#4.1 a
df.boxplot(column="standard_range", by="Bezirk")

#4.1 b
pos = 0
labels = df["Bezirk"].unique()
for b in labels:
    bez = df[df.Bezirk == b]
    plt.boxplot(bez["standard_range"], positions=[pos])
    pos += 1
    plt.xticks(range(len(labels)), labels)
    
#4.1 c
sns.boxenplot(x = df["Bezirk"], y = df["standard_range"], data=df)
plt.savefig("img/4_2.png")
plt.show()

# 4.2
sns.barplot(x = df.columns[3:26], y = df.values[2,3:26], palette="terrain")
plt.show()

# 5
df_2 = pd.read_excel("data/bev_meld.xlsx")

data = pd.merge(df, df_2, how="inner", on="Gemnr")
data = data.drop(columns="Gemnr")

base = ["Bezirk", "Gemeinde"]
years = data.columns[2:25].astype(str)
base_2 = ["minimum", "maximum", "range", "avg", "standard_range", "Bezirk2", "Gemeinde2"]
years_2 = data.columns[32:].astype(str)
base.extend(years)
base.extend(base_2)
base.extend("y" + years_2)
data.columns = base

# 5 a
stays_per_person_2018 = data["x2018"]/data["y2018"]
stays_per_person_2020 = data["x2020"]/data["y2020"]

# 5 b
sns.boxplot(x = data["Bezirk"], y = stays_per_person_2018, data=data)
plt.savefig("img/5_b_1.png")
plt.show()

sns.boxplot(x = data["Bezirk"], y = stays_per_person_2020, data=data)
plt.savefig("img/5_b_2.png")
plt.show()

# 5 c
lowest_ten = stays_per_person_2020.sort_values(ascending=True)
highest_ten = stays_per_person_2020.sort_values(ascending=False)

lowest_indexes = []
highest_indexes = []
bezirke = data["Gemeinde"]

for i in range(0,10):
    lowest_indexes.append(bezirke[lowest_ten.index[stays_per_person_2020 == lowest_ten[i]]].values[0])
    highest_indexes.append(bezirke[highest_ten.index[stays_per_person_2020 == highest_ten[i]]].values[0])
    
sns.boxplot(x = lowest_indexes, y = lowest_ten[:10], data=data)
plt.savefig("img/5_c_1.png")
plt.show()

sns.boxplot(x = highest_indexes, y = highest_ten[:10], data=data)
plt.savefig("img/5_c_2.png")
plt.show()

# 5 d
plt.title("Nächtigungen pro Kopf in Angerberg")
plt.plot(stays_per_person_2020[139-6], "m.")# Angerberg in Excel: Zeile 139 
#print(stays_per_person_2020[139-6])
plt.xlabel("Gemeinde")
plt.ylabel("Nächtigungen pro Kopf")
plt.savefig("img/5_d.png")
plt.show()