#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
resv = pd.read_csv('https://raw.githubusercontent.com/pizacd/OpenTable_reservationdata/master/YoY_Seated_Diner_Data.csv')


#separate dataframe into cities, states and countries
#Disclaimer: OpenTable did not provide data on all cities, states and countries 
country = resv[resv.Type=='country']
states= resv[resv.Type == 'state']
city = resv[resv.Type == 'city']


states.describe() #row indices are states, columns are dates of OpenTable data



resv.Type.value_counts() #Breakdown of number of cities, states, and countries OpenTable Collected data on



plt.figure(figsize = (15,10))
plt.plot(np.transpose(states[states.Name=='Maryland'])[2:],'bo:',np.array([0 for zero in range(len(np.transpose(states[states.Name =='Maryland'])[2:]))]),
         'k--',) #Using the transpose so reservation dates become rows
plt.xticks(states[states.Name=='Maryland'].columns[2::7],fontsize = 12) #Separating the xticks by week to make less cluttered
plt.yticks(fontsize = 12)
plt.title("Maryland's Year-over-Year Change in Reservations",fontsize = 30,fontweight = 'bold')
plt.xlabel('Month/day in 2020', fontsize = 18)
plt.ylabel('Change in Reservations YOY (percent)',fontsize = 18)
plt.figtext(0.5, 0.04, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()


usa = country[country.Name == 'United States']
uk = country[country.Name == 'United Kingdom']
ger = country[country.Name =='Germany']
can = country[country.Name =='Canada']
plt.figure(figsize = (15,10))
plt.plot(np.transpose(usa)[2:],'bo:',np.transpose(uk)[2:],'go:',np.transpose(ger)[2:],'yo:',np.transpose(can)[2:],'ro:',
         np.array([0 for zero in range(len(np.transpose(country[country.Name =='United Kingdom'])[2:]))]),
         'k--',alpha = 0.6)
plt.xticks(usa.columns[2::7],fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('Country Changes in Reservations Year-over-Year',fontsize = 30, fontweight = 'bold')
plt.legend(('USA','United Kingdom','Germany','Canada'),loc = 'upper left',fontsize = 12)
plt.xlabel('Month/Day in Year 2020',fontsize = 18)
plt.ylabel('Percent change from pervious year',fontsize = 18)
plt.figtext(0.5, 0.04, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()


hou = np.transpose(city[city.Name == 'Houston'])[2:]
bal = np.transpose(city[city.Name == 'Baltimore'])[2:]
nyc = np.transpose(city[city.Name == 'New York'])[2:]
sea = np.transpose(city[city.Name == 'Seattle'])[2:]
mia = np.transpose(city[city.Name == 'Miami'])[2:]
la = np.transpose(city[city.Name == 'Los Angeles'])[2:]
no = np.transpose(city[city.Name == 'New Orleans'])[2:]



plt.figure(figsize = (15,10))
plt.plot(hou,'bo:',mia,'ro:',nyc,'go:',sea,'yo:',no,'ko:',
         la,'mo:',
         np.array([0 for zero in range(len(np.transpose(city[city.Name =='Baltimore'])[2:]))]),
         'k--',alpha = 0.52)
plt.xticks(usa.columns[2::7],fontsize = 12)
plt.xticks(usa.columns[2::7],fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('City Changes in Reservations Year-over-Year',fontsize = 30, fontweight = 'bold')
plt.legend(('Houston','Miami','New York City','Seattle','New Orleans','Los Angeles'),loc = 'upper right')
plt.xlabel('Month/Day in Year 2020',fontsize = 18)
plt.ylabel('Percent change from pervious year',fontsize = 18)
plt.figtext(0.5, 0.04, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()


tx = np.transpose(states[states.Name == 'Texas'])[2:]
pa = np.transpose(states[states.Name == 'Pennsylvania'])[2:]
ny = np.transpose(states[states.Name == 'New York'])[2:]
ore = np.transpose(states[states.Name == 'Oregon'])[2:]
fl = np.transpose(states[states.Name == 'Florida'])[2:]
ca = np.transpose(states[states.Name == 'California'])[2:]
az = np.transpose(states[states.Name == 'Arizona'])[2:]



plt.figure(figsize = (15,10))
plt.plot(tx,'bo:',pa,'ro:',ny,'go:',ore,'yo:',fl,'ko:',
         ca,'mo:', az,'co:',
         np.array([0 for zero in range(len(np.transpose(city[city.Name =='Baltimore'])[2:]))]),
         'k--',alpha = 0.49)
plt.xticks(usa.columns[2::7],fontsize = 12)
plt.xticks(usa.columns[2::7],fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('State Changes in Reservations Year-over-Year',fontsize = 30, fontweight = 'bold',fontname = 'Times New Roman')
plt.legend(('Texas','Pennsylvania','New York','Oregon','Florida','California', 'Arizona'),loc = 'upper right')
plt.xlabel('Month/Day in Year 2020',fontsize = 18, fontname = 'Times New Roman')
plt.ylabel('Percent change from pervious year',fontsize = 18,fontname = 'Times New Roman')
plt.figtext(0.51, 0.04, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()




def resv_plot(land,name):  #land is either a city, state or country. Name is the city/state/country name to extract data from
    geo = resv[resv.Type == land]
    if land not in ['city','state','country']:
        print('land argument must be either: city, state or country and formatted as a string')
    else:
        n = geo[geo.Name == name]
        
        try:
            plt.figure(figsize = (15,10))
            plt.plot(np.transpose(n)[2:],'o:' ,np.array([0 for zero in range(len(np.transpose(n)[2:]))]),'k:')
            plt.xticks(geo.columns[2::7],fontsize = 12)
            plt.yticks(fontsize = 12)
            plt.title('{} Changes in Reservations Year-over-Year'.format(name),fontsize = 30, fontweight = 'bold')
            plt.xlabel('Month/Day in Year 2020',fontsize = 18)
            plt.ylabel('Percent change from pervious year',fontsize = 18)
            plt.figtext(0.5, 0.04, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
            plt.show()
        except ZeroDivisionError:
            print('{} is not in the OpenTable dataset'.format(land.capitalize()))
        


resv_plot('city','Baltimore')


import geopandas as gpd
from shapely.geometry import Point, Polygon
from mpl_toolkits.axes_grid1 import make_axes_locatable
united_states = gpd.read_file('/Users/pizac/Downloads/states_21basic/states.shp')



map_plot = united_states.merge(states.loc[:,['Name',states.columns[-1]]],left_on = 'STATE_NAME', right_on = 'Name')



fig, ax = plt.subplots(1,figsize = (25,15),facecolor = 'lightblue')
ax.set_axis_off()
ax.set_title('States Year-Over-Year Changes in Reservations on {}/20'.format(map_plot.columns[-1]),fontsize = 30,fontweight = 'bold',fontname = 'Comic Sans MS')
ax.annotate('Source: https://opentable.com/state-of-industry',xy = (0.36,0.25),xycoords='figure fraction', fontname = 'Comic Sans MS', fontsize=18)
divider = make_axes_locatable(ax)
cax = divider.append_axes('right',size = '3%',pad = .05)
map_plot.dropna().plot(column=map_plot.columns[-1],ax = ax,cax = cax, cmap = 'hot',edgecolor = 'k',   
                                  k=4, legend =  True);
plt.show()




def usa_plotter(date): #day argument selects the column of OpenTable data for that respective month/day of 2020 
    import geopandas as gpd
    from shapely.geometry import Point, Polygon
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    united_states = gpd.read_file('/Users/pizac/Downloads/states_21basic/states.shp')
    map_plot = united_states.merge(states.loc[:,['Name',date]],left_on = 'STATE_NAME', right_on = 'Name')
    fig, ax = plt.subplots(1,figsize = (25,15),facecolor = 'lightblue')
    ax.set_axis_off()
    ax.set_title('States Year-Over-Year Changes in Reservations on {}/20'.format(map_plot.columns[-1]),fontsize = 30,fontweight = 'bold',fontname = 'Comic Sans MS')
    ax.annotate('Source: https://opentable.com/state-of-industry',xy = (0.36,0.25),xycoords='figure fraction', fontname = 'Comic Sans MS', fontsize=18)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right',size = '3%',pad = .05)
    map_plot.dropna().plot(column=map_plot.columns[-1],ax = ax,cax = cax, cmap = 'hot',edgecolor = 'k',   
                                  k=4, legend =  True);
    plt.show()


