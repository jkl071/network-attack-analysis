#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:19:54 2018

@author: jamie

n_back_with_predictable_task_switching

predictive: 
    task - switch vs stay
    task: 1back or 2back
    
n_back: ['match','mismatch','mismatch','mismatch','mismatch']
delays: 1back or 2back

240 trials total, 40 trials per block, 6 blocks
note: each block has both 1 and 2-back trials.

"""

import pandas as pd

input_path = "~/Desktop/network_tasks_output_files/n_back_with_predictable_task_switching/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'n_back_with_predictable_task_switching_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

predictive_stay__mismatch = 0 
predictive_stay__match = 0
predictive_switch__mismatch = 0
predictive_switch__match = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].predictive_condition == "stay" and test_trials.iloc[row].n_back_condition == "mismatch":
        predictive_stay__mismatch += 1
    
    elif test_trials.iloc[row].predictive_condition == "stay" and test_trials.iloc[row].n_back_condition == "match":
        predictive_stay__match += 1
    
    elif test_trials.iloc[row].predictive_condition == "switch" and test_trials.iloc[row].n_back_condition == "mismatch":
        predictive_switch__mismatch += 1
    
    elif test_trials.iloc[row].predictive_condition == "switch" and test_trials.iloc[row].n_back_condition == "match":
        predictive_switch__match += 1

        
        
print("predictive_stay__mismatch = " + str(predictive_stay__mismatch) + " / " + str(len(test_trials)))
print("predictive_stay__match = " + str(predictive_stay__match) + " / " + str(len(test_trials))) 

print("predictive_switch__mismatch = " + str(predictive_switch__mismatch) + " / " + str(len(test_trials)))
print("predictive_switch__match = " + str(predictive_switch__match) + " / " + str(len(test_trials))) 


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