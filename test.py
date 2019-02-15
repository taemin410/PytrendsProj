"""
pytrends library practice 2

Mainly focus on Object oriented programming
test case file

version : 1.0 v
Author : Tae Min Ha

"""
from trendfunc import *
from trendclass import *

dict={}
dict["kw_list"] = ["Apple", "Samsung"]
dict["timeframe"]= "today 5-y"

dum="dummy string"
"""
Functional call with scripts of functions
just works for one or more functions.

If we want to do other functions we need to 
exclusively define more functions or we have to use 
if/else or switches to know which function we are calling
"""
get_Trend(dum, dict)

print_dummy(dum, dict)


"""
Object-oriented programming using classes
"""
trendobj= trendclass("today 5-y", ["Apple"])

trendobj.get_trend()
trendobj.functionsForAnyUse()

"""
The advantage of Object oriented programming is that 
it can privately keep its own variables,
it can use those data to do other functions if class has it defined
it can be modified and used anywhere else if it is designed carefully.

Note that the libraries that we have been calling were all 
objects that is pre-defined by others 

If our project is carefully designed and uploaded somewhere,
people can actually use it by just calling its name.( object)

"""