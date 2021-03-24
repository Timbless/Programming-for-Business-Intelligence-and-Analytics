# -*- coding: utf-8 -*-
"""income_disparity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1upuHuQ3gWDkpbvkvHl2uTQlSv20JZnf2
"""

!pip install wbdata
#!pip install pandas-datareader
import wbdata
import datetime
import numpy as np
import pandas as pd
from pandas_datareader import wb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as lr
from matplotlib.pyplot import MultipleLocator


# =============================================================================
# # Part 1: API Integration
# =============================================================================

# =============================================================================
# # API method 1: using wbdata module
# =============================================================================

# #searching for countries index using names
# print(wbdata.search_countries('United Kingdom'))

# list of countries
countries = ["USA", "BEL", "BRA", "COL", "FRA", "DEU", "GRC", "IDN", "IRL", "MEX", "NLD", "RUS"]
# date period
dates = datetime.datetime(2008, 1, 1), datetime.datetime(2018, 1, 1)

# data object
indicators = {'SI.DST.05TH.20':'Income share held by highest 20%', 'SI.DST.FRST.20': 'Income share held by lowest 20%', \
             'SL.EMP.TOTL.SP.FE.NE.ZS': 'Employment to population ratio, 15+, female (%) (national estimate)',\
             'SL.EMP.TOTL.SP.MA.NE.ZS': 'Employment to population ratio, 15+, male (%) (national estimate)'}

# getting data from these countries
raw_data = wbdata.get_dataframe(indicators, country=countries, data_date=dates, convert_date=True)

raw_unstacked_data = raw_data.unstack(level=0)

# printing our data object
# print(raw_data)
# print(raw_unstacked_data)

# =============================================================================
# # API method 2: using from pandas.datareader import wb, convert the data object to a DataFrame 
# =============================================================================

# view all data
pd.set_option('display.max_columns', 15) 
pd.set_option('display.max_rows', 15) 

df1 = wb.download(indicator = indicators, country = countries,  start = 2008, end = 2018)
date_period = [i for i in range(2008, 2019)]
print(df1)

# create a new DataFrame df2 for later use, not change origin values from df1 if we do some calculations for our dataframe df2
# rename the columns name
df2 = df1.rename(columns = {'SI.DST.05TH.20':'Income share held by highest 20%', 'SI.DST.FRST.20': 'Income share held by lowest 20%', \
             'SL.EMP.TOTL.SP.FE.NE.ZS': 'Employment to population ratio, 15+, female (%) (national estimate)',\
             'SL.EMP.TOTL.SP.MA.NE.ZS': 'Employment to population ratio, 15+, male (%) (national estimate)'}, inplace = False)

# overview our data object DataFrame
# Data manipulation: dealing with the missing value, replace them as mean(), which has less impact on our data sets
df2.mean()
df2.fillna(df2.mean(), inplace = True)
print(df2)

# Overview our new edited DataFram and get basic info of statistics
print(df2.describe())




# =============================================================================
# # Part 2: Data structure set up
# =============================================================================

# =============================================================================
# # creating our Data Structure type I
# =============================================================================

# step I: convert DataFrame to a list in correct order from 2008 to 2018
def country_DataFrame_to_list(country, target_data):
  df = wb.download(indicator = target_data, country = country,  start = 2008, end = 2018)
  df.fillna(df.mean(), inplace = True)
  df_list =df[df.columns[0]].tolist()
  round_list = [round(i, 2) for i in df_list ]
  return round_list[::-1]

# step II: make a list of tuple, which is a good way to save our data
def country_tuples(country_list, time):
  return list(zip(country_list, time))

# additional gap calculation for calculating the gap between two list
def gap_between(toplist, lowlist):
  gap_list = []
  for i in range(len(toplist)):
    gap_list.append(round((toplist[i]- lowlist[i]), 2))
  return gap_list



# step IV: Make a dictionary of list of tuple, which is one of our data structure of this project,
# named as Data Structure type I.
def object_Dictionary(country_list, object_target, date_period):
  object_df = {}
  for country in country_list:
    object_df[country] = country_tuples(date_period, country_DataFrame_to_list(country, object_target))
  return object_df

# step V: start to build: 
    
    
# This data set is for storing data of Income share held by highest 20%
Top_20_df = object_Dictionary(countries, 'SI.DST.05TH.20', date_period)

# This data set is for storing data of Income share held by lowest 20%
Low_20_df = object_Dictionary(countries, 'SI.DST.FRST.20', date_period)

# This data set is for storing data of 'Employment to population ratio, 15+, female (%) (national estimate)'
female_employ_df = object_Dictionary(countries, 'SL.EMP.TOTL.SP.FE.NE.ZS', date_period)

# This data set is for storing data of 'Employment to population ratio, 15+, male (%) (national estimate)'
male_employ_df = object_Dictionary(countries, 'SL.EMP.TOTL.SP.MA.NE.ZS', date_period)




# =============================================================================
# # creating our Data Structure type II: convert our Data structure type I to typle II
# =============================================================================
# step 1: write a function that can unpack dictionary of tuple to a new dictionary of simple list, and calculate the gap
def no_tuple_dic(object_Dictionary1, object_Dictionary2):
  new_dict = {}
  for i in countries:
    new_list = []
    for j in range(11):
      # The reason why I didn't use the difference function is because I don't want my new dictionary has year
      new_list.append(round((object_Dictionary1[i][j][1]- object_Dictionary2[i][j][1]), 2)) 
    new_dict[i] = new_list  

  return new_dict

# step 2: getting the income gap dictionary of list between income share held by highest 20% and income share held by lowest 20%
income_gap_dict = no_tuple_dic(Top_20_df, Low_20_df)

# step 3: create our Data structure type II, DataFrame
income_gap_dict_df = pd.DataFrame(income_gap_dict, columns = countries)

# step 4: show the basic statistic info of our income gap DataFrame
print(round(income_gap_dict_df.describe(),2))

# same step as above, to get our Data Structure type II, between male employment population and female employment population
gender_gap_dict = no_tuple_dic(male_employ_df, female_employ_df)

gender_gap_dict_df = pd.DataFrame(gender_gap_dict, columns = countries)
print(round(gender_gap_dict_df.describe(),2))



# Data Structure function application

# This function is to calculate the difference of the gap between income share held by highest 20% and income share held by lowest 20%
def gap_income_Dataframe(country):
  gap = {}
  for i in range(len(Top_20_df[country])):
    year1, data1 = Top_20_df[country][i]
    year2, data2 = Low_20_df[country][i]  
    if year1 == year2:
      gap[year1] = round(data1-data2, 2)
  return gap

# This function is to calculate the difference of the gap between male employment population and female employment population
def gap_gender_Dataframe(country):
  gap = {}
  for i in range(len(Top_20_df[country])):
    year1, data1 = male_employ_df[country][i]
    year2, data2 = female_employ_df[country][i]  
    if year1 == year2:
      gap[year1] = round(data1-data2, 2)
  return gap

# This function is to searching specific country and year  
def searching_data(object_Dictionary, country, year):
  country_list = []
  if country in countries:
    for i in range(11):
      country_list.append(object_Dictionary[country][i])
  
  output = [item for item in country_list if item[0] == year]
  #return empty list if data not found, return a tuple if country and year is valid    
  return output





# =============================================================================
# # Part 3: Ploting the data set
# =============================================================================


# =============================================================================
# #plot 1: Income gap from 2008 to 2018
# =============================================================================

from matplotlib.pyplot import MultipleLocator
plt.title('Income gap from 2008 to 2018')
plt.xlabel('Year')
plt.ylabel('Income gap%')
all_data_i = []

for c in countries:
  gap_i = gap_income_Dataframe(c)
  x_i = gap_i.keys()
  y_i = gap_i.values()
  all_data_i.append(gap_i)
  plt.scatter(x_i,y_i,marker='+',label=c)
  plt.legend(loc=2,bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)

x_major_locator=MultipleLocator(1)  #set the x interval as 1
y_major_locator=MultipleLocator(2)   #set the y interval as 2
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)     #Set the major scale of the x-axis to a multiple of 1
ax.yaxis.set_major_locator(y_major_locator)     #Set the major scale of the y-axis to a multiple of 2
plt.xlim(2007,2019)   #Set the x scale range of the x-axis from 2008 to 2018， the reason why I use 2019 is because we can see clearly t 
plt.ylim(25,60)     #Set the y scale range of the y-axis from 25 to 60

N = 10000
xr_i = list(range(2008,2019))
yr_i = []
for i in xr_i:
  temp = 0
  for j in all_data_i:
    temp += j[i]
  temp /= len(countries)
  yr_i.append(temp)
plt.plot(xr_i,yr_i,"r-",label='average')
plt.legend(loc=2,bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
plt.savefig('Income gap.pdf')  
plt.show()

# =============================================================================
# #plot 2: Gender Employment rate gap from 2008 to 2018
# =============================================================================

plt.title('Gender Employment rate gap from 2008 to 2018')
plt.xlabel('Year')
plt.ylabel('Gender Employment Gap %')
all_data_j = []
for c in countries:
  gap_j = gap_gender_Dataframe(c)
  x_j = gap_j.keys()
  y_j = gap_j.values()
  all_data_j.append(gap_j)
  plt.scatter(x_j,y_j,marker='+',label=c)
  plt.legend(loc=2,bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)

x_major_locator=MultipleLocator(1)  #set the x interval as 1
y_major_locator=MultipleLocator(2)   #set the y interval as 2
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)     #Set the major scale of the x-axis to a multiple of 1
ax.yaxis.set_major_locator(y_major_locator)     #Set the major scale of the y-axis to a multiple of 0.02
plt.xlim(2007,2019)   #Set the scale range of the x-axis from 2008 to 2018
plt.ylim(6,38)     #Set the scale range of the y-axis from 25 to 60

N = 10000
xr_j = list(range(2008,2019))
yr_j = []
for i in xr_j:
  temp = 0
  for j in all_data_j:
    temp += j[i]
  temp /= len(countries)
  yr_j.append(temp)
plt.plot(xr_j,yr_j,"r-",label='average')
plt.legend(loc=2,bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
plt.show()

# =============================================================================
# #boxplot 1 income gap
# =============================================================================

plt.figure(figsize=(9,6),dpi=60)

labels, data = [*zip(*income_gap_dict.items())]  # 'transpose' items to parallel key, value lists

# or backwards compatable    
labels, data = income_gap_dict.keys(), income_gap_dict.values()
plt.title('Income Gap from 2008 to 2018')
plt.xlabel('Country')
plt.ylabel('Income Gap %')
plt.boxplot(data)
plt.xticks(range(1, len(labels) + 1), labels)
plt.show()

# =============================================================================
# #boxplot 2 gender employment gap
# =============================================================================

plt.figure(figsize=(9,6),dpi=60)

labels, data = [*zip(*gender_gap_dict.items())]  # 'transpose' items to parallel key, value lists

# or backwards compatable    
labels, data = gender_gap_dict.keys(), gender_gap_dict.values()
plt.title('Gender Employment Gap')
plt.xlabel('Country')
plt.ylabel('Gender Employment Gap %')
plt.boxplot(data)
plt.xticks(range(1, len(labels) + 1), labels)
plt.show()

# =============================================================================
# #Part 4: linear regression
# =============================================================================

import numpy as np
from sklearn.linear_model import LinearRegression

# Convert the original data frame to list
def convert_to_target_data_dict(country_list):
    converted_dict = {}

    for i in range(len(country_list)):
        country_name = country_list[i]
        converted_dict[country_name] = {}
        gap_income_dict = gap_income_Dataframe(country_name)
        gap_gender_dict = gap_gender_Dataframe(country_name)
        converted_gap_income_list = []
        converted_gap_gender_list = []

        for k in gap_income_dict:
            converted_gap_income_list.append(gap_income_dict[k])
            converted_gap_gender_list.append(gap_gender_dict[k])

        converted_dict[country_name]["income"] = converted_gap_income_list
        converted_dict[country_name]["gender"] = converted_gap_gender_list

    return converted_dict


# Work out the x-coordinates for linear regression
def x_coordinate():
    x_list = []
    x_coordinate = 2008
    for i in range(11):
        x_list.append(x_coordinate)
        x_coordinate = x_coordinate + 1

    return x_list


# Work out the linear regression for single country
def linear_regression(contry_name, coordinate_dict, data_type, predict_time):
    y_list = coordinate_dict[contry_name][data_type]
    x_list = x_coordinate()
    x = np.array(x_list).reshape((-1, 1))
    y = np.array(y_list)

    linear_model = LinearRegression().fit(x, y)

    predict_year = np.array([predict_time]).reshape((-1, 1))
    ten_year_prediction = linear_model.predict(predict_year)
    

    return ten_year_prediction[0]


# Work out the final predicted result for the income and gender gap of 2030
def total_linear_regression_result(y_coordinate_dict):
    linear_regression_result_dict = {}

    for k in y_coordinate_dict:
        linear_regression_result_dict[k] = {}
        predict_income_gap_2030 = linear_regression(k, y_coordinate_dict, "income", 2030)
        predict_gender_gap_2030 = linear_regression(k, y_coordinate_dict, "gender", 2030)
        linear_regression_result_dict[k]["income"] = predict_income_gap_2030
        linear_regression_result_dict[k]["gender"] = predict_gender_gap_2030

    return linear_regression_result_dict


# Calculate the average income & gender gap of 2030
def calculate_average_gap(result_dict, country_list):
    average_result_dict = {}
    sum_income_gap = 0
    sum_gender_gap = 0

    for k in result_dict:
        sum_income_gap = sum_income_gap + result_dict[k]["income"]
        sum_gender_gap = sum_gender_gap + result_dict[k]["gender"]

    average_income_gap = sum_income_gap / len(country_list)
    average_gender_gap = sum_gender_gap / len(country_list)

    average_result_dict["average_income_gap"] = average_income_gap
    average_result_dict["average_gender_gap"] = average_gender_gap

    return average_result_dict


# Compare the average value with our liner regression result
# print the list of countries which higher or lower than our average prediction, or even equal
def compare_with_the_average(average_dict, result_dict):
    compare_result_dict = {}
    higher_than_income_average = []
    lower_than_income_average = []
    equal_to_income_average = []
    higher_than_gender_average = []
    lower_than_gender_average = []
    equal_to_gender_average = []

    for k in result_dict:
        if result_dict[k]["income"] > average_dict["average_income_gap"]:
            higher_than_income_average.append(k)
        elif result_dict[k]["income"] < average_dict["average_income_gap"]:
            lower_than_income_average.append(k)
        elif result_dict[k]["income"] == average_dict["average_income_gap"]:
            equal_to_income_average.append(k)

        if result_dict[k]["gender"] > average_dict["average_gender_gap"]:
            higher_than_gender_average.append(k)
        elif result_dict[k]["gender"] < average_dict["average_gender_gap"]:
            lower_than_gender_average.append(k)
        elif result_dict[k]["gender"] == average_dict["average_gender_gap"]:
            equal_to_gender_average.append(k)

    compare_result_dict["higher_than_income_average"] = higher_than_income_average
    compare_result_dict["lower_than_income_average"] = lower_than_income_average
    compare_result_dict["equal_to_income_average"] = equal_to_income_average

    compare_result_dict["higher_than_gender_average"] = higher_than_gender_average
    compare_result_dict["lower_than_gender_average"] = lower_than_gender_average
    compare_result_dict["equal_to_gender_average"] = equal_to_gender_average

    return compare_result_dict


def main():
    # Work out the linear regression result for the 'countries' list
    y_dict = convert_to_target_data_dict(countries)
    linear_regression_result_dict = total_linear_regression_result(y_dict)

    # Work out the average income & gender gap
    average_gap_result = calculate_average_gap(linear_regression_result_dict, countries)

    # Compare the average gap with the gap for each country
    compare_with_average = compare_with_the_average(average_gap_result, linear_regression_result_dict)

    # Print the results
    print(linear_regression_result_dict)
    print()
    print(average_gap_result)
    print()
    print(compare_with_average)
    return linear_regression_result_dict,average_gap_result,compare_with_average


if __name__ == "__main__":
    linear_regression_result_dict,average_gap_result,compare_with_average = main()


# over view our linear regression result
print()
print(linear_regression_result_dict)


# =============================================================================
# #part 5: plot the figure with our prediction with comparison
# =============================================================================

# Commented out IPython magic to ensure Python compatibility.
# =============================================================================
# #plot 1 for income gap with prediction in 2030
# =============================================================================
# %matplotlib inline
from matplotlib.pyplot import MultipleLocator
plt.figure(figsize=(12,6),dpi=60)
plt.title('Prediction of Income Gap in 2030')
plt.xlabel('Year')
plt.ylabel('Income gap%')
all_data_i = []

xr_x = list(range(2008,2019))
xr_x.append(2030)
# xr_x = list(map(lambda x:str(x),xr_x))
for c in countries:
  gap_i = gap_income_Dataframe(c)
  x_i = list(gap_i.keys())
  y_i = list(gap_i.values())
  tmp = linear_regression_result_dict[c]
  x_i.append(2019)
  y_i.append(tmp["income"])
  gap_i[2019] = tmp["income"]
  all_data_i.append(gap_i)
  plt.scatter(xr_x,y_i,marker='+',label=c)
  plt.legend(loc=2,bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)

x_major_locator=MultipleLocator(1)  #set the x interval as 1
y_major_locator=MultipleLocator(2)   #set the y interval as 2
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)     #Set the major scale of the x-axis to a multiple of 1
ax.yaxis.set_major_locator(y_major_locator)     #Set the major scale of the y-axis to a multiple of 2
plt.xlim(2007,2031)   #Set the scale range of the x-axis from 2008 to 2018
plt.ylim(25,60)     #Set the scale range of the y-axis from 25 to 60


xr_i = list(range(2008,2019))
xr_i.append(2019)
yr_i = []
for i in xr_i:
  temp = 0
  for j in all_data_i:
    temp += j[i]
  temp /= len(countries)
  yr_i.append(temp)

plt.plot(xr_x,yr_i,"r-",label='average')
plt.legend(loc=2,bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
plt.savefig('Income gap.pdf')  
plt.show()




# =============================================================================
# #plot 2 for gender gap with prediction in 2030
# =============================================================================
plt.figure(figsize=(12,6),dpi=60)
plt.title('Prediction of Gender Employment Gap in 2030')
plt.xlabel('Year')
plt.ylabel('Gender Employment Gap %')
all_data_j = []

xr_x = list(range(2008,2019))
xr_x.append(2030)
for c in countries:
  gap_j = gap_gender_Dataframe(c)
  x_j = list(gap_j.keys())
  y_j = list(gap_j.values())
  tmp = linear_regression_result_dict[c]
  x_j.append(2019)
  y_j.append(tmp["gender"])
  gap_j[2019] = tmp["gender"]
  all_data_j.append(gap_j)
  plt.scatter(xr_x,y_j,marker='+',label=c)
  plt.legend(loc=2,bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)

x_major_locator=MultipleLocator(1)  #set the x interval as 1
y_major_locator=MultipleLocator(2)   #set the y interval as 2
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)     #Set the major scale of the x-axis to a multiple of 1
ax.yaxis.set_major_locator(y_major_locator)     #Set the major scale of the y-axis to a multiple of 0.02
plt.xlim(2007,2031)   #Set the scale range of the x-axis from 2008 to 2018
plt.ylim(2,38)     #Set the scale range of the y-axis from 25 to 60


xr_j = list(range(2008,2019))
xr_j.append(2019)
yr_j = []
for i in xr_j:
  temp = 0
  for j in all_data_j:
    temp += j[i]
  temp /= len(countries)
  yr_j.append(temp)
plt.plot(xr_x,yr_j,"r-",label='average')
plt.legend(loc=2,bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
plt.show()



