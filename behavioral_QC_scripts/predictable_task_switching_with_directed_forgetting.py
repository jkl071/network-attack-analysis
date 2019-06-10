#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:20:44 2018

@author: jamie

predictable_task_switching_with_directed_forgetting

160 total trials, 32 trials per block, 5 blocks

predictive: switch or stay
directed: pos pos neg con

full counterbalancing
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/predictable_task_switching_with_directed_forgetting/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'predictable_task_switching_with_directed_forgetting_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

directed_forgetting_conditions = ['pos','pos','con','neg']

switch__pos = 0
switch__con = 0
switch__neg = 0

stay__pos = 0
stay__con = 0
stay__neg = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].directed_forgetting_condition == 'pos' and test_trials.iloc[row].predictive_condition == 'switch':
        switch__pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con' and test_trials.iloc[row].predictive_condition == 'switch':
        switch__con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg' and test_trials.iloc[row].predictive_condition == 'switch':
        switch__neg += 1
        
    
    elif test_trials.iloc[row].directed_forgetting_condition == 'pos' and test_trials.iloc[row].predictive_condition == 'stay':
        stay__pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con' and test_trials.iloc[row].predictive_condition == 'stay':
        stay__con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg' and test_trials.iloc[row].predictive_condition == 'stay':
        stay__neg += 1
        
        
print("switch__pos = " + str(switch__pos) + " / " + str(len(test_trials)))
print("switch__con = " + str(switch__con) + " / " + str(len(test_trials)))
print("switch__neg = " + str(switch__neg) + " / " + str(len(test_trials)))

print("stay__pos = " + str(stay__pos) + " / " + str(len(test_trials)))
print("stay__con = " + str(stay__con) + " / " + str(len(test_trials)))
print("stay__neg = " + str(stay__neg) + " / " + str(len(test_trials)))


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