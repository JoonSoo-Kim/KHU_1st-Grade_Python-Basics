import numpy as np
import matplotlib.pyplot as plt
import csv

def which_Country(countryInput):
    if countryInput == "Argentina":
        return 1
    elif countryInput == "Australia":
        return 2
    elif countryInput == "Brazil":
        return 3
    elif countryInput == "Britain":
        return 4
    elif countryInput == "Canada":
        return 5
    elif countryInput == "China":
        return 6
    elif countryInput == "Indonesia":
        return 7
    elif countryInput == "Japan":
        return 8
    elif countryInput == "Russia":
        return 9
    elif countryInput == "South Korea":
        return 10

countryInput=input("Country : ")
countryNum=which_Country(countryInput)

fileMatrix = []
with open('Error Rate.csv', 'r') as fileRead:
    csvFirst=csv.reader(fileRead)
    for i in csvFirst:
        fileMatrix.append(i)

y_rate=[]
for i in range(10):
    y_rate.append(float(fileMatrix[i][countryNum]))

x_year=['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010']

N_of_groups = len(x_year)
index = np.arange(N_of_groups)

plt.bar(index, y_rate, tick_label=x_year, align='center')

plt.xlabel('Year')
plt.ylabel('Error Rate (%) ')
plt.title('Error Rate of '+countryInput)
plt.xlim( -1, N_of_groups)
plt.ylim( -100, 100)
fig = plt.gcf()
plt.show()

bar_width = 0.2
opacity = 0.5

plt.bar(index, y_rate, bar_width, tick_label=x_year, align='center',alpha=opacity, color='#AA2848', label='rainfall')
fig.savefig("Chart_"+countryInput+".png")