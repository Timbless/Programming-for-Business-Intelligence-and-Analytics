# Name: ...
# ID: ...
# Homework 3: Election prediction

import csv
import os
import time

def read_csv(path):
    """
    Reads the CSV file at path, and returns a list of rows. Each row is a
    dictionary that maps a column name to a value in that column, as a string.
    """
    output = []
    for row in csv.DictReader(open(path)):
        output.append(row)
    return output


################################################################################
# Problem 1: State edges
################################################################################

def row_to_edge(row):
    """
    Given an election result row or poll data row, returns the Democratic edge
    in that state.
    """
    return float(row["Dem"]) - float(row["Rep"])  

def state_edges(election_result_rows):
    """
    Given a list of election result rows, returns state edges.
    The input list does has no duplicate states;
    that is, each state is represented at most once in the input list.
    """
    #TODO: Implement this function
    state_edges = {}#create a dictionary 
    for row in election_result_rows: #implement each row in election_result_rows
        state_name = row['State'] # the dictionary key is the State
        state_edges[state_name] = row_to_edge(row) #the value is state edge we solved in function row_to_edge(row)
    return state_edges


################################################################################
# Problem 2: Find the most recent poll row
################################################################################

def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if 
    date1 is after date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of poll data rows, returns the most recent row with the
    specified pollster and state. If no such row exists, returns None.
    """
    #TODO: Implement this function
    recent = None #initialize our result to be None, and if input are not satisfy our correct condition we print None
    for i in range(len(poll_rows)): # create a loop to save correct Pollster and State, total iteration is len(poll_rows)-1
        if poll_rows[i]['Pollster'] == pollster and poll_rows[i]['State'] == state: # correct condition
            recent = poll_rows[i] #save the correct data
            if earlier_date(poll_rows[i]['Date'], recent['Date']): #when poll_rows date is after recent date
                recent = poll_rows[i] #update the recent date 
    return recent

################################################################################
# Problem 3: Pollster predictions
################################################################################

def unique_column_values(rows, column_name):
    """
    Given a list of rows and the name of a column (a string), returns a set
    containing all values in that column.
    """
    #TODO: Implement this function
   
    unique_list = [] #create an empty list 
    for row in rows: #create a loop which can search every column_name from rows list
        unique_list.append(row[column_name]) # implement the each column_name from rows list into our list 

    return set(unique_list)

def pollster_predictions(poll_rows):
    """
    Given a list of poll data rows, returns pollster predictions.
    """
    #TODO: Implement this function
    predict = dict()  #create an empty dictionary
    pollsters = unique_column_values(poll_rows, "Pollster")  # this gives us all pollster value
    states = unique_column_values(poll_rows, "State") # this gives us all state value
    for i in pollsters:
        polldict = dict()  #create a dictionary that saves all values
        for j in states:
            if most_recent_poll_row(poll_rows, i, j) != None: #check if recent is not empty list
                poll = most_recent_poll_row(poll_rows, i, j) # reture the most recent poll value
                polldict[j] = row_to_edge(poll) #value is row_to_edge
        predict[i] = polldict # save our result into predict dictionary
    return predict 



            
################################################################################
# Problem 4: Pollster errors
################################################################################

def average_error(state_edges_predicted, state_edges_actual):
    """
    Given predicted state edges and actual state edges, returns
    the average error of the prediction.
    """
    #TODO: Implement this function
    n = 0 #initialize the total number of results
    sum = 0 # initialize the total sum of results
    for i in state_edges_predicted:
        sum += abs(state_edges_predicted[i] - state_edges_actual[i]) #sum should be absolute valuse of difference of each row
        n += 1 #iterate total number of results
    return sum/n #reture our average

def pollster_errors(pollster_predictions, state_edges_actual):
    """
    Given pollster predictions and actual state edges, retuns pollster errors.
    """
    #TODO: Implement this function
    perror = {} #create a dictionary
    for i in pollster_predictions: # create a loop that find each prediction - state_edge_actual
        perror[i] = average_error(pollster_predictions[i], state_edges_actual) #save it into perror
    return perror 


################################################################################
# Problem 5: Pivot a nested dictionary
################################################################################

def pivot_nested_dict(nested_dict):
    """
    Pivots a nested dictionary, producing a different nested dictionary
    containing the same values.
    The input is a dictionary d1 that maps from keys k1 to dictionaries d2,
    where d2 maps from keys k2 to values v.
    The output is a dictionary d3 that maps from keys k2 to dictionaries d4,
    where d4 maps from keys k1 to values v.
    For example:
      input = { "a" : { "x": 1, "y": 2 },
                "b" : { "x": 3, "z": 4 } }
      output = {'y': {'a': 2},
                'x': {'a': 1, 'b': 3},
                'z': {'b': 4} }
    """
     #TODO: Implement this function
    pivot_dict = {} #create a new dictionary
    for key in nested_dict.keys(): #this loop is to get outer key value
        for ikey in nested_dict[key].keys(): 
            pivot_dict[ikey] = {} #create a new dictionary for outer key
    for key in nested_dict.keys(): #this loop is to get inner key value
        for jkey in nested_dict[key].keys():
            pivot_dict[jkey][key] = nested_dict[key][jkey] #switch outer key and inner key
    return pivot_dict


    

################################################################################
# Problem 6: Average the edges in a single state
################################################################################

def average_error_to_weight(error):
    """
    Given the average error of a pollster, returns that pollster's weight.
    The error must be a positive number.
    """
    return error ** (-2)

# The default average error of a pollster who did no polling in the
# previous election.
DEFAULT_AVERAGE_ERROR = 5.0

def pollster_to_weight(pollster, pollster_errors):
    """"
    Given a pollster and a pollster errors, return the given pollster's weight.
    """
    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):
    """
    Returns the weighted average of a list of items.
    
    Arguments:
    items is a list of numbers.
    weights is a list of numbers, whose sum is nonzero.
    
    Each weight in weights corresponds to the item in items at the same index.
    items and weights must be the same length.
    """
    assert len(items) > 0
    assert len(items) == len(weights)
    #TODO: Implement this function
    sumnumerator = 0 # initialize w1x1 + .... + wnxn
    sumdenominator = 0 # initialize w1 + ... + wn
    for i, j in zip(items, weights): # use zip function to pack items and weights 
        sumnumerator += i * j
        sumdenominator += j
    return sumnumerator/sumdenominator # w1x1 + .... + wnxn/w1 + ... + wn

def average_edge(pollster_edges, pollster_errors):
    """
    Given pollster edges and pollster errors, returns the average of these edges
    weighted by their respective pollster errors.
    """
    #TODO: Implement this function

    pollster_weight = {} #create a dictionary to saving all pollster weight result ()
    weights = {} # create a dictionary 
    for pollster in pollster_edges:
        pollster_weight[pollster] = pollster_to_weight(pollster,pollster_errors) # use pollster_to_weight function to get pollster_weight
    for pollster in pollster_edges:
        weights = weighted_average(pollster_edges.values(),pollster_weight.values()) # then we input first loop result
    #print weights
    return weights


    
################################################################################
# Problem 7: Predict the 2012 election
################################################################################

def predict_state_edges(pollster_predictions, pollster_errors):
    """
    Given pollster predictions from a current election and pollster errors from
    a past election, returns the predicted state edges of the current election.
    """
    #TODO: Implement this function
    state_edges = dict() #create a dictionary for state edge
    state_predictions = pivot_nested_dict(pollster_predictions) # use pivot_nested_dict function to get each pollster prediction in state form
    for i in state_predictions:
        temp = state_predictions[i]# only copy the each value of state_prediction rather than all copy
        state_edges[i] = average_edge(temp, pollster_errors) # run our average_edge function to get final result save it in our dictionary
    return state_edges


################################################################################
# Electoral College, Main Function, etc.
################################################################################

def electoral_college_outcome(ec_rows, state_edges):
    """
    Given electoral college rows and state edges, returns the outcome of
    the Electoral College, as a map from "Dem" or "Rep" to a number of
    electoral votes won.  If a state has an edge of exactly 0.0, its votes
    are evenly divided between both parties.
    """
    ec_votes = {}               # maps from state to number of electoral votes
    for row in ec_rows:
        ec_votes[row["State"]] = float(row["Electors"])

    outcome = {"Dem": 0, "Rep": 0}
    for state in state_edges:
        votes = ec_votes[state]
        if state_edges[state] > 0:
            outcome["Dem"] += votes
        elif state_edges[state] < 0:
            outcome["Rep"] += votes
        else:
            outcome["Dem"] += votes/2.0
            outcome["Rep"] += votes/2.0
    return outcome


def print_dict(dictionary):
    """
    Given a dictionary, prints its contents in sorted order by key.
    Rounds float values to 8 decimal places.
    """
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if type(value) == float:
            value = round(value, 8)
        print (key, value)


def main():
    """
    Main function, which is executed when election.py is run as a Python script.
    """
    # Read state edges from the 2008 election
    edges_2008 = state_edges(read_csv("data/2008-results.csv"))
    
    # Read pollster predictions from the 2008 and 2012 election
    polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
    polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))
    
    # Compute pollster errors for the 2008 election
    error_2008 = pollster_errors(polls_2008, edges_2008)
    
    # Predict the 2012 state edges
    prediction_2012 = predict_state_edges(polls_2012, error_2008)
    
    # Obtain the 2012 Electoral College outcome
    ec_2012 = electoral_college_outcome(read_csv("data/2012-electoral-college.csv"),
                                        prediction_2012)
    
    print ("Predicted 2012 election results:")
    print_dict(prediction_2012)
    print
    
    print ("Predicted 2012 Electoral College outcome:")
    print_dict(ec_2012)
    print    


# If this file, election.py, is run as a Python script (such as by typing
# "python election.py" at the command shell), then run the main() function.
if __name__ == "__main__":
    main()
