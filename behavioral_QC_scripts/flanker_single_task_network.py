#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:53:40 2018

@author: jamie

checks trial types for flanker single task network

exp calls for 48 trials per block, 96 trials total. 
Half should be incompatible
half should be compatible
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'flanker_single_task_network_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice
                 
incompatible = 0
compatible = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].condition == "compatible":
        compatible += 1
    elif test_trials.iloc[row].condition == "incompatible":
        incompatible += 1
        
print("compatible = " + str(compatible) + " / " + str(len(test_trials)))
print("incompatible = " + str(incompatible) + " / " + str(len(test_trials))) 
    

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