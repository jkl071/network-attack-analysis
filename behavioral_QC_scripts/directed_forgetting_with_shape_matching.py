#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:18:57 2018

@author: jamie


directed_forgetting_with_shape_matching

directed: pos pos neg con
shape matching: match mismatch

8 = lowest number of trials
full counterbalancing
160 trials total, 32 per block, 5 blocks

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'directed_forgetting_with_shape_matching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

directed_forgetting_conditions = ['pos','pos','con','neg']

match__pos = 0
match__con = 0
match__neg = 0

mismatch__pos = 0
mismatch__con = 0
mismatch__neg = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].directed_forgetting_condition == 'pos' and test_trials.iloc[row].shape_matching_condition == 'match':
        match__pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con' and test_trials.iloc[row].shape_matching_condition == 'match':
        match__con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg' and test_trials.iloc[row].shape_matching_condition == 'match':
        match__neg += 1
        
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'pos' and test_trials.iloc[row].shape_matching_condition == 'mismatch':
        mismatch__pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con' and test_trials.iloc[row].shape_matching_condition == 'mismatch':
        mismatch__con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg' and test_trials.iloc[row].shape_matching_condition == 'mismatch':
        mismatch__neg += 1
        
    
        
        
print("match__pos = " + str(match__pos) + " / " + str(len(test_trials)))
print("match__con = " + str(match__con) + " / " + str(len(test_trials)))
print("match__neg = " + str(match__neg) + " / " + str(len(test_trials)))

print("mismatch__pos = " + str(mismatch__pos) + " / " + str(len(test_trials)))
print("mismatch__con = " + str(mismatch__con) + " / " + str(len(test_trials)))
print("mismatch__neg = " + str(mismatch__neg) + " / " + str(len(test_trials)))


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