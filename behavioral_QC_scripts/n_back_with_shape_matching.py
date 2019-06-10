#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:38:29 2018

@author: jamie

n_back_with_shape_matching

shape: match vs mismatch
nback: match match match match mismatch
nback: 3 delays, 1,2,3

full counterbalancing
10 minimum trials

240 trials total, 40 trials each block, 6 blocks
note: this nback needs to have block % 3 == 0
each delay has its own block, and there are three delays

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/n_back_with_shape_matching/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'n_back_with_shape_matching_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

nback_conditions = ['match','mismatch']
delays = ['1','2','3']

shape_mismatch__nback_one_match = 0
shape_mismatch__nback_one_mismatch = 0
shape_mismatch__nback_two_match = 0
shape_mismatch__nback_two_mismatch = 0
shape_mismatch__nback_three_match = 0
shape_mismatch__nback_three_mismatch = 0

shape_match__nback_one_match = 0
shape_match__nback_one_mismatch = 0
shape_match__nback_two_match = 0
shape_match__nback_two_mismatch = 0
shape_match__nback_three_match = 0
shape_match__nback_three_mismatch = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].shape_matching_condition == 'mismatch':
        shape_mismatch__nback_one_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].shape_matching_condition == 'mismatch':
        shape_mismatch__nback_one_mismatch += 1
  
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].shape_matching_condition == 'mismatch':
        shape_mismatch__nback_two_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].shape_matching_condition == 'mismatch':
        shape_mismatch__nback_two_mismatch += 1
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].shape_matching_condition == 'mismatch':
        shape_mismatch__nback_three_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].shape_matching_condition == 'mismatch':
        shape_mismatch__nback_three_mismatch += 1
       
        
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].shape_matching_condition == 'match':
        shape_match__nback_one_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].shape_matching_condition == 'match':
        shape_match__nback_one_mismatch += 1
  
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].shape_matching_condition == 'match':
        shape_match__nback_two_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].shape_matching_condition == 'match':
        shape_match__nback_two_mismatch += 1
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].shape_matching_condition == 'match':
        shape_match__nback_three_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].shape_matching_condition == 'match':
        shape_match__nback_three_mismatch += 1
        
        
        
print("shape_mismatch__nback_one_match = " + str(shape_mismatch__nback_one_match) + " / " + str(len(test_trials)))
print("shape_mismatch__nback_one_mismatch = " + str(shape_mismatch__nback_one_mismatch) + " / " + str(len(test_trials)))
print("shape_mismatch__nback_two_match = " + str(shape_mismatch__nback_two_match) + " / " + str(len(test_trials)))
print("shape_mismatch__nback_two_mismatch = " + str(shape_mismatch__nback_two_mismatch) + " / " + str(len(test_trials)))
print("shape_mismatch__nback_three_match = " + str(shape_mismatch__nback_three_match) + " / " + str(len(test_trials)))
print("shape_mismatch__nback_three_mismatch = " + str(shape_mismatch__nback_three_mismatch) + " / " + str(len(test_trials)))


print("shape_match__nback_one_match = " + str(shape_match__nback_one_match) + " / " + str(len(test_trials)))
print("shape_match__nback_one_mismatch = " + str(shape_match__nback_one_mismatch) + " / " + str(len(test_trials)))
print("shape_match__nback_two_match = " + str(shape_match__nback_two_match) + " / " + str(len(test_trials)))
print("shape_match__nback_two_mismatch = " + str(shape_match__nback_two_mismatch) + " / " + str(len(test_trials)))
print("shape_match__nback_three_match = " + str(shape_match__nback_three_match) + " / " + str(len(test_trials)))
print("shape_match__nback_three_mismatch = " + str(shape_match__nback_three_mismatch) + " / " + str(len(test_trials)))



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