#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:29:04 2018

@author: jamie

stop signal with two by two

task switch: stay vs switch
cue switch: stay vs switch
stop: go go stop
full counterbalancing

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'stop_signal_with_cued_task_switching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

SS_stop__task_stay__cue_stay = 0
SS_stop__task_stay__cue_switch = 0
SS_stop__task_switch__cue_stay = 0
SS_stop__task_switch__cue_switch = 0

SS_go__task_stay__cue_stay = 0
SS_go__task_stay__cue_switch = 0
SS_go__task_switch__cue_stay = 0
SS_go__task_switch__cue_switch = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].stop_signal_condition == "stop":
        SS_stop__task_stay__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].stop_signal_condition == "stop":
        SS_stop__task_stay__cue_switch += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].stop_signal_condition == "stop":
        SS_stop__task_switch__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].stop_signal_condition == "stop":
        SS_stop__task_switch__cue_switch += 1
    
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].stop_signal_condition == "go":
        SS_go__task_stay__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].stop_signal_condition == "go":
        SS_go__task_stay__cue_switch += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].stop_signal_condition == "go":
        SS_go__task_switch__cue_stay += 1
    
    elif test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].stop_signal_condition == "go":
        SS_go__task_switch__cue_switch += 1

        
        
print("SS_stop__task_stay__cue_stay = " + str(SS_stop__task_stay__cue_stay) + " / " + str(len(test_trials)))
print("SS_stop__task_stay__cue_switch = " + str(SS_stop__task_stay__cue_switch) + " / " + str(len(test_trials))) 
print("SS_stop__task_switch__cue_stay = " + str(SS_stop__task_switch__cue_stay) + " / " + str(len(test_trials)))
print("SS_stop__task_switch__cue_switch = " + str(SS_stop__task_switch__cue_switch) + " / " + str(len(test_trials)))

print("SS_go__task_stay__cue_stay = " + str(SS_go__task_stay__cue_stay) + " / " + str(len(test_trials)))
print("SS_go__task_stay__cue_switch = " + str(SS_go__task_stay__cue_switch) + " / " + str(len(test_trials))) 
print("SS_go__task_switch__cue_stay = " + str(SS_go__task_switch__cue_stay) + " / " + str(len(test_trials)))
print("SS_go__task_switch__cue_switch = " + str(SS_go__task_switch__cue_switch) + " / " + str(len(test_trials))) 


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