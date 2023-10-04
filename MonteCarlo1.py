#A program that prompts the user for the number of dice and number of iterations and creates a histogram of the results of a monte carlo simulation
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

	# Add a vertical line for the mean
	mean_value = df.index.to_series().mean()
	plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label='Mean')

	#Save Figure
	plt.savefig(file_name)

	print()
	print("Figure sucessfully created!")
	print("file_name: " + file_name)
	print()

	#prompts user if they would like to display the chart
	show_chart = input("Show chart? (yes/no) ")

	if show_chart == "yes":
		plt.show()

def MonteCarloDice(n,num_dice):
	#rolls num_dice dice n times and records the cumulative sum into a dictionary 

	#creates blank dictionary
	frequency_dict = {}
	cur_sum = 0

	for i in range(n):
		for j in range(num_dice):
			#rolls num_dice dice n times and calculates the cumulative sum
			cur_sum += random.randint(1, 6)

		# Update the frequency count in the dictionary
		if cur_sum in frequency_dict:
			frequency_dict[cur_sum] += 1

		else:
			frequency_dict[cur_sum] = 1			

		cur_sum = 0

	return frequency_dict


### currently does not have error checking for the inputs

print("Welcome to the Monte Carlo Dice Simulation!")

print()
num_dice = int(input("How many dice would you like to roll? "))
n = int(input("How many iterations? "))
print()

chart_title = "Monte Carlo Simulation of " + str(num_dice) + " Dice (n = " + str(n) + ")"
axis_label = "Frequency of Cumulative sum of " + str(num_dice) + " Dice"
file_name = chart_title + ".png"


# creates data frame of results of monte carlo dice simulation based off of the user inputed number of dice and number of iterations
test_dict = MonteCarloDice(n,num_dice)
df = pd.DataFrame.from_dict(test_dict, orient= "index",columns= ['frequency'])

#sorts dataframe index from smallest to largest for a more logical chart
df.sort_index(ascending=True, inplace= True)

#creates histogram of the above dataframe
CreateChart(df, axis_label, chart_title, file_name)