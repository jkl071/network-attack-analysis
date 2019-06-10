#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:43:22 2018

@author: jamie


directed forgetting single task
pos pos neg con - four conditions full counterbalancing
pos - probe was in memory set
neg - probe was in forget set
con - probe was not in either memory or forget


80 trials total, 20/block, 4 blocks

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/directed_forgetting_single_task_network/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'directed_forgetting_single_task_network_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

directed_forgetting_conditions = ['pos','pos','con','neg']

pos = 0
con = 0
neg = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].directed_forgetting_condition == 'pos':
        pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con':
        con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg':
        neg += 1
        
        
        
print("pos = " + str(pos) + " / " + str(len(test_trials)))
print("con = " + str(con) + " / " + str(len(test_trials)))
print("neg = " + str(neg) + " / " + str(len(test_trials)))


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