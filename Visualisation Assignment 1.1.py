# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 00:54:22 2023

@author: Anns Tomy
"""

"""Anns Tomy"""
"""Student I D: 22033815"""
#importing the required libraries for plotting and reading the given excel file.
import pandas as pd

import matplotlib.pyplot as plt


"""creating a function for the lineplot"""
def lin_plt(x_axis, y_axis, name, col):
    plt.plot(x_axis, y_axis, label = name, color = col)
    return
    
"""creating a function for bar plot"""
def bar_plt(x_axis, y_axis):
    plt.bar(x_axis, y_axis)
    return

"""creating a function for pie plot"""
def pie_plt(y, label):
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
lin_plt(df_life_expectancy2.columns, df_life_expectancy2.loc["Albania"], "Albania", "red")
lin_plt(df_life_expectancy2.columns, df_life_expectancy2.loc["Algeria"], "Algeria", "green")
lin_plt(df_life_expectancy2.columns, df_life_expectancy2.loc["Afghanistan"], "Afghanistan", "blue")
lin_plt(df_life_expectancy2.columns, df_life_expectancy2.loc["Aruba"], "Aruba", "yellow")
plt.legend()
plt.xlabel("Years")
plt.ylabel("Life Expectancy at birth")
plt.title("Life Expectancy")
plt.show()


#plotting the Life expectancy rate of the year 2000 using barplot
plt.figure(figsize = (16,8))
bar_plt(df_life_expectancy2.index, df_life_expectancy2["2000"])



plt.xlabel("counries")
plt.ylabel("Life Expectancy at birth")
plt.title("Life Expectancy rate of the year 2000")
plt.show()

"""read the excel file and demonstrate it as a dataframe"""
df_exports =  pd.read_excel("D:\Exports of goods and services (% of GDP).xlsx", index_col = 0)
df_exports

"""dropping the unwanted columns"""
df_exports1 = df_exports.drop(['Unnamed: 10'], axis = 1)
df_exports1

#plotting the pie chart of the year 2000
pie_plt(df_exports1['2000'], label = df_exports1.index)
plt.title("Exports of Goods and Services in the year 2000 (% of Population)")
plt.show()


