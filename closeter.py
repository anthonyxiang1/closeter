#I use DarkSky API to show weather info to base my three inputs on (shoes, season, and style)
#then create an outfit for me to wear that day.

#To reduce outfit decision fatigue and the amount of time spent in the morning getting ready

#things I want to add to this:
#use tkinter GUI
#put shorts into csv later, spring and winter distinction
#account for colors (no groufits)
#rating system - each combination gets a rating, saves it
#accounts for laundry and repeated clothing (maybe a reset button after doing laundry)
#a gym input - clothes to change into

import random
import math
from darksky import forecast
from datetime import date, timedelta
import csv
import matplotlib.pyplot as plt

#darksky API
APIKEY = 'f66b5c93b776e8e4eae533967cba301a'

#using local latitude and longitude, get DarkSky's summary, temperature high/low,
#and precipitation probability for the next few hours
weekday = date.today()
with forecast(APIKEY, 40.9257, -73.1409) as sbu:
    print("WEATHER SUMMARY")
    print(sbu.hourly.summary)
    print("Temp range: " + (str)(sbu.daily[0].temperatureMin) + " - " + (str)(sbu.daily[0].temperatureMax))
    print("Precipitation intensity: " + (str)(sbu.daily[0].precipIntensity))

    hourprecip = [hour.precipProbability for hour in sbu.hourly[:24]]
    time = [(hour.time/3600 -5)%12 + 1 for hour in sbu.hourly[:24]]
    print ("precip probability next 24 hrs: ")
    for i in range(len(hourprecip)):
        print((str)((int)(time[i])) + ":00 : " + (str)(hourprecip[i]))
            
print('----------------------------------')

#my shoes
shoes = ['chucks', 'white leather', 'beaters', 'alphabounce', 'timbs','boots']

if (sbu.daily[0].precipIntensity > 0.01):
    shoes = ['beaters', 'timbs']

#season and temperature-based decisions for jacket
seasons = ['winter', 'spring']
seasonChoice = eval(input("What season is it?" + (str)(seasons)))

if (seasonChoice == 0):
    jackets = ['olive', 'none']
else:
    jackets = ['navy', 'none']

if ((sbu.daily[0].temperatureMax + sbu.daily[0].temperatureMin)/2 < 50 and seasonChoice == 0):
    jacketChoice=0
else:
    jacketChoice = random.randint(0,len(jackets)-1)

#the different styles that I dress in
styles = ("ath", "casual", "bizcasual")

ath = []
casual = []
bizcasual = []

#makes athleisure, casual, and bizcasual category lists
with open('closeter.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i in readCSV:
        if(i[3] == 'ath' or i[4] == 'ath'):
            ath.append(i)
        if(i[3] == 'casual' or i[4] == 'casual'):
            casual.append(i)
        if(i[3] == 'bizcasual' or i[4] == 'bizcasual'):
            bizcasual.append(i)

#I like to start my outfits from the bottom up, choosing shoes first based on weather
#style depending on the weather and occasion
shoeChoice = eval(input("Which shoe to wear today?" + (str)(shoes)))
styleChoice = eval(input("Which style for today?" + (str)(styles)))

if (styleChoice == 0):
    li = ath
elif (styleChoice == 1):
    li = casual
elif (styleChoice == 2):
    li = bizcasual

def outfitMaker(li):
    layer2 = []
    shirt = []
    pants = []
    outfitList = []
    
    for i in range(len(li)):
        if (li[i][1] == 'layer2'):
            layer2.append(li[i][0])
        if (li[i][1] == 'shirt'):
            shirt.append(li[i][0])
        if (li[i][1] == 'pants'):
            pants.append(li[i][0])

    outfitList.append("Jacket: " + jackets[jacketChoice])
    outfitList.append("Outer: " + layer2[random.randint(0,len(layer2)-1)])
    outfitList.append("Shirt: " + shirt[random.randint(0,len(shirt)-1)])
    outfitList.append("Pants: " + pants[random.randint(0,len(pants)-1)])
    outfitList.append("Shoes: " + shoes[shoeChoice])

    for element in range(len(outfitList)):
        print(outfitList[element])


#run outfitMaker
outfitMaker(li)
