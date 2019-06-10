#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:44:46 2018

@author: jamie

checks trial types and timing for:
    flanker with two by two

exp calls for 40 trials per block, 240 trials total, 6 blocks.

conditions:
Flanker: ['congruent','incongruent']
two by two: 2 task (switch or stay) 
two by two: 2 cue (switch or stay)
full counterbalancing 
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'flanker_with_cued_task_switching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice
                 

task_stay__cue_stay__congruent = 0
task_stay__cue_stay__incongruent = 0

task_stay__cue_switch__congruent = 0
task_stay__cue_switch__incongruent = 0

task_switch__cue_stay__congruent = 0
task_switch__cue_stay__incongruent = 0

task_switch__cue_switch__congruent = 0
task_switch__cue_switch__incongruent = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].flanker_condition == "congruent":
        task_stay__cue_stay__congruent += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].flanker_condition == "incongruent":
        task_stay__cue_stay__incongruent += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].flanker_condition == "congruent":
        task_stay__cue_switch__congruent += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].flanker_condition == "incongruent":
        task_stay__cue_switch__incongruent += 1
    
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].flanker_condition == "congruent":
        task_switch__cue_stay__congruent += 1
    
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].flanker_condition == "incongruent":
        task_switch__cue_stay__incongruent += 1
    
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].flanker_condition == "congruent":
        task_switch__cue_switch__congruent += 1
    
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].flanker_condition == "incongruent":
        task_switch__cue_switch__incongruent += 1
        
        
print("task_stay__cue_stay__congruent = " + str(task_stay__cue_stay__congruent) + " / " + str(len(test_trials)))
print("task_stay__cue_stay__incongruent = " + str(task_stay__cue_stay__incongruent) + " / " + str(len(test_trials))) 
print("task_stay__cue_switch__congruent = " + str(task_stay__cue_switch__congruent) + " / " + str(len(test_trials))) 
print("task_stay__cue_switch__incongruent = " + str(task_stay__cue_switch__incongruent) + " / " + str(len(test_trials))) 

print("task_switch__cue_stay__congruent = " + str(task_switch__cue_stay__congruent) + " / " + str(len(test_trials)))
print("task_switch__cue_stay__incongruent = " + str(task_switch__cue_stay__incongruent) + " / " + str(len(test_trials))) 
print("task_switch__cue_switch__congruent = " + str(task_switch__cue_switch__congruent) + " / " + str(len(test_trials))) 
print("task_switch__cue_switch__incongruent = " + str(task_switch__cue_switch__incongruent) + " / " + str(len(test_trials))) 


        
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