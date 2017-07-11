#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from __future__ import division
import pickle
from functools import reduce

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print len(list(filter(lambda x: x[1]["poi"], enron_data.iteritems())))

print(enron_data["PRENTICE JAMES"]["total_stock_value"])

print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

big_three = {k: enron_data[k] for k in ("SKILLING JEFFREY K","LAY KENNETH L", "FASTOW ANDREW S")}
biggest_hitter =  reduce(lambda prev, curr: curr if curr[1]["total_payments"] >= prev[1]["total_payments"] else prev,big_three.iteritems())

print "{} took home {}".format(biggest_hitter[0], biggest_hitter[1]["total_payments"])

num_of_quantified_salaries = len(filter(lambda x: x[1]["salary"] != 'NaN', enron_data.iteritems()))

num_of_known_email_addresses = len(filter(lambda x: x[1]["email_address"] != 'NaN', enron_data.iteritems()))

print "No. of known salaries: {}\nNo. of known emails: {}".format(num_of_quantified_salaries, num_of_known_email_addresses)

pois = filter(lambda x: x[1]["poi"], enron_data.iteritems())
num_of_unkown_payments =  len(filter(lambda x: x[1]["total_payments"]=='NaN', pois)) / len(pois)

print num_of_unkown_payments


more_data = list(enron_data.iteritems()) + [(str(i),{"poi": True, "total_payments": "NaN"}) for i in range(10)]

print len(more_data)

print len(filter( lambda x: x[1]["total_payments"] == "NaN", more_data))

more_pois = filter(lambda x: x[1]["poi"], more_data)

print len(more_pois)
print len(filter(lambda x: x[1]["total_payments"] == "NaN", more_pois))
