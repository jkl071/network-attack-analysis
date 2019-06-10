#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:20:20 2018

@author: jamie

checks trial types for flanker with predictive task switching

exp calls for 40 trials per block, 200 trials total, 5 blocks.
Due to the nature of the predictive_task, I added 1 throwaway trial at the beginning, 
to have full set of switch vs stay trials. 

conditions:
Flanker: ['congruent','incongruent']
Predictive: 2 (switch or stay) 
full counterbalancing 
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'flanker_with_predictable_task_switching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice
                 
congruent_switch = 0
congruent_stay = 0
incongruent_switch = 0
incongruent_stay = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].predictive_condition == "stay" and test_trials.iloc[row].flanker_condition == "congruent":
        congruent_stay += 1
    elif test_trials.iloc[row].predictive_condition == "stay" and test_trials.iloc[row].flanker_condition == "incongruent":
        incongruent_stay += 1
    elif test_trials.iloc[row].predictive_condition == "switch" and test_trials.iloc[row].flanker_condition == "incongruent":
        incongruent_switch += 1
    elif test_trials.iloc[row].predictive_condition == "switch" and test_trials.iloc[row].flanker_condition == "congruent":
        congruent_switch += 1
        
        
        
print("congruent_switch = " + str(congruent_switch) + " / " + str(len(test_trials)))
print("incongruent_switch = " + str(incongruent_switch) + " / " + str(len(test_trials))) 
print("incongruent_stay = " + str(incongruent_stay) + " / " + str(len(test_trials))) 
print("congruent_stay = " + str(congruent_stay) + " / " + str(len(test_trials))) 
    

suspect_trial_timing = []
for row in range(0,len(df)-1):
    actual_duration = df.iloc[row + 1].time_elapsed - df.iloc[row].time_elapsed
    expected_duration = df.iloc[row + 1].block_duration + df.iloc[row].timing_post_trial
    if df.iloc[row + 1].trial_type == 'poldrack-categorize':
            expected_duration += 500
    if abs(expected_duration - actual_duration) > 50:
        suspect_trial_timing.append(str(df.iloc[row + 1].trial_index) + '_' + 
                                    task + '_' + 
                                    str(abs(expected_duration - actual_duration)) + '_' + 
                                    str(actual_duration) + '_' + 
                                    df.iloc[row + 1].trial_id + '_' +
                                    df.iloc[row + 1].trial_type)
        
if len(suspect_trial_timing) == 0:
    print('no suspect timing issues')
else: 
    print('check suspect_trial_timing array - this exp has been fixed')