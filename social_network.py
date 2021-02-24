# Name: ...
# Homework 4

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

###
### Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
# TODO: Add more here...
practice_graph.add_edge("B", "D")
practice_graph.add_edge("D", "E")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "F")

assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

# Test shape of practice graph
assert set(practice_graph.neighbors("A")) == set(["B", "C"])
assert set(practice_graph.neighbors("B")) == set(["A", "D", "C"])
assert set(practice_graph.neighbors("C")) == set(["A", "B", "D", "F"])
assert set(practice_graph.neighbors("D")) == set(["B", "C", "E", "F"])
assert set(practice_graph.neighbors("E")) == set(["D"])
assert set(practice_graph.neighbors("F")) == set(["C", "D"])

def draw_practice_graph():
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(practice_graph)
    plt.show()

# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
#draw_practice_graph()


###
### Problem 1b
###

# (Your code for Problem 1b goes here.)
rj = nx.Graph()
rj.add_edge("Nurse", "Juliet")
rj.add_edge("Juliet", "Tybalt")
rj.add_edge("Juliet", "Capulet")
rj.add_edge("Capulet", "Tybalt")
rj.add_edge("Juliet", "Friar Laurence")
rj.add_edge("Juliet", "Romeo")
rj.add_edge("Romeo", "Friar Laurence")
rj.add_edge("Romeo", "Benvolio")
rj.add_edge("Romeo", "Montague")
rj.add_edge("Romeo", "Mercutio")
rj.add_edge("Benvolio", "Montague")
rj.add_edge("Montague", "Escalus")
rj.add_edge("Capulet", "Escalus")
rj.add_edge("Capulet", "Paris")
rj.add_edge("Escalus", "Mercutio")
rj.add_edge("Escalus", "Paris")
rj.add_edge("Paris", "Mercutio")




assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

# Test shape of Romeo-and-Juliet graph
assert set(rj.neighbors("Nurse")) == set(["Juliet"])
assert set(rj.neighbors("Friar Laurence")) == set(["Juliet", "Romeo"])
assert set(rj.neighbors("Tybalt")) == set(["Juliet", "Capulet"])
assert set(rj.neighbors("Benvolio")) == set(["Romeo", "Montague"])
assert set(rj.neighbors("Paris")) == set(["Escalus", "Capulet", "Mercutio"])
assert set(rj.neighbors("Mercutio")) == set(["Paris", "Escalus", "Romeo"])
assert set(rj.neighbors("Montague")) == set(["Escalus", "Romeo", "Benvolio"])
assert set(rj.neighbors("Capulet")) == \
    set(["Juliet", "Tybalt", "Paris", "Escalus"])
assert set(rj.neighbors("Escalus")) == \
    set(["Paris", "Mercutio", "Montague", "Capulet"])
assert set(rj.neighbors("Juliet")) == \
    set(["Nurse", "Tybalt", "Capulet", "Friar Laurence", "Romeo"])
assert set(rj.neighbors("Romeo")) == \
    set(["Juliet", "Friar Laurence", "Benvolio", "Montague", "Mercutio"])

def draw_rj():
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(rj)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
#draw_rj()


###
### Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


assert friends(rj, "Mercutio") == set(['Romeo', 'Escalus', 'Paris'])


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given 
    graph. The result does not include the given user nor any of that user's
    friends.
    """
    ff = set() # set for friends of friends
    setf = graph.neighbors(user) # find user's friends
    for friend in setf: 
        setff = graph.neighbors(friend)
        for f_friend in setff: # find user's each friend's friends
            if(f_friend != user) and (f_friend not in graph.neighbors(user)):
                ff.add(f_friend) # add element into our set
    return ff
    



assert friends_of_friends(rj, "Mercutio") == \
    set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common.
    """
    commonf = set() # set for common friends
    for friend1 in graph.neighbors(user1): # user1's each friend
        for friend2 in graph.neighbors(user2): # user2's each friend
            if friend1 == friend2: # condition: if their friend are common
                commonf.add(friend1) # add element into our common friends set
    return commonf
    
    
    


assert common_friends(practice_graph,"A", "B") == set(['C'])
assert common_friends(practice_graph,"A", "D") == set(['B', 'C'])
assert common_friends(practice_graph,"A", "E") == set([])
assert common_friends(practice_graph,"A", "F") == set(['C'])
assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping from each user U to the number 
    of friends U has in common with the given user. The map keys are the 
    users who have at least one friend in common with the given user, 
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "A" 
    (Note: This is NOT the practice_graph used in the assignment writeup.)
    Here is what is relevant about my_graph:
        - "A" and "B" have two friends in common
        - "A" and "C" have one friend in common
        - "A" and "D" have one friend in common
        - "A" and "E" have no friends in common
        - "A" is friends with "D" (but not with "B" or "C")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "A")  =>   { 'B':2, 'C':1 }
    """
    numcf = {} #a dictionary for number of common friends 
    for friend in friends_of_friends(graph, user): #find user's friends of friends
        numcf[friend] = len(common_friends(graph, user, friend)) # update our dictionary
        # key is friend, value is the count each fof common friend and 
        
    return numcf    
    
    #print ("Remove this print statement once " + \
        #"number_of_common_friends is implemented")


assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}
assert number_of_common_friends_map(rj, "Mercutio") == \
    { 'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1, 
      'Juliet': 1, 'Montague': 2 }


def number_map_to_sorted_list(map_with_number_vals):
    """Given map_with_number_vals, a dictionary whose values are numbers, 
    return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.
    """
    sort_alpha = sorted(map_with_number_vals.items(), key = lambda x: x[0], reverse = False)
    # sort the dictionary alphabetically based on the key
    sort_max = sorted(sort_alpha, key= lambda x: x[1], reverse = True)
    # sort the new dictionary based on the value
    getkey = itemgetter(0)
    
    return list(map(getkey, sort_max)) #pack our dictionary and get the list of each key 
    


    
# =============================================================================
#     print ("Remove this print statement once " + \
#         "number_map_to_sorted_list is implemented")
# =============================================================================print(number_map_to_sorted_list({"a":5, "b":2, "c":7, "d":5, "e":5}))

assert number_map_to_sorted_list({"a":5, "b":2, "c":7, "d":5, "e":5}) == \
    ['c', 'a', 'd', 'e', 'b']


def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    #use the function we create to get recommond result
    ncf = number_of_common_friends_map(graph, user) 
    return number_map_to_sorted_list(ncf)
# =============================================================================
#     print ("Remove this print statement once " + \
#         "recommend_by_number_of_common_friends is implemented")
# 
# =============================================================================

assert recommend_by_number_of_common_friends(practice_graph,"A") == ['D', 'F']

assert recommend_by_number_of_common_friends(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person P to their 
    influence score, with respect to the given user. The map only 
    contains people who have at least one friend in common with the given 
    user and are neither the user nor one of the users's friends. 
    See the assignment for the definition of influence scores.
    """
    foflist= list(friends_of_friends(graph, user)) #the list is user's friends of friends
    influence_friend = {} # a dictionary for recommond friend, key is recommond friend, value should be scores
    for fof in foflist:
        cfof = list(common_friends(graph, user, fof)) #get friend of friends common friends
        lenlist = list() #a list for count common friends
        for i in cfof:
            lenlist.append(len(friends(graph, i))) # get each common friends count
            
        influence_score = 0 # initialize score is 0
        for j in lenlist: # this loop for get influcence score
            influence_score += 1/j
            influence_friend[fof] = influence_score    
    return influence_friend
    
    #print ("Remove this print statement once influence_map is implemented")



assert influence_map(rj, "Mercutio") == \
    { 'Benvolio': 0.2, 'Capulet': 0.5833333333333333, 
      'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45 }


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    #same step as recommon by number of common friends, first alphabetically then numerically sorted
    sort_alpha = sorted(influence_map(graph, user).items(), key = lambda x: x[0])
    sort_max = sorted(sort_alpha, key = lambda x: x[1], reverse = True)
    
    getkey = itemgetter(0)
    
    return list(map(getkey, sort_max))
    
# =============================================================================
#     print ("Remove this print statement once " + \
#         "recommend_by_influence is implemented")
# 
# =============================================================================

assert recommend_by_influence(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 4
###

# (Your Problem 4 code goes here.)
name_list = ["Nurse", "Juliet", "Tybalt", "Capulet", "Friar Laurence", "Romeo", "Benvolio", "Montague",
             "Escalus", "Mercutio", "Paris"
             ]
# create lists to save our person's name
same_recommend_list = [] 
diff_recommend_list = []
for user in name_list: 
    if recommend_by_influence(rj, user) == recommend_by_number_of_common_friends(rj, user): #condition
        same_recommend_list.append(user) #append our same list
    else:
        diff_recommend_list.append(user) #append our diff list

print("Problem 4:")
print("")
print("Unchanged Recommendations:", same_recommend_list) 
print("Changed Recommendations:", diff_recommend_list)       






###
### Problem 5
###

# (Your Problem 5 code goes here.)
import numpy as np
import pandas as pd

#I don't know about how to read specific column correctly in txt file by using networkx package.
#Therefore, I am done with that method. To solve this problem, back to pandas package, which easy to solve the
#format problem, what I mean is, edit the file, then output the new file, then we can use networkx package read again


df = pd.read_table('facebook-links.txt', header = None, sep='\t') # read our files, 
df.rename(columns = { 0 : 'user', 1 : 'friend', 2 : 'timestamp'}, inplace=True) 
# rename our column's name, which is helpful to later formatting 

df.drop('timestamp', axis = 1, inplace = True) # drop the last column in order to read correctly

np.savetxt(r'C:\Users\hulkb\Desktop\Academic\PythonP\HWK 4\facebookoutput.txt', df.values, fmt = '%d' )
#output our new txt file named facebookoutput.txt
facebook = nx.read_edgelist("facebookoutput.txt", nodetype = int) # got it from online resource

#check nodes or edges if they are wrong 
#print(facebook.number_of_nodes())
#print(facebook.number_of_edges())




assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090


###
### Problem 6
###

# (Your Problem 6 code goes here.)
print("")
print("Problem 6: ")
print("")
multiple_thousand_list = [] # create a list for all nodes that are multiple of 1000 

for i in list(facebook.nodes):
    if i % 1000 == 0: # simple condition to get multiple of 1000
        multiple_thousand_list.append(i)

for j in multiple_thousand_list: # use the recommend_by_number_of_common_friends method
    list_recommend = recommend_by_number_of_common_friends(facebook, j)
    print(j,'(by number_of_common_friends):', list_recommend[:10]) # get first 10 elements of list



###
### Problem 7
###

# (Your Problem 7 code goes here.)
print("")
print("Problem 7: ")
print("")

for k in multiple_thousand_list:
    list_inf_recommend = recommend_by_influence(facebook, k) #use the recommend_by_influence method
    print(k, '(by influence):', list_inf_recommend[:10]) # get first 10 elements of list




###
### Problem 8
###

# (Your Problem 8 code goes here.)
print("")
print("Problem 8: ")
print("")

fb_same_recom = 0
fb_diff_recom = 0

for i in multiple_thousand_list:
    if recommend_by_influence(facebook, i) == recommend_by_number_of_common_friends(facebook, i): #condition
        fb_same_recom += 1 #count same
    else:
        fb_diff_recom += 1 #count diff
        
print('Same:', fb_same_recom)
print('Different:', fb_diff_recom)

###
### Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").

# =============================================================================
# Problem 4:
# 
# Unchanged Recommendations: ['Nurse', 'Friar Laurence', 'Benvolio', 'Escalus', 'Mercutio']
# Changed Recommendations: ['Juliet', 'Tybalt', 'Capulet', 'Romeo', 'Montague', 'Paris']
# 
# Problem 6: 
# 
# 1000 (by number_of_common_friends): [23, 453, 456, 467, 1140, 2068, 451, 469, 472, 746]
# 2000 (by number_of_common_friends): [1686, 1693, 639, 1160, 1408, 1436, 1685, 1691, 1692, 1694]
# 3000 (by number_of_common_friends): [2868, 1156, 3004, 2260, 3002, 244, 639, 867, 2999, 3018]
# 4000 (by number_of_common_friends): [284, 3423, 3978, 4012, 3159, 3975, 3977, 3992, 4003, 4004]
# 5000 (by number_of_common_friends): [1685, 2152, 2218, 1686, 1687, 1691, 1693, 2660, 1689, 2141]
# 6000 (by number_of_common_friends): [22596, 22599, 6015, 40834, 903, 37969, 5792, 40833, 6010, 5232]
# 7000 (by number_of_common_friends): [24649, 20401, 34865, 31156, 20934, 38854, 20010, 6956, 9660, 10221]
# 8000 (by number_of_common_friends): [1209, 7999, 17802, 1299, 3169, 4481, 5280, 5615, 6662, 13283]
# 9000 (by number_of_common_friends): [19228, 10397, 19231, 1632, 7157, 18388, 19286, 1466, 2217, 18397]
# 10000 (by number_of_common_friends): [528, 534, 6027, 6237, 32097, 280, 292, 388, 1304, 1337]
# 11000 (by number_of_common_friends): [13477, 25839, 6951, 10621, 22987, 1395, 10885, 21955, 27329, 1181]
# 12000 (by number_of_common_friends): [3875, 14877, 14884, 3878, 8423, 3901, 14872, 7507, 8272, 9219]
# 13000 (by number_of_common_friends): [25755, 27126, 24543, 7765, 25767, 7108, 14684, 15869, 3579, 7111]
# 14000 (by number_of_common_friends): [13609, 1236, 305, 464, 774, 2019, 2097, 2382, 2848, 3733]
# 15000 (by number_of_common_friends): [23656, 11731, 14484, 26276, 31526, 32017, 11730, 20137, 23673, 26429]
# 16000 (by number_of_common_friends): [1089, 55916, 127, 7063, 31291, 857, 1112, 1401, 6876, 7058]
# 17000 (by number_of_common_friends): [16998, 516, 2723, 4873, 5246, 11292, 16999, 17733, 18553, 19151]
# 18000 (by number_of_common_friends): [18003, 22964, 85, 133, 416, 471, 480, 526, 532, 689]
# 19000 (by number_of_common_friends): [1027, 1759, 2979, 3633, 4353, 5377, 5380, 5931, 7408, 7905]
# 20000 (by number_of_common_friends): [8096, 11756, 27380, 14360, 26799, 4758, 19310, 27091, 28662, 7224]
# 21000 (by number_of_common_friends): [1461, 873, 1456, 1479, 1494, 1518, 1522, 1529, 1622, 6841]
# 22000 (by number_of_common_friends): [18839, 7293, 13766, 18808, 5303, 7365, 9630, 10673, 31329, 46446]
# 23000 (by number_of_common_friends): [28815, 12030, 15148, 11017, 12015, 4459, 26886, 6365, 12046, 15046]
# 24000 (by number_of_common_friends): [150, 360, 471, 492, 720, 870, 1120, 1209, 1381, 1440]
# 25000 (by number_of_common_friends): [11038, 12024, 15677, 16031, 30466, 12019, 12035, 16030, 16032, 12044]
# 26000 (by number_of_common_friends): [32017, 32025, 11731, 18121, 26429, 26576, 17906, 18110, 20029, 34621]
# 27000 (by number_of_common_friends): [6221, 10076, 6224, 6205, 6208, 6194, 6225, 22710, 23167, 26910]
# 28000 (by number_of_common_friends): [23, 1445, 4610, 7996, 10397, 11213, 56, 85, 471, 522]
# 29000 (by number_of_common_friends): [28606]
# 30000 (by number_of_common_friends): [862, 869, 919, 941, 3154, 8180, 8269, 8614, 14473, 14495]
# 31000 (by number_of_common_friends): [8148, 24192, 8757, 9143, 11237, 3983, 5204, 7520, 11608, 21716]
# 32000 (by number_of_common_friends): [133, 22299, 32668, 15582, 19576, 20809, 27719, 5146, 11615, 19519]
# 33000 (by number_of_common_friends): [3598, 8440, 11544, 12248, 32314, 32675, 33001, 280, 313, 432]
# 34000 (by number_of_common_friends): [4940, 10887, 10894, 14099, 15429, 25805, 785, 816, 1143, 1547]
# 35000 (by number_of_common_friends): [2322, 2332, 2341, 9904, 3943, 5144, 11844, 1143, 1900, 1902]
# 36000 (by number_of_common_friends): [32930, 32939, 28405, 35939, 19602, 35573, 24292, 35689, 35748, 35750]
# 37000 (by number_of_common_friends): [15, 542, 785, 817, 3588, 4374, 5033, 7540, 7576, 7901]
# 38000 (by number_of_common_friends): [7586, 994, 5804, 14233, 14678, 17505, 25203, 25212, 26088, 46539]
# 39000 (by number_of_common_friends): [14, 429, 10884, 11784, 12991, 122, 3703, 12970, 12971, 3635]
# 40000 (by number_of_common_friends): [18359, 21771, 21795, 32905, 42949, 48472, 207, 397, 1432, 3497]
# 41000 (by number_of_common_friends): [27803, 40644, 48063, 779, 1919, 7917, 14096, 17921, 23094, 29523]
# 42000 (by number_of_common_friends): [2942, 3360, 5711, 5720, 6442, 6670, 8569, 10086, 10102, 10287]
# 43000 (by number_of_common_friends): [171, 196, 545, 546, 560, 1455, 1957, 1963, 2095, 4626]
# 44000 (by number_of_common_friends): [33208, 6200, 13765, 15447, 17367, 21064, 30204, 32636, 34316, 34348]
# 45000 (by number_of_common_friends): [2322, 2338, 3595, 3880, 3897, 3904, 3910, 3922, 3933, 3938]
# 46000 (by number_of_common_friends): [33700, 31799, 13273, 17344, 27579, 36546, 44120, 4401, 17286, 17380]
# 47000 (by number_of_common_friends): [7183, 4733, 4736, 7164, 20655, 263, 423, 469, 1029, 1143]
# 48000 (by number_of_common_friends): [25172, 26255, 33499, 47998, 25190, 26256, 44153, 47991, 22078, 26257]
# 49000 (by number_of_common_friends): [2206, 2572, 37817, 48995, 48996, 48997, 48998, 48999, 49001]
# 50000 (by number_of_common_friends): [50001, 6992, 7681, 8089, 9369, 9995, 14534, 15045, 16234, 17206]
# 51000 (by number_of_common_friends): [29845, 40214, 40215, 40217]
# 52000 (by number_of_common_friends): [6349, 17121]
# 53000 (by number_of_common_friends): [1524, 3814, 5482, 8415, 8521, 8861, 9126, 10789, 10790, 11727]
# 54000 (by number_of_common_friends): [994, 1495, 1535, 5309, 5424, 6072, 7341, 16301, 17515, 17586]
# 55000 (by number_of_common_friends): [11504, 19302, 21996, 22626, 23503, 34236, 39190, 44928, 47087, 48340]
# 56000 (by number_of_common_friends): [33925, 6498, 10452, 13325, 16495, 18926, 30332, 30973, 37461, 51988]
# 57000 (by number_of_common_friends): [2714, 23, 554, 1078, 1141, 1474, 1476, 1594, 1615, 1739]
# 58000 (by number_of_common_friends): [7748, 7750, 7751, 7754, 7756, 7759, 10500, 10505, 12937, 21332]
# 59000 (by number_of_common_friends): [3847, 22245, 28648, 30983, 32900, 32905, 35522, 35763, 36099, 38599]
# 60000 (by number_of_common_friends): [1739, 8252, 10626, 11103, 14294, 15446, 24421, 31692, 36702, 44849]
# 61000 (by number_of_common_friends): [23, 82, 207, 266, 423, 451, 469, 554, 824, 869]
# 62000 (by number_of_common_friends): [8136, 10483, 10746, 14927, 18006, 18544, 19863, 21264, 21529, 21939]
# 63000 (by number_of_common_friends): [30173, 230, 362, 369, 371, 423, 451, 469, 824, 829]
# 
# Problem 7: 
# 
# 1000 (by influence): [23, 453, 456, 467, 1140, 1009, 16423, 2068, 1011, 469]
# 2000 (by influence): [1686, 1693, 1691, 1692, 2117, 2162, 2163, 2164, 7787, 8821]
# 3000 (by influence): [2868, 12623, 4653, 4864, 554, 1156, 639, 3002, 3004, 9033]
# 4000 (by influence): [28751, 29830, 33373, 53528, 284, 3423, 3978, 4012, 9401, 13454]
# 5000 (by influence): [1685, 2152, 2218, 2141, 1691, 1693, 2660, 1686, 1687, 704]
# 6000 (by influence): [22596, 40834, 22599, 6015, 53878, 61092, 58637, 37969, 41627, 903]
# 7000 (by influence): [24649, 13775, 28568, 34865, 20401, 7160, 26203, 26206, 20934, 31156]
# 8000 (by influence): [1689, 4758, 13523, 20165, 1209, 7999, 17802, 3169, 4481, 6662]
# 9000 (by influence): [41322, 7999, 21759, 41321, 19228, 19231, 19286, 18388, 13421, 8988]
# 10000 (by influence): [32097, 10452, 280, 552, 12670, 24929, 27028, 53942, 4343, 9989]
# 11000 (by influence): [25839, 10885, 13477, 10621, 1395, 22987, 10076, 41993, 42129, 53544]
# 12000 (by influence): [27846, 3875, 14877, 14884, 8423, 9219, 3878, 3901, 14872, 14902]
# 13000 (by influence): [25755, 27126, 24543, 15869, 25767, 7108, 25823, 12985, 3579, 31248]
# 14000 (by influence): [13609, 1236, 464, 8194, 16596, 305, 774, 2848, 4639, 4971]
# 15000 (by influence): [23656, 11731, 20137, 14484, 31526, 26276, 32017, 20678, 38263, 12333]
# 16000 (by influence): [127, 994, 13746, 27461, 857, 55916, 12822, 1089, 45612, 47458]
# 17000 (by influence): [16998, 16999, 11292, 19151, 27888, 49414, 516, 2723, 4873, 5246]
# 18000 (by influence): [4694, 22964, 6580, 6628, 28110, 39736, 44524, 44526, 44527, 44529]
# 19000 (by influence): [17386, 1027, 1759, 2979, 3633, 4353, 5377, 5380, 5931, 7408]
# 20000 (by influence): [8096, 11756, 14360, 27380, 26799, 4758, 27091, 11742, 28662, 28807]
# 21000 (by influence): [6113, 6373, 7983, 61201, 1504, 5237, 381, 4557, 5651, 5988]
# 22000 (by influence): [18839, 16240, 20511, 7999, 10971, 28361, 3050, 61619, 16239, 26740]
# 23000 (by influence): [28815, 12030, 15148, 26886, 2183, 4459, 24112, 21362, 15150, 15165]
# 24000 (by influence): [2848, 7885, 13404, 20637, 22235, 23615, 32751, 32752, 32753, 150]
# 25000 (by influence): [11038, 16031, 15180, 21136, 15677, 6776, 12024, 30466, 12019, 16030]
# 26000 (by influence): [32025, 32017, 18121, 11731, 26429, 26576, 17906, 18110, 1667, 38879]
# 27000 (by influence): [6221, 10076, 6224, 6205, 6194, 6225, 26910, 6208, 26996, 5788]
# 28000 (by influence): [7033, 17125, 15462, 33049, 51105, 16424, 23, 7996, 725, 1539]
# 29000 (by influence): [28606]
# 30000 (by influence): [862, 869, 919, 941, 3154, 8269, 14473, 14495, 17951, 19611]
# 31000 (by influence): [8148, 21272, 11237, 3326, 20928, 29207, 32236, 20561, 9143, 11317]
# 32000 (by influence): [5146, 20809, 133, 17186, 22299, 28987, 17404, 32668, 16541, 19576]
# 33000 (by influence): [3598, 33001, 3726, 5120, 12321, 13216, 14252, 14676, 19517, 25908]
# 34000 (by influence): [1143, 15400, 4940, 10894, 14099, 15429, 25805, 10887, 5130, 5475]
# 35000 (by influence): [15417, 7743, 26620, 9875, 11702, 25334, 27548, 28282, 1900, 25585]
# 36000 (by influence): [32939, 41053, 35939, 35518, 32930, 31485, 42977, 53473, 28405, 41049]
# 37000 (by influence): [15, 542, 785, 817, 3588, 4374, 5033, 7540, 7576, 7901]
# 38000 (by influence): [994, 5804, 3105, 5698, 9198, 11242, 12095, 12096, 12647, 16927]
# 39000 (by influence): [3635, 14, 429, 10884, 11784, 12991, 3703, 3620, 25563, 122]
# 40000 (by influence): [18359, 21795, 21771, 32905, 42949, 48472, 397, 19719, 21794, 24291]
# 41000 (by influence): [48063, 27803, 40644, 14096, 29523, 17921, 29932, 37866, 779, 1919]
# 42000 (by influence): [2942, 3360, 5711, 5720, 6442, 6670, 8569, 10086, 10102, 10287]
# 43000 (by influence): [57206, 60733, 60734, 8787, 17638, 25872, 35508, 56702, 171, 196]
# 44000 (by influence): [33208, 34316, 43748, 47480, 61395, 6200, 13765, 15447, 17367, 21064]
# 45000 (by influence): [2322, 2338, 3595, 3880, 3897, 3904, 3910, 3922, 3933, 3938]
# 46000 (by influence): [31799, 994, 17344, 33700, 44120, 27583, 27579, 40594, 41282, 13273]
# 47000 (by influence): [6443, 10076, 12846, 25236, 7183, 4736, 7164, 20655, 4733, 16227]
# 48000 (by influence): [25190, 47991, 25172, 33499, 26255, 52067, 47998, 47822, 43047, 26256]
# 49000 (by influence): [2206, 2572, 37817, 48995, 48996, 48997, 48998, 48999, 49001]
# 50000 (by influence): [50001, 20669, 43838, 44533, 50774, 6992, 46451, 19236, 47885, 41197]
# 51000 (by influence): [29845, 40214, 40215, 40217]
# 52000 (by influence): [6349, 17121]
# 53000 (by influence): [51077, 53001, 1524, 3814, 5482, 8415, 8521, 8861, 9126, 10789]
# 54000 (by influence): [994, 1495, 1535, 5309, 5424, 6072, 7341, 16301, 17515, 17586]
# 55000 (by influence): [23503, 34236, 48340, 58009, 47087, 30345, 11504, 21996, 22626, 39190]
# 56000 (by influence): [33925, 13325, 30973, 57979, 58161, 63494, 6498, 10452, 16495, 18926]
# 57000 (by influence): [2714, 23, 554, 3294, 3295, 3358, 3866, 4581, 4963, 5625]
# 58000 (by influence): [25103, 25104, 25108, 25111, 25114, 53837, 55995, 7748, 7750, 7751]
# 59000 (by influence): [3847, 22245, 28648, 30983, 32900, 32905, 35522, 35763, 36099, 38599]
# 60000 (by influence): [10626, 11103, 15446, 24421, 1739, 8252, 14294, 31692, 36702, 44849]
# 61000 (by influence): [38671, 61929, 23, 82, 207, 266, 423, 451, 469, 554]
# 62000 (by influence): [8136, 10483, 10746, 14927, 18006, 18544, 19863, 21264, 21529, 21939]
# 63000 (by influence): [30173, 6930, 21742, 22005, 25114, 40785, 45365, 47055, 58805, 2396]
# 
# Problem 8: 
# 
# Same: 10
# Different: 53
# 
# 
# =============================================================================



































