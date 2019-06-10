#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:49:30 2018

@author: jamie

go_nogo_with_predictable_task_switching

300 total trials, 60 trials per block, 5 blocks total

GNG: ['go','go','go','go','nogo']
Predictive: 2 (switch or stay) by 2 (mag or parity)

20 minimum trials
full counterbalancing
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'go_nogo_with_predictable_task_switching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

predictive_stay__gng_go = 0 
predictive_stay__gng_nogo = 0
predictive_switch__gng_go = 0
predictive_switch__gng_nogo = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].predictive_condition == "stay" and test_trials.iloc[row].go_nogo_condition == "go":
        predictive_stay__gng_go += 1
    
    elif test_trials.iloc[row].predictive_condition == "stay" and test_trials.iloc[row].go_nogo_condition == "nogo":
        predictive_stay__gng_nogo += 1
    
    elif test_trials.iloc[row].predictive_condition == "switch" and test_trials.iloc[row].go_nogo_condition == "go":
        predictive_switch__gng_go += 1
    
    elif test_trials.iloc[row].predictive_condition == "switch" and test_trials.iloc[row].go_nogo_condition == "nogo":
        predictive_switch__gng_nogo += 1

        
        
print("predictive_stay__gng_go = " + str(predictive_stay__gng_go) + " / " + str(len(test_trials)))
print("predictive_stay__gng_nogo = " + str(predictive_stay__gng_nogo) + " / " + str(len(test_trials))) 

print("predictive_switch__gng_go = " + str(predictive_switch__gng_go) + " / " + str(len(test_trials)))
print("predictive_switch__gng_nogo = " + str(predictive_switch__gng_nogo) + " / " + str(len(test_trials))) 


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
