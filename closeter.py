#I use DarkSky API to show weather info to base my three inputs on (shoes, season, and style)
#then create an outfit for me to wear that day.

#To reduce outfit decision fatigue and the amount of time spent in the morning getting ready

#things I want to add to this:
#use tkinter GUI
#put shorts into csv later
#account for colors (no groufits)
#rating system - each combination gets a rating, saves it
#accounts for laundry and repeated clothing (maybe a reset button after doing laundry)

import random
import math
from darksky import forecast
from datetime import date, timedelta
import csv
import matplotlib.pyplot as plt

#darksky API
APIKEY = 'f66b5c93b776e8e4eae533967cba301a'

lat = eval(input("Enter latitude:"))
long = eval(input("Enter longitude:"))

#using local latitude and longitude, get DarkSky's summary, temperature high/low,
#and precipitation probability for the next few hours
weekday = date.today()
with forecast(APIKEY, lat, long) as location:
    print("WEATHER SUMMARY")
    print(location.hourly.summary)
    print("Temp range: " + (str)(location.daily[0].temperatureMin) + " - " + (str)(location.daily[0].temperatureMax))
    print("Precipitation intensity: " + (str)(location.daily[0].precipIntensity))

    hourprecip = [hour.precipProbability for hour in location.hourly[:24]]
    time = [(hour.time/3600 -5)%12 + 1 for hour in location.hourly[:24]]
    print ("precip probability next 24 hrs: ")
    for i in range(len(hourprecip)):
        print((str)((int)(time[i])) + ":00 : " + (str)(hourprecip[i]))
            
print('----------------------------------')

#season and temperature-based decisions
seasons = ['fall/winter', 'spring/summer']


#the different styles that I dress in
styles = ("ath", "casual", "bizcasual")

athWinter = []
casualWinter = []
bizcasualWinter = []
athSpring = []
casualSpring = []
bizcasualSpring = []

#my shoes
shoes = []

#makes athleisure, casual, and bizcasual category lists, split again by season - 
with open('closeter.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i in readCSV:
        if((i[3] == 'ath' or i[4] == 'ath') and (i[5] == 'winter' or i[6] == 'winter')):
            athWinter.append(i)
        if((i[3] == 'casual' or i[4] == 'casual') and (i[5] == 'winter' or i[6] == 'winter')):
            casualWinter.append(i)
        if((i[3] == 'bizcasual' or i[4] == 'bizcasual') and (i[5] == 'winter' or i[6] == 'winter')):
            bizcasualWinter.append(i)
        if((i[3] == 'ath' or i[4] == 'ath') and (i[5] == 'spring' or i[6] == 'spring')):
            athSpring.append(i)
        if((i[3] == 'casual' or i[4] == 'casual') and (i[5] == 'spring' or i[6] == 'spring')):
            casualSpring.append(i)
        if((i[3] == 'bizcasual' or i[4] == 'bizcasual') and (i[5] == 'spring' or i[6] == 'spring')):
            bizcasualSpring.append(i)
        if(i[1] == 'shoes' and location.daily[0].precipIntensity > 0.01):
            if(i[5] == 'all'):
                shoes.append(i[0])
        elif(i[1] == 'shoes'):
            shoes.append(i[0])

#I like to start my outfits from the bottom up, choosing shoes first based on weather
#style depending on the weather and occasion
shoeChoice = eval(input("Which shoe to wear today?" + (str)(shoes)))
styleChoice = eval(input("Which style for today?" + (str)(styles)))
seasonChoice = eval(input("Which season is it?" + (str)(seasons)))

if (styleChoice == 0 and seasonChoice == 0):
    li = athWinter
elif (styleChoice == 1 and seasonChoice == 0):
    li = casualWinter
elif (styleChoice == 2 and seasonChoice == 0):
    li = bizcasualWinter
elif (styleChoice == 0 and seasonChoice == 1):
    li = athSpring
elif (styleChoice == 1 and seasonChoice == 1):
    li = casualSpring
elif (styleChoice == 2 and seasonChoice == 1):
    li = bizcasualSpring

def outfitMaker(li):
    if (seasonChoice == 1):
        jacket = ['None']
    else:
        jacket = ['None']
    layer2 = []
    shirt = []
    pants = []
    outfitList = []
    
    for i in range(len(li)):
        if (li[i][1] == 'jacket'):
            jacket.append(li[i][0])
        if (li[i][1] == 'layer2'):
            layer2.append(li[i][0])
        if (li[i][1] == 'shirt'):
            shirt.append(li[i][0])
        if (li[i][1] == 'pants'):
            pants.append(li[i][0])
    
    outfitList.append("Jacket: " + jacket[random.randint(0,len(jacket)-1)])

    #add a jacket if the avg temperature is under 70
    if ((location.daily[0].temperatureMax + location.daily[0].temperatureMin)/2 < 70):
        outfitList.append("Outer: " + layer2[random.randint(0,len(layer2)-1)])
    else:
        outfitList.append("Outer: None")

    #randomly generated outfit
    outfitList.append("Shirt: " + shirt[random.randint(0,len(shirt)-1)])
    outfitList.append("Pants: " + pants[random.randint(0,len(pants)-1)])
    outfitList.append("Shoes: " + shoes[shoeChoice])

    for element in range(len(outfitList)):
        print(outfitList[element])


#run outfitMaker
outfitMaker(li)











