#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:26:29 2018

@author: jamie

go_nogo_with_directed_forgetting


GNG: ['go','go','go','go','stop']
Directed: ['pos', 'pos', 'neg', 'con']

20 minimum trials
full counterbalancing

180 total trials, 20 trials per block, 9 blocks total
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/go_nogo_with_directed_forgetting/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'go_nogo_with_directed_forgetting_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

directed_forgetting_conditions = ['pos','pos','con','neg']

gng_go__pos = 0
gng_go__con = 0
gng_go__neg = 0

gng_nogo__pos = 0
gng_nogo__con = 0
gng_nogo__neg = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].directed_forgetting_condition == 'pos' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__neg += 1
        
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'pos' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__neg += 1
        
        
        
print("gng_go__pos = " + str(gng_go__pos) + " / " + str(len(test_trials)))
print("gng_go__con = " + str(gng_go__con) + " / " + str(len(test_trials)))
print("gng_go__neg = " + str(gng_go__neg) + " / " + str(len(test_trials)))

print("gng_nogo__pos = " + str(gng_nogo__pos) + " / " + str(len(test_trials)))
print("gng_nogo__con = " + str(gng_nogo__con) + " / " + str(len(test_trials)))
print("gng_nogo__neg = " + str(gng_nogo__neg) + " / " + str(len(test_trials)))


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

