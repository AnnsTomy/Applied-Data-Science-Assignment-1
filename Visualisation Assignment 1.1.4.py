# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 00:54:22 2023

@author: Anns Tomy
"""

"""Anns Tomy"""
"""Student I D: 22033815"""

'#importing the required libraries.'

import pandas as pd
import matplotlib.pyplot as plt


"""creating a function for the lineplot"""
def lin_plt(x_axis, y_axis, name, col):  #definition of the line plot
    plt.plot(x_axis, y_axis, label = name, color = col)
    return
    
"""creating a function for bar plot"""
def bar_plt(x_axis, y_axis): #definition of bar plot
    plt.bar(x_axis, y_axis) 
    return

"""creating a function for pie plot"""
def pie_plt(y, label): #definition of a pie chart
    plt.pie(y, labels = label, autopct = '%1.f%%')
    return
    
"""read the excel file and demonstrate it as a dataframe"""
df_life_expectancy =  pd.read_excel('D:\POPULAR INDICATORS LIFE EXPECTANCY.xlsx', index_col=0)
print(df_life_expectancy)  

#dropping the unwanted columns
df_life_expectancy1 = df_life_expectancy.drop(["Unnamed: 11"], axis = 1)
df_life_expectancy1

#slicing the dataframe 
df_life_expectancy2 = df_life_expectancy1.iloc[:,0:9]
df_life_expectancy2

# plot the Life expectancy rate using lineplot
plt.figure()
lin_plt(df_life_expectancy2.columns, df_life_expectancy2.loc["Albania"], "Albania", "red") #df_life_expectancy2.columns gives the years.
lin_plt(df_life_expectancy2.columns, df_life_expectancy2.loc["Algeria"], "Algeria", "green")
lin_plt(df_life_expectancy2.columns, df_life_expectancy2.loc["Afghanistan"], "Afghanistan", "blue")
lin_plt(df_life_expectancy2.columns, df_life_expectancy2.loc["Aruba"], "Aruba", "yellow")
plt.legend()
plt.xlabel("Years") #set x label
plt.ylabel("Life Expectancy rate") #set y label
plt.title("Life Expectancy at birth ") #set title
plt.show()


#plotting the Life expectancy rate of the year 2000 using barplot
plt.figure(figsize = (16,8)) #set the figure size 
bar_plt(df_life_expectancy2.index, df_life_expectancy2["2000"]) #df_life_expectancy2.index gives the countries list.
plt.xlabel("counries") #set the x label
plt.ylabel("Life Expectancy rate") #set the y label
plt.title("Life Expectancy of countries in the year 2000") #set the title
plt.show()

"""read the excel file and demonstrate it as a dataframe"""
df_exports =  pd.read_excel("D:\Exports of goods and services (% of GDP).xlsx", index_col = 0)
df_exports

"""dropping the unwanted columns"""
df_exports1 = df_exports.drop(['Unnamed: 10'], axis = 1)
df_exports1

#plotting the pie chart of the year 2000
pie_plt(df_exports1['2000'], label = df_exports1.index)
plt.title("Exports of Goods and Services of countries in the year 2000 (% of GDP)")
plt.show()


