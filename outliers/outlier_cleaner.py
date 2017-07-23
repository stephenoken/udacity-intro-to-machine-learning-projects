#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    # cleaned_data = []

    ### your code goes here
    
    data = zip(ages, net_worths, predictions) 
    analysed_data = map(lambda x: (x[0], x[1], x[2]/x[1]), data) 
    removing_number = len(analysed_data) * 0.1
    removing_index = int(len(analysed_data) - removing_number)
    cleaned_data = sorted(analysed_data, key= lambda x: x[2])[:removing_index]
    print cleaned_data[0]
    return cleaned_data

