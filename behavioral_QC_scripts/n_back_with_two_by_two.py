#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:12:42 2018

@author: jamie

n back with two by two

nback : 1back vs 2back
two by two -
task: stay vs switch
    task - 1back vs 2 back
cues: stay vs switch
    cues - one-ago & 1-back  vs two-ago & 2-back
    
full counterbalancing

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'n_back_with_cued_task_switching_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

nback_match__task_stay__cue_stay = 0
nback_match__task_stay__cue_switch = 0
nback_match__task_switch__cue_stay = 0
nback_match__task_switch__cue_switch = 0

nback_mismatch__task_stay__cue_stay = 0
nback_mismatch__task_stay__cue_switch = 0
nback_mismatch__task_switch__cue_stay = 0
nback_mismatch__task_switch__cue_switch = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].n_back_condition == "mismatch" and test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay":
        nback_mismatch__task_stay__cue_stay += 1
    
    elif test_trials.iloc[row].n_back_condition == "mismatch" and test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch":
        nback_mismatch__task_stay__cue_switch += 1
    
    elif test_trials.iloc[row].n_back_condition == "mismatch" and test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "stay":
        nback_mismatch__task_switch__cue_stay += 1
    
    elif test_trials.iloc[row].n_back_condition == "mismatch" and test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "switch":
        nback_mismatch__task_switch__cue_switch += 1

        
        
    elif test_trials.iloc[row].n_back_condition == "match" and test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay":
        nback_match__task_stay__cue_stay += 1
    
    elif test_trials.iloc[row].n_back_condition == "match" and test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch":
        nback_match__task_stay__cue_switch += 1
    
    elif test_trials.iloc[row].n_back_condition == "match" and test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "stay":
        nback_match__task_switch__cue_stay += 1
    
    elif test_trials.iloc[row].n_back_condition == "match" and test_trials.iloc[row].task_condition == "switch" and test_trials.iloc[row].cue_condition == "switch":
        nback_match__task_switch__cue_switch += 1
        
        
print("nback_match__task_stay__cue_stay = " + str(nback_match__task_stay__cue_stay) + " / " + str(len(test_trials)))
print("nback_match__task_stay__cue_switch = " + str(nback_match__task_stay__cue_switch) + " / " + str(len(test_trials))) 
print("nback_match__task_switch__cue_stay = " + str(nback_match__task_switch__cue_stay) + " / " + str(len(test_trials)))
print("nback_match__task_switch__cue_switch = " + str(nback_match__task_switch__cue_switch) + " / " + str(len(test_trials))) 

print("nback_mismatch__task_stay__cue_stay = " + str(nback_mismatch__task_stay__cue_stay) + " / " + str(len(test_trials)))
print("nback_mismatch__task_stay__cue_switch = " + str(nback_mismatch__task_stay__cue_switch) + " / " + str(len(test_trials))) 
print("nback_mismatch__task_switch__cue_stay = " + str(nback_mismatch__task_switch__cue_stay) + " / " + str(len(test_trials)))
print("nback_mismatch__task_switch__cue_switch = " + str(nback_mismatch__task_switch__cue_switch) + " / " + str(len(test_trials))) 


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