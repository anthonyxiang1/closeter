# Closeter - outfit creating app

A outfit selecting app given a csv file of the user's wardrobe - includes decision automation using weather based features through DarkSky API.

## Inspiration/About
For my personal inability to decide what to wear, to combat decision fatigue and wasted time during the morning. Creates an outfit based on three inputs - style, season, and shoe. Uses DarkSky API to make decisions based on weather and reads clothes from a CSV file. Automates certain decisions based on the weather - specifically temperature and precipitation probability.

## Usage
1. Using Notepad, input clothes that you want to wear in the following format:

- name,type,color,style1,style2,weather1,weather2

- name does not have to be specific, as long as you know which clothing piece you are referring to.

- For shoes, weather1 has inputs: all | no rain

- (See the csv file attached as an example.)

2. Download files and run closeter.py in terminal

3. Select choices using the list index: if it asks [fall, winter], input '0' for fall and '1' for winter.
