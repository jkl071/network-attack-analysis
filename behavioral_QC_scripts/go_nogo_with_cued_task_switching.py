#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:18:55 2018

@author: jamie

go_nogo_with_two_by_two
go-nogo: go, go, go, go, stop
two by two: 
    task: stay vs switch
    cues: stay vs switch
    
full counterbalancing
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'go_nogo_with_cued_task_switching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

gng_go__task_stay__cue_stay = 0
gng_go__task_stay__cue_switch = 0
gng_go__task_switch__cue_stay = 0
gng_go__task_switch__cue_switch = 0

gng_nogo__task_stay__cue_stay = 0
gng_nogo__task_stay__cue_switch = 0
gng_nogo__task_switch__cue_stay = 0
gng_nogo__task_switch__cue_switch = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].go_no_go_condition == "go" and test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay":
        gng_go__task_stay__cue_stay += 1
    
    elif test_trials.iloc[row].go_no_go_condition == "go" and test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch":
        gng_go__task_stay__cue_switch += 1
    
    elif test_trials.iloc[row].go_no_go_condition == "go" and test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "stay":
        gng_go__task_switch__cue_stay += 1
    
    elif test_trials.iloc[row].go_no_go_condition == "go" and test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "switch":
        gng_go__task_switch__cue_switch += 1
    
    elif test_trials.iloc[row].go_no_go_condition == "nogo" and test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay":
        gng_nogo__task_stay__cue_stay += 1
    
    elif test_trials.iloc[row].go_no_go_condition == "nogo" and test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch":
        gng_nogo__task_stay__cue_switch += 1
    
    elif test_trials.iloc[row].go_no_go_condition == "nogo" and test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "stay":
        gng_nogo__task_switch__cue_stay += 1
    
    elif test_trials.iloc[row].go_no_go_condition == "nogo" and test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "switch":
        gng_nogo__task_switch__cue_switch += 1
        
        
print("gng_go__task_stay__cue_stay = " + str(gng_go__task_stay__cue_stay) + " / " + str(len(test_trials)))
print("gng_go__task_stay__cue_switch = " + str(gng_go__task_stay__cue_switch) + " / " + str(len(test_trials))) 
print("gng_go__task_switch__cue_stay = " + str(gng_go__task_switch__cue_stay) + " / " + str(len(test_trials)))
print("gng_go__task_switch__cue_switch = " + str(gng_go__task_switch__cue_switch) + " / " + str(len(test_trials))) 

print("gng_nogo__task_stay__cue_stay = " + str(gng_nogo__task_stay__cue_stay) + " / " + str(len(test_trials)))
print("gng_nogo__task_stay__cue_switch = " + str(gng_nogo__task_stay__cue_switch) + " / " + str(len(test_trials))) 
print("gng_nogo__task_switch__cue_stay = " + str(gng_nogo__task_switch__cue_stay) + " / " + str(len(test_trials)))
print("gng_nogo__task_switch__cue_switch = " + str(gng_nogo__task_switch__cue_switch) + " / " + str(len(test_trials))) 


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