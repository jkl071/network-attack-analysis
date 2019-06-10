#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:32:44 2018

@author: jamie

nback single task network
condition (match match match match mismatch)
delay (1,2,3)
15 trials - full counterbalancing


150 total trials, 50/block, 3 blocks
note: nback tasks must have multiples of 3 blocks, 1 for each delay (1,2,3)
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'n_back_single_task_network_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

nback_conditions = ['match','mismatch']
delays = ['1','2','3']

one_match = 0
one_mismatch = 0
two_match = 0
two_mismatch = 0
three_match = 0
three_mismatch = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 1:
        one_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 1:
        one_mismatch += 1
  
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 2:
        two_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 2:
        two_mismatch += 1
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 3:
        three_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 3:
        three_mismatch += 1
        
        
        
print("one_match = " + str(one_match) + " / " + str(len(test_trials)))
print("one_mismatch = " + str(one_mismatch) + " / " + str(len(test_trials)))

print("two_match = " + str(two_match) + " / " + str(len(test_trials)))
print("two_mismatch = " + str(two_mismatch) + " / " + str(len(test_trials)))

print("three_match = " + str(three_match) + " / " + str(len(test_trials)))
print("three_mismatch = " + str(three_mismatch) + " / " + str(len(test_trials)))



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
    print('check suspect_trial_timing array')