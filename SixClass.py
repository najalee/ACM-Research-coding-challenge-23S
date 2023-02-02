import numpy as np
import matplotlib.pyplot as plt


    

# get the data
data = np.genfromtxt('6 class csv.csv', delimiter=',')

# magnitude vs radius of dwarf stars
dwarfMag = np.array([])
dwarfRad = np.array([])
i = 0
# get an array of all the dwarf star magnitudes and radii
for starType in data[:-1, 4]:
    if starType == 0 or starType == 1 or starType == 2:
        dwarfMag = np.append(dwarfMag, data[i, 3])
        dwarfRad = np.append(dwarfRad, data[i, 2])
    i+=1

plt.plot(dwarfRad, dwarfMag, 'ro')
plt.xlabel('Radius (R/Ro)')
plt.ylabel('Absolute Magnitude (Mv)')
plt.title("Dwarf Stars Absolute Magnitude vs Radius")
plt.axis([0, .8, 0, 20])
plt.show()

# Brown Dwarf -> Star Type = 0
# Red Dwarf -> Star Type = 1
# White Dwarf -> Star Type = 2
# Main Sequence -> Star Type = 3
# Supergiant -> Star Type = 4
# Hypergiant -> Star Type = 5

bDwarfAvgL = 0
rDwarfAvgL = 0
wDwarfAvgL = 0
i = 0

# count the total luminosity of all dwarf stars
for starType in data[:-1, 4]:
    if starType == 0:
        bDwarfAvgL+=data[i, 1]

    elif starType == 1:
        rDwarfAvgL+=data[i, 1]

    elif starType == 2:
        wDwarfAvgL+= data[i, 1]
    
    i+=1

# get the average luminosity of each type
bDwarfAvgL/=40
rDwarfAvgL/=40
wDwarfAvgL/=40

# put the values into scientific notation:
sci = "{:.2e}".format(bDwarfAvgL)
bDwarfAvgLSci = float(sci[:-4])
sci = "{:.2e}".format(rDwarfAvgL)
rDwarfAvgLSci = float(sci[:-4])
sci = "{:.2e}".format(wDwarfAvgL)
wDwarfAvgLSci = float(sci[:-4])

# average luminosity of brown, red, and white dwarf stars
names = ["Brown", "Red", "White"]
values = [bDwarfAvgL, rDwarfAvgL, wDwarfAvgL]
plt.subplot(131)
plt.bar(names, values)
plt.xlabel("Dwarf Star")
plt.ylabel("Average Luminosity")
plt.show()


bDwarfAvgT = 0
rDwarfAvgT = 0
wDwarfAvgT = 0
i = 0

# count the total temperature of all dwarf stars
for starType in data[:-1, 4]:
    if starType == 0:
        bDwarfAvgT+=data[i, 0]

    elif starType == 1:
        rDwarfAvgT+=data[i, 0]

    elif starType == 2:
        wDwarfAvgT+= data[i, 0]
    
    i+=1

# get the average temperature of each type
bDwarfAvgT/=40
rDwarfAvgT/=40
wDwarfAvgT/=40

# put the values into scientific notation:
sci = "{:.2e}".format(bDwarfAvgT)
bDwarfAvgTSci = float(sci[:-4])
sci = "{:.2e}".format(rDwarfAvgT)
rDwarfAvgTSci = float(sci[:-4])
sci = "{:.2e}".format(wDwarfAvgT)
wDwarfAvgTSci = float(sci[:-4])


bDwarfAvgR = 0
rDwarfAvgR = 0
wDwarfAvgR = 0
i = 0

# count the total radius of all dwarf stars
for starType in data[:-1, 4]:
    if starType == 0:
        bDwarfAvgR += data[i, 2]

    elif starType == 1:
        rDwarfAvgR += data[i, 2]

    elif starType == 2:
        wDwarfAvgR += data[i, 2]

    i += 1

# get the average radius of each type
bDwarfAvgR/=40
rDwarfAvgR/=40
wDwarfAvgR/=40

# put the values into scientific notation:
sci = "{:.2e}".format(bDwarfAvgR)
bDwarfAvgRSci = float(sci[:-4])
sci = "{:.2e}".format(rDwarfAvgR)
rDwarfAvgRSci = float(sci[:-4])
sci = "{:.2e}".format(wDwarfAvgR)
wDwarfAvgRSci = float(sci[:-4])

bDwarfAvgAM = 0
rDwarfAvgAM = 0
wDwarfAvgAM = 0
i = 0

# count the total absolute magnitude of all dwarf stars
for starType in data[:-1, 4]:
    if starType == 0:
        bDwarfAvgAM+=data[i, 3]
    elif starType == 1:
        rDwarfAvgAM+=data[i, 3]
    elif starType == 2:
        wDwarfAvgAM+=data[i, 3]
    i += 1

# get the average absolute magnitude of each type
bDwarfAvgAM/=40
rDwarfAvgAM/=40
wDwarfAvgAM/=40


# put the values into scientific notation:
sci = "{:.2e}".format(bDwarfAvgAM)
bDwarfAvgAMSci = float(sci[:-4])
sci = "{:.2e}".format(rDwarfAvgAM)
rDwarfAvgAMSci = float(sci[:-4])
sci = "{:.2e}".format(wDwarfAvgAM)
wDwarfAvgAMSci = float(sci[:-4])


# radar chart of brown, red, white dwarf stars
names = ["Temperature", "Luminosity", "Radius", "Absolute Magnitude"]
names = [*names, names[0]]
bDwarfValues = [bDwarfAvgT/1000, bDwarfAvgL*1000, bDwarfAvgRSci, bDwarfAvgAMSci]
rDwarfValues = [rDwarfAvgT/1000, rDwarfAvgL*1000, rDwarfAvgRSci, rDwarfAvgAMSci]
wDwarfValues = [wDwarfAvgT/1000, wDwarfAvgL*1000, wDwarfAvgRSci, wDwarfAvgAMSci]
bDwarfValues = [*bDwarfValues, bDwarfValues[0]]
rDwarfValues = [*rDwarfValues, rDwarfValues[0]]
wDwarfValues = [*wDwarfValues, wDwarfValues[0]]

categoryLabels = np.linspace(start=0, stop=2 * np.pi, num=len(bDwarfValues))

plt.figure(figsize=(8, 8))
plt.subplot(polar=True)
plt.plot(categoryLabels, bDwarfValues, label='Brown Dwarf', color="green")
plt.plot(categoryLabels, rDwarfValues, label='Red Dwarf', color="red")
plt.plot(categoryLabels, wDwarfValues, label='White Dwarf', color="gray")
plt.title('Average Dwarf Star Values Comparison', size=20)
lines, categoryLabels = plt.thetagrids(np.degrees(categoryLabels), labels=names)
plt.legend()
plt.show()


