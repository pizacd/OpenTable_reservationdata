# coding: utf-8

'''
OpenTable.py

•Opentable dataset downloaded from https://www.opentable.com/state-of-industry
•Filtered dataframe into separate cities, states and countries
•Plotted time-series data for countries as well as various cities/states in the US
•Created two functions:
    resv_plot: plots time series data from a specific city/state/country to show changes in reservations from the previous year
    usa_plotter: accepts a specific month/day as an argument and returns the reservation data for each US state as a choropleth map.


'''

#importing libraries for the analyses
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
resv = pd.read_csv('https://raw.githubusercontent.com/pizacd/OpenTable_reservationdata/master/YoY_Seated_Diner_Data.csv')


#separate dataframe into cities, states and countries
#Disclaimer: OpenTable did not provide data on all cities, states and countries 
country = resv[resv.Type=='country']
states= resv[resv.Type == 'state']
city = resv[resv.Type == 'city']


#row indices are states, columns are dates of OpenTable data

print(resv.Type.value_counts()) #Breakdown of number of cities, states, and countries OpenTable Collected data on

#plotting a single state's time-series reservation data
#The np.array in the plot is a dotted zero line, indicating no changes in reservations year-over-year.


#plotting the time series data for four countries.
def yelp_cleaning(landtype, name):
    yelp_data = np.transpose(resv.loc[(resv.Type == landtype.lower())&(resv.Name == name.title())])[2:].reset_index()
    yelp_data.columns = ['date','reservations']
    yelp_data.date = pd.to_datetime(yelp_data.date+'/2020')
    yelp_data.reservations = yelp_data.reservations.astype(float)
    return yelp_data

usa,uk,ger = yelp_cleaning('country','United States'),yelp_cleaning('country','United Kingdom'),yelp_cleaning('country','Germany')
ire,can = yelp_cleaning('country','Ireland'),yelp_cleaning('country','Canada')

plt.figure(figsize = (15,10))
plt.plot(usa.date,usa.reservations,'bo:',alpha = 0.6)
plt.plot(uk.date,uk.reservations,'go:',alpha = 0.6)
plt.plot(ger.date,ger.reservations,'yo:',alpha = 0.6)
plt.plot(ire.date,ire.reservations,'mo:',alpha = 0.6)
plt.plot(can.date,can.reservations,'ro:',alpha = 0.6)
plt.plot(usa.date, np.array([0 for zero in range(len(usa.date))]),'k--',alpha = 0.6)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('Country Changes in Reservations Year-over-Year',fontsize = 30, fontweight = 'bold')
plt.legend(('USA','United Kingdom','Germany','Ireland','Canada'),loc = 'upper left',fontsize = 12)
plt.xlabel('Year-Month',fontsize = 18)
plt.ylabel('Percent change from pervious year',fontsize = 18)
plt.figtext(0.5, 0.008, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()

#Filtering time series data for various US cities


hou,bal,nyc = yelp_cleaning('city','Houston'),yelp_cleaning('city','Baltimore'),yelp_cleaning('city','New York')
sea,mia,la,no = yelp_cleaning('city','Seattle'),yelp_cleaning('city','Miami'),yelp_cleaning('city','Los Angeles'),yelp_cleaning('city','New Orleans')



#Plotting the time series data for various US Cities
plt.figure(figsize = (15,10))
plt.plot(hou.date,hou.reservations,'bo:',alpha =0.6)
plt.plot(mia.date,mia.reservations,'ro:',alpha = 0.6)
plt.plot(nyc.date,nyc.reservations,'go:', alpha = 0.6)
plt.plot(sea.date,sea.reservations,'yo:', alpha = 0.6)
plt.plot(no.date,no.reservations,'ko:', alpha = 0.6)
plt.plot(la.date,la.reservations,'mo:', alpha = 0.6)
plt.plot(hou.date,np.array([0 for zero in range(len(hou.date))]),
         'k--',alpha = 0.52)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('City Changes in Reservations Year-over-Year',fontsize = 30, fontweight = 'bold')
plt.legend(('Houston','Miami','New York City','Seattle','New Orleans','Los Angeles'),loc = 'upper right')
plt.xlabel('Year-Month',fontsize = 18)
plt.ylabel('Percent change from pervious year',fontsize = 18)
plt.figtext(0.5, 0.008, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()


#Filtering time series data for various US states
tx,pa,ny,ore, = yelp_cleaning('state','Texas'),yelp_cleaning('state','Pennsylvania'),yelp_cleaning('state','New York'),yelp_cleaning('state','Oregon')
fl,ca,az = yelp_cleaning('state','Florida'),yelp_cleaning('state','California'),yelp_cleaning('state','Arizona')



#Plotting the time series data for various US states
plt.figure(figsize = (15,10))
plt.plot(tx.date,tx.reservations,'bo:',alpha = 0.49)
plt.plot(pa.date,pa.reservations,'ro:',alpha = 0.49)
plt.plot(ny.date,ny.reservations,'go:',alpha = 0.49)
plt.plot(ore.date,ore.reservations,'yo:',alpha = 0.49)
plt.plot(fl.date,fl.reservations,'ko:',alpha = 0.49)
plt.plot(ca.date,ca.reservations,'mo:',alpha = 0.49)
plt.plot(az.date,az.reservations,'co:',alpha = 0.49)
plt.plot(tx.date,np.array([0 for zero in range(len(tx.date))]),
         'k--',alpha = 0.49)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('State Changes in Reservations Year-over-Year',fontsize = 30, fontweight = 'bold',fontname = 'Times New Roman')
plt.legend(('Texas','Pennsylvania','New York','Oregon','Florida','California', 'Arizona'),loc = 'upper right')
plt.xlabel('Year-Month',fontsize = 18, fontname = 'Times New Roman')
plt.ylabel('Percent change from pervious year',fontsize = 18,fontname = 'Times New Roman')
plt.figtext(0.51, 0.008, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()




def resv_plot(land,name):  #land is either a city, state or country. Name is the city/state/country name to extract data from
    geo = resv[resv.Type == land.lower()]
    if land not in ['city','state','country']:
        print("land argument must be either: 'city', 'state' or 'country' and formatted as a string")
    else:
        n = yelp_cleaning(land,name.title())
        
        try:
            plt.figure(figsize = (15,10))
            plt.plot(n.date,n.reservations,'o:')
            plt.plot(n.date,np.array([0 for zero in range(len(n.date))]),'k:')
            plt.xticks(fontsize = 12)
            plt.yticks(fontsize = 12)
            plt.title('{} Changes in Reservations Year-over-Year'.format(name),fontsize = 30, fontweight = 'bold')
            plt.xlabel('Year-Month',fontsize = 18)
            plt.ylabel('Percent change from pervious year',fontsize = 18)
            plt.figtext(0.5, 0.008, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
            plt.show()
        except ZeroDivisionError:
            print('{} is not in the OpenTable dataset'.format(land.capitalize()))
        


resv_plot('city','Austin')

#Importing geopandas and axes libraries to make US map for choropleth
import geopandas as gpd
from shapely.geometry import Point, Polygon
from mpl_toolkits.axes_grid1 import make_axes_locatable
united_states = gpd.read_file('/Users/pizac/Downloads/states_21basic/states.shp')


#Merging .shp file with states dataframe using the state name to merge the two
map_plot = united_states.merge(states.loc[:,['Name',states.columns[-1]]],left_on = 'STATE_NAME', right_on = 'Name')


#Plotting the states' reservation percentages for the most recent day given in the dataset
fig, ax = plt.subplots(1,figsize = (25,15),facecolor = 'lightblue')
ax.set_axis_off()
ax.set_title('States Year-Over-Year Changes in Reservations on {}/20'.format(map_plot.columns[-1]),fontsize = 30,fontweight = 'bold',fontname = 'Comic Sans MS')
ax.annotate('Source: https://opentable.com/state-of-industry',xy = (0.36,0.25),xycoords='figure fraction', fontname = 'Times New Roman', fontsize=18)
divider = make_axes_locatable(ax)
cax = divider.append_axes('right',size = '3%',pad = .05)
map_plot.dropna().plot(column=map_plot.columns[-1],ax = ax,cax = cax, cmap = 'hot',edgecolor = 'k',   
                                  k=4, legend =  True);
plt.show()



#Plots the states' reservation percentages on whichever date is provided as the argument
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


