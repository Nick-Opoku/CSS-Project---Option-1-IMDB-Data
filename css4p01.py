#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:27:40 2024

@author: nick
"""

import pandas

import numpy as np

import matplotlib.pyplot as plt


movie_data = pandas.read_csv("/home/nick/Documents/Summer-School-NITP/css2024_day1/data_01/movie_dataset.csv")
print(movie_data)


data2 = movie_data.query("Rating == 9")
print(data2["Title"].value_counts().head(10))

print(movie_data.describe())

print(movie_data['Revenue (Millions)'].mean())

first_rank = movie_data.loc[1,'Rank']
print("Rank of first row:", first_rank)

Year_2015_to_2017 = movie_data[movie_data.loc[:,'Year'].between(2015,2017)]

print("Year between 2009 and 2012:\n", Year_2015_to_2017)

print(movie_data[movie_data.loc[:,'Year'].between(2015,2017)].mean())


a = filtered_df = movie_data[movie_data['Year'] == 2016].count()
print(a)

b = filtered_df = movie_data[movie_data['Director'] == 'Christopher Nolan'].count()
print(b)

c = filtered_df = movie_data[movie_data['Rating'] >= 8.0].count()
print(c)

b1 = filtered_df = movie_data[movie_data['Director'] == 'Christopher Nolan'].median()
print(b1)

data3 = movie_data.loc[movie_data['Rating'].idxmax()]
print(data3)


#res = movie_data.Actors.str.split(expand=True).stack().value_counts()
#print("Result:\n",res)

#count = movie_data.groupby('Actors').size()

#mask = movie_data['Actors'] == 'Mark Wahlberg'


splitted_name=movie_data.Actors.str.split(expand=True)

res = splitted_name[1].str.split(expand=True).stack().value_counts()


temp = movie_data.Genre.str.split(",").value_counts()


Correlation = movie_data.corr()
print(Correlation)








#Other-important-sample-codes
#Actors_movie_data['First_name'] = splitted_name[:1]

#movie_data['M']= np.where(splitted_name[2].notna(), splitted_name[1], '')

#movie_data['L']= np.where(splitted_name[2].notna(), splitted_name[2], splitted_name[1])

#df = pandas.DataFrame(movie_data1, movie_dataM, movie_data2)

#print (movie_data)

