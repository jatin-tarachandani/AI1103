# -*- coding: utf-8 -*-
import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

#Raw probability data given in the question

prob_def_a=0.02*0.6# Probability that an item is made in A and defective
prob_def_b=0.01*0.4# Probability that an item is made in B and defective

trials=int(1e7)
 #Calculating the bernoulli distributions for 10000000 trials with p being the probability of defective item from A, or from B
defect_a_dist=bernoulli.rvs(prob_def_a, size=trials)
defect_b_dist=bernoulli.rvs(prob_def_b, size=trials)

#Here, since the Bernoulli distribution returns 1 for a succesful trial and 0 for an unsuccesful one, we can directly take the mean of the array elements
#.i.e number of successful trials divided by the total number of trials
exp_prob_def_a=np.mean(defect_a_dist)
exp_prob_def_b=np.mean(defect_b_dist)

#Taking these as our probability values and applying Bayes Theorem we get the probability of a defective item coming from B
final_exp_prob=exp_prob_def_b/(exp_prob_def_a+exp_prob_def_b)
final_theo_prob=prob_def_b/(prob_def_b+prob_def_a)
print("The experimentally obtained probability of the defective part coming from B is ", final_exp_prob)
print("The theoretically determined probability of the defective part coming from B is ", final_theo_prob)
