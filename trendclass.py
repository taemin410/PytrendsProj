"""
pytrends library practice 2

Mainly focus on Object oriented programming
class object file

version : 1.0 v
Author : Tae Min Ha
"""

from pytrends.request import TrendReq

class trendclass():
    def __init__(self,timef, kwlist):
        #initialize the object with constructor
        self.timeFrame = timef
        self.keywordList= kwlist


    def get_trend(self):
        pytrends = TrendReq(hl='en-EN', tz=360)

        kw_list = self.keywordList
        timeframe = self.timeFrame

        pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='', gprop='')

        data = pytrends.interest_over_time()

        print(data.head())


    def functionsForAnyUse(self):
        print(self.timeFrame)
        print(self.keywordList)

        print("You can use classes to have variables of its own and "
              "you can use those variables to act in different way ")


