#A program that creates a montecarlo simulation
# Reference: https://levelup.gitconnected.com/how-to-make-pareto-chart-in-matplotlib-ff9b6ec7fadf

#By: Dan Comey

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import json
import random

def CreateChart(df, axis_label, chart_title, file_name):
	#creates chart from dataframe
	
	fig, ax = plt.subplots(figsize= (16, 9))
	ax.bar(x= df.index, height= df['frequency'], width = 0.98, edgecolor = "Black")
	
	ax.set_title(chart_title, fontsize= 28)
	ax.set_ylabel(axis_label, fontsize= 18)

	plt.savefig(file_name)

	print()
	print("Figure sucessfully created!")
	print("file_name: " + file_name)
	print()

	show_chart = input("Show chart? (yes/no) ")

	if show_chart == "yes":
		plt.show()

def MonteCarloDice(n,num_dice):
	#rolls num_dice dice n times and records the cumulative sum into a dataframe 

	#creates blank dictionary
	frequency_dict = {}
	cur_sum = 0

	for i in range(n):
		for j in range(num_dice):
			cur_sum += random.randint(1, 6)

		# Update the frequency count in the dictionary
		if cur_sum in frequency_dict:
			frequency_dict[cur_sum] += 1

		else:
			frequency_dict[cur_sum] = 1			

		cur_sum = 0

	return frequency_dict


### need to add error checking

print("Welcome to the Monte Carlo Dice Simulation!")

print()
num_dice = int(input("How many dice would you like to roll? "))
n = int(input("How many iterations? "))
print()

chart_title = "Monte Carlo Simulation of " + str(num_dice) + " Dice (n = " + str(n) + ")"
axis_label = "Frequency of Cumulative sum of " + str(num_dice) + " Dice"

file_name = chart_title + ".png"

test_dict = MonteCarloDice(n,num_dice)

df = pd.DataFrame.from_dict(test_dict, orient= "index",columns= ['frequency'])
df.sort_index(ascending=True, inplace= True)

CreateChart(df, axis_label, chart_title, file_name)



# print("before df head")
# print(df.head())

