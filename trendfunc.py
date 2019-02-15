"""
pytrends library practice 2

Mainly focus on Object oriented programming
functions file

version : 1.0 v
Author : Tae Min Ha
"""

from pytrends.request import TrendReq
#import matplotlib.pyplot as plt


def get_Trend(data, dict):
    pytrends = TrendReq(hl='en-EN', tz=360)

    kw_list = dict["kw_list"]
    timeframe=dict["timeframe"]

    pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='', gprop='')

    data = pytrends.interest_over_time()

    print(data.head())


def print_dummy(dum, dict):
    print(dum)
    print(dict)
