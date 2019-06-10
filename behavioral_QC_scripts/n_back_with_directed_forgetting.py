#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 22:27:26 2018

@author: jamie

n_back_with_directed_forgetting

N-Back: ['match','mismatch','mismatch','mismatch','mismatch']
Directed Forgetting: ['forget','remember']

10 minimum trials 
full counterbalancing
240 total trials, 40 trials per block, 6 blocks total

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/n_back_with_directed_forgetting/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'n_back_with_directed_forgetting_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

nback_conditions = ['match','mismatch']
delays = ['1','2','3']

directed_rememember__one_match = 0
directed_rememember__one_mismatch = 0
directed_rememember__two_match = 0
directed_rememember__two_mismatch = 0
directed_rememember__three_match = 0
directed_rememember__three_mismatch = 0

directed_forget__one_match = 0
directed_forget__one_mismatch = 0
directed_forget__two_match = 0
directed_forget__two_mismatch = 0
directed_forget__three_match = 0
directed_forget__three_mismatch = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].directed_forgetting_condition == 'remember':
        directed_rememember__one_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].directed_forgetting_condition == 'remember':
        directed_rememember__one_mismatch += 1
  
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].directed_forgetting_condition == 'remember':
        directed_rememember__two_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].directed_forgetting_condition == 'remember':
        directed_rememember__two_mismatch += 1
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].directed_forgetting_condition == 'remember':
        directed_rememember__three_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].directed_forgetting_condition == 'remember':
        directed_rememember__three_mismatch += 1
        
        
        
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].directed_forgetting_condition == 'forget':
        directed_forget__one_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].directed_forgetting_condition == 'forget':
        directed_forget__one_mismatch += 1
  
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].directed_forgetting_condition == 'forget':
        directed_forget__two_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].directed_forgetting_condition == 'forget':
        directed_forget__two_mismatch += 1
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].directed_forgetting_condition == 'forget':
        directed_forget__three_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].directed_forgetting_condition == 'forget':
        directed_forget__three_mismatch += 1
        
        
        
print("directed_rememember__one_match = " + str(directed_rememember__one_match) + " / " + str(len(test_trials)))
print("directed_rememember__one_mismatch = " + str(directed_rememember__one_mismatch) + " / " + str(len(test_trials)))
print("directed_rememember__two_match = " + str(directed_rememember__two_match) + " / " + str(len(test_trials)))
print("directed_rememember__two_mismatch = " + str(directed_rememember__two_mismatch) + " / " + str(len(test_trials)))
print("directed_rememember__three_match = " + str(directed_rememember__three_match) + " / " + str(len(test_trials)))
print("directed_rememember__three_mismatch = " + str(directed_rememember__three_mismatch) + " / " + str(len(test_trials)))


print("directed_forget__one_match = " + str(directed_forget__one_match) + " / " + str(len(test_trials)))
print("directed_forget__one_mismatch = " + str(directed_forget__one_mismatch) + " / " + str(len(test_trials)))
print("directed_forget__two_match = " + str(directed_forget__two_match) + " / " + str(len(test_trials)))
print("directed_forget__two_mismatch = " + str(directed_forget__two_mismatch) + " / " + str(len(test_trials)))
print("directed_forget__three_match = " + str(directed_forget__three_match) + " / " + str(len(test_trials)))
print("directed_forget__three_mismatch = " + str(directed_forget__three_mismatch) + " / " + str(len(test_trials)))



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