#A program that creates a montecarlo simulation
# Reference: https://levelup.gitconnected.com/how-to-make-pareto-chart-in-matplotlib-ff9b6ec7fadf

#By: Dan Comey

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import json
import random

def CreateChart(df, column_name, axis_label, chart_title, file_name):
	#creates chart from dataframe

def MonteCarloDice(n,num_dice):
	#rolls num_dice dice n times and records the cumulative sum into a dataframe 

	#creates blank dataframe
	df = pd.DataFrame('Sum','Frequency')
	
	for i in range(n):
		for j in range(num_dice):
			cur_sum += random.randint(1, 6)

		cur_sum = 0


	return df


