#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:51:38 2018

@author: jamie

two_by_two_with_directed_forgetting

directed: pos pos con neg
cued: 
    task - switch vs stay
    cue - switch vs stay
    
full counterbalancing
160 total trials, 32 trials per block, 5 blocks total

"""
A3NNB4LWIKA3BQ

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'directed_forgetting_single_task_network_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

directed_neg__task_stay__cue_stay = 0
directed_neg__task_stay__cue_switch = 0
directed_neg__task_switch__cue_stay = 0
directed_neg__task_switch__cue_switch = 0
                 
directed_pos__task_stay__cue_stay = 0
directed_pos__task_stay__cue_switch = 0
directed_pos__task_switch__cue_stay = 0
directed_pos__task_switch__cue_switch = 0

directed_con__task_stay__cue_stay = 0
directed_con__task_stay__cue_switch = 0
directed_con__task_switch__cue_stay = 0
directed_con__task_switch__cue_switch = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].directed_forgetting_condition == 'neg':
        directed_neg__task_stay__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].directed_forgetting_condition == 'neg':
        directed_neg__task_stay__cue_switch += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].directed_forgetting_condition == 'neg':
        directed_neg__task_switch__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].directed_forgetting_condition == 'neg':
        directed_neg__task_switch__cue_switch += 1
        
        
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].directed_forgetting_condition == 'pos':
        directed_pos__task_stay__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].directed_forgetting_condition == 'pos':
        directed_pos__task_stay__cue_switch += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].directed_forgetting_condition == 'pos':
        directed_pos__task_switch__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].directed_forgetting_condition == 'pos':
        directed_pos__task_switch__cue_switch += 1
        
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].directed_forgetting_condition == 'con':
        directed_con__task_stay__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].directed_forgetting_condition == 'con':
        directed_con__task_stay__cue_switch += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].directed_forgetting_condition == 'con':
        directed_con__task_switch__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].directed_forgetting_condition == 'con':
        directed_con__task_switch__cue_switch += 1

        
        
print("directed_neg__task_stay__cue_stay = " + str(directed_neg__task_stay__cue_stay) + " / " + str(len(test_trials)))
print("directed_neg__task_stay__cue_switch = " + str(directed_neg__task_stay__cue_switch) + " / " + str(len(test_trials))) 
print("directed_neg__task_switch__cue_stay = " + str(directed_neg__task_switch__cue_stay) + " / " + str(len(test_trials)))
print("directed_neg__task_switch__cue_switch = " + str(directed_neg__task_switch__cue_switch) + " / " + str(len(test_trials))) 

print("directed_pos__task_stay__cue_stay = " + str(directed_pos__task_stay__cue_stay) + " / " + str(len(test_trials)))
print("directed_pos__task_stay__cue_switch = " + str(directed_pos__task_stay__cue_switch) + " / " + str(len(test_trials))) 
print("directed_pos__task_switch__cue_stay = " + str(directed_pos__task_switch__cue_stay) + " / " + str(len(test_trials)))
print("directed_pos__task_switch__cue_switch = " + str(directed_pos__task_switch__cue_switch) + " / " + str(len(test_trials))) 

print("directed_con__task_stay__cue_stay = " + str(directed_con__task_stay__cue_stay) + " / " + str(len(test_trials)))
print("directed_con__task_stay__cue_switch = " + str(directed_con__task_stay__cue_switch) + " / " + str(len(test_trials))) 
print("directed_con__task_switch__cue_stay = " + str(directed_con__task_switch__cue_stay) + " / " + str(len(test_trials)))
print("directed_con__task_switch__cue_switch = " + str(directed_con__task_switch__cue_switch) + " / " + str(len(test_trials))) 


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