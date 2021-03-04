# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:29:22 2021

@author: hulkb
"""


"""
•extract_election_vote_counts(filename, column_names)

•ones_and_tens_digit_histogram(numbers)

•plot_iranian_least_digits_histogram(histogram)

•plot_distribution_by_sample_size()

•mean_squared_error(numbers1, numbers2)

•calculate_mse_with_uniform(histogram)

•compare_iranian_mse_to_samples(mse)

"""



import numpy as np
import matplotlib.pyplot as plt
import csv

# =============================================================================
# #problem 1
# =============================================================================

#Method 1
def extract_election_vote_counts(filename, column_names):
    #I don't know what the hell was encoding = 'unicode_escape', but it works, copy it from online
    with open(filename, 'r', encoding= 'unicode_escape') as f:
        #read the csv file, and generate a list a dictionary
        csv_reader = csv.DictReader(f) 
    
        us_list = [] #create a list that save the correct elements 
    
        for row in csv_reader:
            for i in column_names:
                us_list.append(row[i])
    
        us_list = [x for x in us_list if x != ''] #delete str '', which cause errors for later calculating 
        
        for item in range(len(us_list)):
            us_list[item] = int(us_list[item].replace(',','')) # convert each str to int

    return us_list
    
# =============================================================================
iran_list = extract_election_vote_counts("election-iran-2009.csv", ["Ahmadinejad",
"Rezai", "Karrubi", "Mousavi"])
# =============================================================================

# =============================================================================
#Method 2
#import pandas as pd
#     votedf = pd.read_csv(r'C:\Users\hulkb\Desktop\Academic\PythonP\HWK 5' +'\\' + filename)
#     
#     if type(column_names) == list:
#         vname = column_names.copy()
#         sdf = votedf[vname]
#     else:
#         sdf = votedf[column_names]
#     
#     for name in vname:
#     
#         for j in range(sdf.index.size):
#             k = int(sdf[name][j].replace(',',''))
#             sdf.at[j, name] = k
#             
#     vote_list = []
#     if type(column_names) == list:
#         for j in range(sdf.index.size):
#             for i in column_names:    
#                 vote_list.append(sdf[i][j])
#     else:
#         for j in range(sdf.index.size):
#             vote_list.append(sdf[column_names][j])
#     
#     
#     return vote_list
# =============================================================================


#print(a_list)

# =============================================================================
# #problem 2
# =============================================================================
def ones_and_tens_digit_histogram(histogram):
    ot_list = []

    for i in range(10):
        countone = 0 #one place digit
        countten = 0 #ten place digit
        for j in histogram: #this loop for counting numbers show up in one place 
            if j % 10 == i:
                countone += 1 
        ot_list.append(countone)
        
        for k in histogram: #this loop for counting numbers show up in ten place
            if (k % 100) // 10 == i:
                countten += 1
        ot_list[i] += countten 
        ot_list[i] = ot_list[i] / (2 * len(histogram))#total case = 2 * len(histogram)
   
          
    
    return ot_list

iran_data = ones_and_tens_digit_histogram(iran_list)


# =============================================================================
# #problem 3
# =============================================================================

def plot_iranian_least_digits_histogram(data):
    fig, axes = plt.subplots(figsize = (8, 6)) # formating the figure size
    
    x1 = np.array(list(range(10))) # x is from 0 to 9
    y1 = np.array(data) #y is the probability that we calculate before
    
    # x2, y2 is the uniform line y = 0.1 all the time
    x2 = np.array(list(range(10))) 
    y2 = np.ones(10)/10
    # here is all details of my plot 
    axes.plot(x2, y2, 'blue', label = "Ideal")
    axes.plot(x1, y1, 'green', label = "Iran")
 
    axes.set_xlim([0, 9])
    axes.set_ylim([0.06, 0.16])
    axes.set_xlabel('Digit')
    axes.set_ylabel('Frequency')
    axes.legend(loc = 1, fontsize = 14, framealpha = 1, edgecolor = "black")
    #fig.savefig("iran-digits.png")
    


# =============================================================================
# #problem 4
# =============================================================================

def plot_distribution_by_sample_size():
    
    fig, axes = plt.subplots(5, 1, figsize = (10, 50))
    x2 = np.array(list(range(10)))
    y2 = np.ones(10)/10
    
    sample_size = [10, 50, 100, 1000, 10000] # this is the list of sample_size
    color_list = ['g', 'r', 'orange', 'm', 'y'] # this is the list of color we choose
    for i in sample_size: # the loop for generating 5 plots 
        arr = np.random.randint(0, 100, i)
        listx = arr.tolist()
        y = np.array(ones_and_tens_digit_histogram(listx))
        x = np.array(list(range(10)))
        # too many details I don't need to explain, just google it, and use the syntax
        colorplt = color_list[sample_size.index(i)]
        axes[sample_size.index(i)].plot(x, y, color = colorplt, label = "sample size {}".format(i))
        axes[sample_size.index(i)].plot(x2, y2, 'blue', label = 'Ideal', alpha=0.5)
        axes[sample_size.index(i)].set_xlabel('Digit')
        axes[sample_size.index(i)].set_ylabel('Frequency')
        axes[sample_size.index(i)].set_title('Distribution of last two digits')
        axes[sample_size.index(i)].set_xlim([0, 9])
        axes[sample_size.index(i)].set_ylim([0.00, 0.25])
        axes[sample_size.index(i)].legend(loc = 1, fontsize = 14, framealpha = 1, edgecolor = "black")
        
    #fig.savefig("random-digits.png")
    return None


# =============================================================================
# #problem 5
# =============================================================================
def mean_squared_error(numbers1, numbers2):
    sum = 0
    for i in range(len(numbers1)):
        sum += (numbers1[i]-numbers2[i]) ** 2 #the math formula
    
    return sum

# =============================================================================
# #problem 6
# =============================================================================

def calculate_mse_with_uniform(histogram):
    return mean_squared_error(histogram, 10*[0.1])
    
def compare_iranian_mse_to_samples(mse):
    
      
    larger = 0 # initialize the number of sample mse larger than iranian mse 
    smaller = 0 # initialize the number of sample mse smaller than iranian mse
    for i in range(1, 10001): # start from 1 to 10001, 10001 exclusive
        arr = np.random.randint(0, 100, 120) # the number should be 120, because iranian has 120 size of number
        listx = arr.tolist() # convert arr to list
        listy = ones_and_tens_digit_histogram(listx)
        smse = calculate_mse_with_uniform(listy)
        if smse >= mse: # conditions
            larger += 1
        else:
            smaller += 1
    print("    compare_iranian_mse_to_samples("+ str(round(mse, 14)) + ')') # correct formatting
    print("Quantity of MSEs larger than or equal to the 2009 Iranian election MSE:", larger)
    print("Quantity of MSEs smaller than the 2009 Iranian election MSE:", smaller)
    print("2009 Iranian election null hypothesis rejection level p:", larger/10000)
    
iran_mse = calculate_mse_with_uniform(iran_data)

compare_iranian_mse_to_samples(iran_mse)


def compare_us_mse_to_samples(mse,sample_size):
    #I add sample_size, because I need to get correct data size of number from us-election file
    #same step as compare_iranian_mse_to_sample(mse)
    larger = 0
    smaller = 0
    for i in range(1, 10001):
        arr = np.random.randint(0, 100, sample_size) #random sample size should match the our file number size
        listx = arr.tolist()
        listy = ones_and_tens_digit_histogram(listx)
        smse = calculate_mse_with_uniform(listy)
        if smse >= mse:
            larger += 1
        else:
            smaller += 1
    print("    compare_us_mse_to_samples("+ str(round(mse, 14)) + ')')
    print("Quantity of MSEs larger than or equal to the 2008 US election MSE:", larger)
    print("Quantity of MSEs smaller than the 2008 US election MSE:", smaller)
    print("2008 US election null hypothesis rejection level p:", larger/10000)

# =============================================================================
# #problem 7 on the answers.txt
# =============================================================================


# =============================================================================
# #problem 8 
# =============================================================================

def main():

    us_2008_candidates = ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"]


    us_list = extract_election_vote_counts('election-us-2008.csv', us_2008_candidates)
    #print(us_list)
    us_data = ones_and_tens_digit_histogram(us_list) 
    us_mse = calculate_mse_with_uniform(us_data)
    print()
    compare_us_mse_to_samples(us_mse, len(us_list)) #sample_size is the len(us_list)
    
    iran_list = extract_election_vote_counts("election-iran-2009.csv", ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])   
    data = ones_and_tens_digit_histogram(iran_list)
    iran_mse = calculate_mse_with_uniform(data)
   
    assert round(iran_mse, 14) == 0.00739583333333 # answer from HWK 5.pdf Problem 6


if __name__ == '__main__':
    main()



# =============================================================================
# #problem 9
# =============================================================================

import math

fig, axes = plt.subplots(figsize = (8, 6))
x = np.array(list(range(1, 10)))
ylist = []
for i in range(len(x)):
    benfor_function = math.log10(1 + (1 / x[i]))
    ylist.append(benfor_function)

y = np.array(ylist)


axes.plot(x, y, label = "Benford")
axes.set_xlim([1, 9])
axes.set_ylim([0.00, 0.35])


#fig.savefig("scale-invariance.png")


# =============================================================================
# print(y_random_list)
# print(y_exp_list)
# 
# =============================================================================

# =============================================================================
# #problem 10
# =============================================================================

# this function for getting the exp list basing on sample size
def get_exp_list(sample_size): 
    y_random_list = np.random.uniform(0.0, 30.0, sample_size)
    y_exp_list = []

    for i in y_random_list:
        y_exp_list.append(math.exp(i))
    
    return y_exp_list

y_exp_list = get_exp_list(1000)

#this function is for get a result list of the most significant digit
def get_the_most_significant_digits(sample_list): 
    most_list = []
    for i in range(len(sample_list)):
        most_list.append(int(str(sample_list[i])[0]))
    return most_list

most_list = get_the_most_significant_digits(y_exp_list)


import collections

#this function is for getting a list of one to nine count number
def count_most_significant_digits(sample_list):
    digits_dict = collections.Counter(sample_list)
    number_list = []
    for i in range(1, 10):
        number_list.append(digits_dict[i])
    
    return number_list
   

count_dict = count_most_significant_digits(most_list)
#print(count_dict)

#this function is for geting a list of frequency of one to nine numner
def frequency_significant_digits(sample_list):
    total_case = 0
    for i in range(len(sample_list)):
        total_case +=sample_list[i]
        
        
    list_frequency_one_to_nine = []
    
    for i in range(len(sample_list)):
        list_frequency_one_to_nine.append(sample_list[i] / total_case)
    
    return list_frequency_one_to_nine

# this function is for simplifying the process of getting frequence list
def process_frequency_list(sample_list): 
    a = get_the_most_significant_digits(sample_list)
    b = count_most_significant_digits(a)
    
    return frequency_significant_digits(b)

frequence_list = frequency_significant_digits(count_dict)
#print(frequence_list)

axes.plot(x, frequence_list, color = 'r', label = "1000 samples")


# =============================================================================
# #problem 11
# =============================================================================

pi_exp_list = [] #list for storing pi * exp value
for i in range(len(y_exp_list)):
    a = y_exp_list[i] * math.pi
    pi_exp_list.append(a)

pi_frequency_list = process_frequency_list(pi_exp_list)
#plot the fig
axes.plot(x, pi_frequency_list, color = 'g', label = "1000 samples, scaled by $\pi$")
axes.legend(loc = 1, fontsize = 14, framealpha = 1, edgecolor = "black")
#fig.savefig("scale-invariance.png")


# =============================================================================
# #problem 12
# =============================================================================

#this function is for get a list of csv file, the reason why I use a new one is
#because they have different format
def extract_population_vote_counts(filename, column_names):
    
    with open(filename, 'r', encoding= 'unicode_escape') as f:
        csv_reader = csv.DictReader(f) 
        column = [row[column_names] for row in csv_reader]
        
        city_2000_list = [x for x in column if x != '0' and x.isdigit()== True]
           
    return city_2000_list
            


city_2000_list = extract_population_vote_counts('SUB-EST2009_ALL.csv', 'POPCENSUS_2000')
city_frequency_list = process_frequency_list(city_2000_list)

#print("city", city_frequency_list)

#this function is to getting a list of benford distribution
def benford_list():
    
    x = np.array(list(range(1, 10)))
    ylist = []
    for i in range(len(x)):
        benfor_function = math.log10(1 + (1 / x[i]))#benford 
        ylist.append(benfor_function)
    
    return ylist

benfordlist = benford_list()
#print(benfordlist)

    
fig, axes = plt.subplots(figsize = (8, 6))
x = np.array(list(range(1, 10)))
y = np.array(benfordlist)
ys = np.array(city_frequency_list)
axes.plot(x, y, color = 'green', label = "Benford")
axes.plot(x, city_frequency_list, marker = 'o', label = 'US (all)', lw = 4, alpha = 0.5)

#axes.hist(sample_list, bins = n_bins, label='US (all)') 
axes.set_xlim([0, 9.5])
axes.set_ylim([0.00, 0.35])
axes.legend()
       

# =============================================================================
# #problem 13
# =============================================================================

#open txt file
with open('literature-population.txt', 'r', encoding='utf8') as f:
    text_list = []
    for line in f:
        temp_list = line.split('\t') # its tab space, which we can split the str
        text_list.append(temp_list[1])
    
   
    for i in range(len(text_list)):
        text_list[i] = text_list[i].rstrip("\n") #get rid of new line
     
text_final_list = []

for i in range(len(text_list)):# convert str to int
    text_final_list.append(int(text_list[i].replace(',','')))
#the process of get y 

text_frequency_list = process_frequency_list(text_final_list)

yt = np.array(text_frequency_list)


axes.plot(x, yt, color = 'red',  ls='-.',label = "Literature Places." )
axes.set_xlim([1, 9])
axes.set_ylim([0.00, 0.35])
axes.legend()

#fig.savefig("population-data.png")

# =============================================================================
# #problem 14
# =============================================================================

#print(city_2000_list)

#this is the process we can get first 10 city frequencey result list
city_most_list = get_the_most_significant_digits(city_2000_list)
first_city_2000_list = []
for i in range(10):
    first_city_2000_list.append(city_most_list[i])

#print(first_city_2000_list) #
city_count_2000_list = count_most_significant_digits(first_city_2000_list)
city_frequency_list = frequency_significant_digits(city_count_2000_list)
#print(city_frequency_list)

#getting sample variation and compare to benford distribution
def sample_variation(benfordlist, sample_list):
    fig, axes = plt.subplots(figsize = (8, 6))
    x = np.array(list(range(1, 10)))
    y = np.array(benfordlist)
    axes.plot(x, y, color = 'blue', ls='--', label = "Benford", alpha = 0.5)
    
    
    y2 = np.array(sample_list)
    
    
    axes.plot(x, y2, color = 'g', label = "first 10 U.S. cities")
    #same procedure that specify different line
    sample_size = [10, 50, 100, 10000]
    color_list = ['black', 'r', 'orange', 'm']
    for i in sample_size: #plot each sample line on same graph
        exp_list = get_exp_list(i) 
        sample_frequency_list = process_frequency_list(exp_list)
        yl = np.array(sample_frequency_list)
        colorplt = color_list[sample_size.index(i)]
        axes.plot(x, yl, color = colorplt, label = "{} samples". format(i))
    
    
    
    axes.legend()
    axes.set_xlim([1, 9])
    axes.set_ylim([0.00, 0.35])
    axes.set_title('Population')
    axes.set_xlabel('Digit')
    axes.set_ylabel('Frequency')
    #fig.savefig("Benford-samples.png")
    
sample_variation(benfordlist, city_frequency_list)

# =============================================================================
# #problem 15
# =============================================================================

#get mse 
a = mean_squared_error(text_frequency_list, benfordlist)




import random # we need it for random select elements from a list

text_most_list = get_the_most_significant_digits(text_final_list)

#this function is for comparing mse between two frequence list
def city_vs_literatue_mse(city_most_list, sample_size, literature_mse, benford_list):
    
    smaller = 0 #initialize the number of mse less than specific mse
    larger = 0 #initialize the number of mse large than specific mse
    for i in range(10000): # 10000 sets
        sample_size_list =[]
        for j in range(len(sample_size)): # get random number select
            random_num = random.choice(city_most_list)
            sample_size_list.append(random_num)
        
        #the process we get frequence list
        sample_count_list = count_most_significant_digits(sample_size_list)
        sample_frequency_list = frequency_significant_digits(sample_count_list)
        value = mean_squared_error(sample_frequency_list, benford_list)
        if value >= literature_mse: #condition
            larger += 1 
        else:
            smaller += 1
    print()       
    print("Comparison of US MSEs to literature MSE:", literature_mse)
    print("larger/equal:", larger)
    print("smaller:", smaller)

#get result
city_vs_literatue_mse(city_most_list, text_most_list, a, benfordlist)




# =============================================================================
# #problem 16 on answers.txt
# =============================================================================


































# =============================================================================
# the following code is totally wrong, but I don't want to delete it
# it is for count every digits for one number
#import collections
# 
# def count_most_significant_digits(sample_list):
#     sum_count = collections.Counter(str(sample_list[0]))
#     for i in range(1, len(sample_list)):
#         sum_count += collections.Counter(str(sample_list[i]))
#     
#     del sum_count['.']
#     del sum_count['0']
#     
#     return sum_count
# 
# count_list = count_most_significant_digits(y_exp_list)
#     
# def frequency_significant_digits(sample_list):    
#     list_one_to_nine = []
#     for i in range(1, 10):
#         list_one_to_nine.append(sample_list[str(i)])
#      
#     total_case = 0
#     for i in range(len(list_one_to_nine)):
#         total_case += list_one_to_nine[i]
#     
#     list_frequency_one_to_nine = []
#     
#     for i in range(len(list_one_to_nine)):
#         list_frequency_one_to_nine.append(list_one_to_nine[i] / total_case)
#     
#     return list_frequency_one_to_nine
# 
# list_frequency_one_to_nine = frequency_significant_digits(count_list)
# 
# axes.plot(x, list_frequency_one_to_nine, color = 'r', label = "1000 samples")
# =============================================================================









