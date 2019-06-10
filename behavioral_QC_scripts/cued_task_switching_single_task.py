#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:10:39 2018

@author: jamie

two by two single task for network grant

4 blocks of 48 trials, 192 total

task switch: stay vs switch
cue switch: stay vs switch
full counterbalancing
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/two_by_two_single_task_network/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'cued_task_switching_single_task_network_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

task_stay__cue_stay = 0
task_stay__cue_switch = 0
task_switch__cue_stay = 0
task_switch__cue_switch = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay":
        task_stay__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch":
        task_stay__cue_switch += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "stay":
        task_switch__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "switch":
        task_switch__cue_switch += 1

        
        
print("task_stay__cue_stay = " + str(task_stay__cue_stay) + " / " + str(len(test_trials)))
print("task_stay__cue_switch = " + str(task_stay__cue_switch) + " / " + str(len(test_trials))) 

print("task_switch__cue_stay = " + str(task_switch__cue_stay) + " / " + str(len(test_trials)))
print("task_switch__cue_switch = " + str(task_switch__cue_switch) + " / " + str(len(test_trials))) 


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