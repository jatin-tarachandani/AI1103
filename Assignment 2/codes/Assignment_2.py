# -*- coding: utf-8 -*-
import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

success=0.5
trials=int(1e7)
#Generating three separate arrays of Bernoulli distibutions to store the first, second and third tosses of each trial. (I did this since I believe binomial distribution does not provide info about the order of the successes/failures)
first_toss_arr=bernoulli.rvs(p=success, size=trials)
second_toss_arr=bernoulli.rvs(p=success, size=trials)
third_toss_arr=bernoulli.rvs(p=success, size=trials)

counter=0 #this number counts the number of times that we got exactly 2 heads in the three tosses i.e only one head in the remaining 2 tosses after the first one is confirmed head
#Now taking the indices of the times when the first toss was head, i.e the value in first_toss_arr was 1
first_head_arr=np.nonzero(first_toss_arr)
for x in range(int(1e7)):
    if first_toss_arr[x]!=0:#only if the first toss was head tdo we even consider the case
        if second_toss_arr[x]+third_toss_arr[x]==1:#if the sum is one for two elements that are either 0 or 1, then one and only one of them must be one
            counter+=1
    
        
#counter now has a record of the number of times we obtained one additional head, making exactly 2 heads in three tosses.

exp_prob=counter/np.size(first_head_arr)
theo_prob=0.5
print("The theoretical probability is", theo_prob)    
print("The experimental probability is ", exp_prob)