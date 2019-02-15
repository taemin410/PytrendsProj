"""
pytrends library practice 1

Mainly focus on downloading data from google trends and
using libraries of python

version : 1.0 v
Author : Tae Min Ha
"""

"""
import necessary libraries at the beginning

To do this, python should be available on the device

1. Prepare python with version higher than 3.4
2. Run: `pip install pytrends` on commandline 
3. Run: `pip install matplotlib` on commandline

*check for `python -V` to check for python version

**note that a lot of libraries are installed in anaconda program 
however, if the environment variable for windows is not established appropriately,
python command would not work on your command prompt

*** pip is a installer that python provides for users to 
easily download libraries that others have uploaded on internet


"""
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime


#Initialize pytrends class with TrendReq function ( hl : header language / tz = timezone which is set for 360 for US)
pytrends = TrendReq(hl='en-EN', tz=360)


#Key word list for trend search
kw_list = ["Iphone Xr", "Apple", "Samsung", "Galaxy S9"]


#Make a payload which brings trend data from google trend
#A lot of parameters can be used such as geo: region, timeframe, etc...)
pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='', gprop='')


"""another way to call for data, there are several funcions in pytrends library, see 
https://github.com/GeneralMills/pytrends/blob/master/README.md
"""
# data= pytrends.get_historical_interest(kw_list, year_start=2018,
#                                  month_start=1, day_start=1, hour_start=0, year_end=2018,
#                                  month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)


#For our case, we look into interest_over_time() function's return value
#This function returns a dataFrame (pandas)
data= pytrends.interest_over_time()

#Trivial function that helps convert datetime object, you can ignore this for now
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()



"""
Printing is not just used for printing messages.
Essentially, print() in programming make use of printing 
as for programmers to easily debug and identify code and its progress.

Try uncommenting three to see what it does! 
"""
#print(data)
#print(data.shape)
#print(data.columns)
"""
Note that if we bring several keywords together,
then, the trend data is regularized into same data volume
EX) 
if 1000 search queries compared to 10000 queries, then 
the number is likely to become 1:10 ratio.
However, how the trend data is calculated is not fully known for google Trend.

"""


#We store the data in x, y variable to plot graph using data retrieved
x=data.index.values
y=data[kw_list]

#We use matplotlib.pyplot library for simple plotting
plt.plot(x, y.Apple)
plt.plot(x, y.Samsung)
plt.plot(x, y["Iphone Xr"])
plt.plot(x, y["Galaxy S9"])

plt.legend(['Apple', 'Samsung', 'Iphone Xr', 'Galaxy S9'], loc='upper left')
plt.title("Trends data from the past three months")
plt.xlabel("Time")
plt.ylabel("Items")
__, labels = plt.xticks()
plt.setp(labels, rotation=45)

plt.show()

print(data.head())

import os
# if file does not exist write header
if not os.path.isfile('trend_data.csv'):
   data.to_csv('trend_data.csv', header='column_names')
else: # else it exists so append without writing the header
   data.to_csv('trend_data.csv', mode='a', header=False)


# data.to_csv("trend_data.csv")



#exit is written to forbid plotly plotting
exit()


"""
Ploting utility using plotly
Mainly deals with interactive Graphs
"""
import plotly
import plotly.graph_objs as go

Apple = go.Scatter(
                x=data.index,
                y=data['Apple'],
                name = "Apple",
                line = dict(color = '#17BECF'),
                opacity = 0.8)
Iphone_Xr = go.Scatter(
                x=data.index,
                y=data['Iphone Xr'],
                name = "Iphone Xr",
                opacity = 0.8)
Galaxy_S9 = go.Scatter(
                x=data.index,
                y=data['Galaxy S9'],
                name = "Galaxy S9",
                opacity = 0.8)
Samsung = go.Scatter(
                x=data.index,
                y=data['Samsung'],
                name = "Samsung",
                opacity = 0.8)

data= [Apple, Iphone_Xr, Samsung, Galaxy_S9]

layout = dict(
    title = "Apple & Samsung Phone trend",
)
fig = dict(data=data, layout=layout)


plotly.offline.plot(fig, filename = "Apple & Samsung Phone trend" , auto_open=True)

