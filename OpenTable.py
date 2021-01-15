'''
•Opentable dataset downloaded from https://www.opentable.com/state-of-industry
•Filtered dataframe into separate cities, states and countries
•Plotted time-series data for countries as well as various cities/states in the US

•Created three functions:
    resv_plot: plots time series data from a specific city/state/country to show YoY changes in reservations.
    usa_plotter: accepts a specific month/day as an argument and returns the reservation data as a choropleth map.


'''

#importing libraries for the analyses
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
resv = pd.read_csv('https://raw.githubusercontent.com/pizacd/OpenTable_reservationdata/master/YoY_Seated_Diner_Data.csv')

food =pd.melt(resv,id_vars = ['Name','Type'])
food.columns= ['Name','LandType','Date','PctChange']
food.Date = pd.to_datetime(food.Date+'/20')
food.PctChange=food.PctChange.astype(float)


#separate dataframe into cities, states and countries
#Disclaimer: OpenTable did not provide data on all cities, states and countries 
country = food[food.LandType=='country']
states= food[food.LandType == 'state']
city = food[food.LandType == 'city']


#row indices are cities, countries or states. columns are dates of OpenTable data

print(resv.Type.value_counts()) #Breakdown of number of cities, states, and countries OpenTable Collected data on


usa,uk = country.loc[country.Name =='United States'],country.loc[country.Name == 'United Kingdom'],
ger = country.loc[country.Name =='Germany']
ire,can = country.loc[country.Name =='Ireland'], country.loc[country.Name == 'Canada']

#Lineplot 
plt.figure(figsize = (15,10))
plt.plot(usa.Date,usa.PctChange,'bo:',alpha = 0.6)
plt.plot(uk.Date,uk.PctChange,'go:',alpha = 0.6)
plt.plot(ger.Date,ger.PctChange,'yo:',alpha = 0.6)
plt.plot(ire.Date,ire.PctChange,'mo:',alpha = 0.6)
plt.plot(can.Date,can.PctChange,'ro:',alpha = 0.6)

#The np.array in the plot is a dotted zero line, indicating no changes in reservations year-over-year.
plt.plot(usa.Date, np.array([0 for zero in range(len(usa.Date))]),'k--',alpha = 0.6)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('Country Changes in Reservations Year-over-Year',fontsize = 30, fontweight = 'bold')
plt.legend(('USA','United Kingdom','Germany','Ireland','Canada'),loc = 'upper left',fontsize = 12)
plt.xlabel('Year-Month',fontsize = 18)
plt.ylabel('Percent change from pervious year',fontsize = 18)
plt.figtext(0.5, 0.008, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()



#Filtering time series data for various US cities

hou,bal = city.loc[city.Name == 'Houston'],city.loc[city.Name == 'Baltimore']
nyc = city.loc[city.Name == 'New York']
sea,mia = city.loc[city.Name == 'Seattle'], city.loc[city.Name == 'Miami']
La,no = city.loc[city.Name == 'Los Angeles'],city.loc[city.Name == 'New Orleans']

#Plotting the time series data for various US Cities
plt.figure(figsize = (15,10))
plt.plot(hou.Date,hou.PctChange,'bo:',alpha =0.6)
plt.plot(mia.Date,mia.PctChange,'ro:',alpha = 0.6)
plt.plot(nyc.Date,nyc.PctChange,'go:', alpha = 0.6)
plt.plot(sea.Date,sea.PctChange,'yo:', alpha = 0.6)
plt.plot(no.Date,no.PctChange,'ko:', alpha = 0.6)
plt.plot(La.Date,La.PctChange,'mo:', alpha = 0.6)
plt.plot(hou.Date,np.array([0 for zero in range(len(hou.Date))]),
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
tx, pa = states.loc[states.Name == 'Texas'], states.loc[states.Name == 'Pennsylvania']
ny, ore = states.loc[states.Name == 'New York'], states.loc[states.Name == 'Oregon']
fl,ca = states.loc[states.Name == 'Florida'], states.loc[states.Name == 'California']
az = states.loc[states.Name == 'Arizona'] 



#Plotting the time series data for various US states
plt.figure(figsize = (15,10))
plt.plot(tx.Date,tx.PctChange,'bo:',alpha = 0.49)
plt.plot(pa.Date,pa.PctChange,'ro:',alpha = 0.49)
plt.plot(ny.Date,ny.PctChange,'go:',alpha = 0.49)
plt.plot(ore.Date,ore.PctChange,'yo:',alpha = 0.49)
plt.plot(fl.Date,fl.PctChange,'ko:',alpha = 0.49)
plt.plot(ca.Date,ca.PctChange,'mo:',alpha = 0.49)
plt.plot(az.Date,az.PctChange,'co:',alpha = 0.49)
plt.plot(tx.Date,np.array([0 for zero in range(len(tx.Date))]),
         'k--',alpha = 0.49)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('State Changes in Reservations Year-over-Year',fontsize = 30, fontweight = 'bold',fontname = 'Times New Roman')
plt.legend(('Texas','Pennsylvania','New York','Oregon','Florida','California', 'Arizona'),loc = 'upper right')
plt.xlabel('Year-Month',fontsize = 18, fontname = 'Times New Roman')
plt.ylabel('Percent change from pervious year',fontsize = 18,fontname = 'Times New Roman')
plt.figtext(0.51, 0.008, 'Source: opentable.com/state-of-industry', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()




def resv_plot(land,name):  
	"""
	Returns an individual line plot for a specific city, state or country.

	Args:
		land is either a city, state or country. 
		name is the city/state/country name to extract data from

	"""

	geo = food[food.LandType == land.lower()]
	if land not in ['city','state','country']:
	    print("land argument must be either: 'city', 'state' or 'country' and formatted as a string")
	else:
	    reserv = geo.loc[geo.Name == name.title()]
	    
	    try:
	        plt.figure(figsize = (15,10))
	        plt.plot(reserv.Date,reserv.PctChange,'o:')
	        plt.plot(reserv.Date,np.array([0 for zero in range(len(reserv.Date))]),'k:')
	        plt.xticks(fontsize = 12)
	        plt.yticks(fontsize = 12)
	        plt.title('{} Changes in Reservations Year-over-Year'.format(name),fontsize = 30, fontweight = 'bold')
	        plt.xlabel('Year-Month',fontsize = 18)
	        plt.ylabel('Percent change from pervious year',fontsize = 18)
	        plt.figtext(0.5, 0.008, 'Source: opentable.com/state-of-industry', 
	        	wrap=True, horizontalalignment='center', fontsize=12)
	        plt.show()
	    except ZeroDivisionError:
	        print('{} is not in the OpenTable dataset'.format(land.capitalize()))
        


resv_plot('city','Austin')

#Importing geopandas and axes libraries to make US map for choropleth
import geopandas as gpd
from shapely.geometry import Point, Polygon
from mpl_toolkits.axes_grid1 import make_axes_locatable
united_states = gpd.read_file('~/Downloads/states_21basic/states.shp')


#Merging .shp file with states dataframe using the state name to merge the two
map_plot = united_states.merge(states.loc[:,['Name','Date','PctChange']],left_on = 'STATE_NAME', right_on = 'Name')
map_plot = map_plot.loc[map_plot.Date == map_plot.Date.iloc[-1].date()]

#Plotting the states' reservation percentages for the most recent day given in the dataset
fig, ax = plt.subplots(1,figsize = (25,15),facecolor = 'lightblue')
ax.set_axis_off()
ax.set_title('States Year-Over-Year Changes in Reservations on {}'.format(map_plot.Date.iloc[-1].date()),
	fontsize = 30,fontweight = 'bold',fontname = 'Times New Roman')
ax.annotate('Source: https://opentable.com/state-of-industry',
	xy = (0.36,0.25),xycoords='figure fraction', fontname = 'Times New Roman', fontsize=18)
divider = make_axes_locatable(ax)
cax = divider.append_axes('right',size = '3%',pad = .05)
map_plot.dropna().plot(column='PctChange',ax = ax,cax = cax, cmap = 'hot',edgecolor = 'k',   
                                  k=4, legend =  True);
plt.show()




def usa_plotter(date):
	"""
	Returns a choropleth map of the USA's reservation percentages YoY on whichever date is provided as the argument.

	Args:
		date: selects the column of OpenTable data for that respective month/day of 2020 
	"""

	import geopandas as gpd
	from shapely.geometry import Point, Polygon
	from mpl_toolkits.axes_grid1 import make_axes_locatable
	united_states = gpd.read_file('/Users/pizac/Downloads/states_21basic/states.shp')
	map_plot = united_states.merge(states.loc[:,['Name','Date','PctChange']],left_on = 'STATE_NAME', right_on = 'Name')
	map_plot = map_plot.loc[map_plot.Date == date]
	fig, ax = plt.subplots(1,figsize = (25,15),facecolor = 'lightblue')
	ax.set_axis_off()
	ax.set_title('States Year-Over-Year Changes in Reservations on {}'.format(map_plot.Date.iloc[-1].date()),
		fontsize = 30,fontweight = 'bold',fontname = 'Times New Roman')
	ax.annotate('Source: https://opentable.com/state-of-industry',xy = (0.36,0.25),
		xycoords='figure fraction', fontname = 'Times New Roman', fontsize=18)
	divider = make_axes_locatable(ax)
	cax = divider.append_axes('right',size = '3%',pad = .05)
	map_plot.dropna().plot(column = 'PctChange',ax = ax,cax = cax, cmap = 'hot',edgecolor = 'k',   
	                              k=4, legend =  True);
	plt.show()


