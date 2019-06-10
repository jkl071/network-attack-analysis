#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:47:55 2018

@author: jamie

go_nogo_with_n_back

GNG: ['go','go','go','go','nogo']
N-Back: ['match','mismatch','mismatch','mismatch','mismatch']
    delay = 1,2,3

25 - minimum number of trials
300 total trials, 50 each block, 6 blocks
note: this nback must have block % 2 == 0, since we want an equal number of blocks per delay
each delay has 2 blocks, each block only has 1 delay
"""


import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/go_nogo_with_n_back/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'go_nogo_with_n_back_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice


delay_1__gng_go__match = 0
delay_1__gng_go__mismatch = 0
delay_1__gng_nogo__match = 0
delay_1__gng_nogo__mismatch = 0

delay_2__gng_go__match = 0
delay_2__gng_go__mismatch = 0
delay_2__gng_nogo__match = 0
delay_2__gng_nogo__mismatch = 0

delay_3__gng_go__match = 0
delay_3__gng_go__mismatch = 0
delay_3__gng_nogo__match = 0
delay_3__gng_nogo__mismatch = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].go_nogo_condition == 'go' and test_trials.iloc[row].delay == 1:
        delay_1__gng_go__match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].go_nogo_condition == 'go' and test_trials.iloc[row].delay == 1:
        delay_1__gng_go__mismatch += 1
          
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].go_nogo_condition == 'nogo' and test_trials.iloc[row].delay == 1:
        delay_1__gng_nogo__match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].go_nogo_condition == 'nogo' and test_trials.iloc[row].delay == 1:
        delay_1__gng_nogo__mismatch += 1
  
        
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].go_nogo_condition == 'go' and test_trials.iloc[row].delay == 2:
        delay_2__gng_go__match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].go_nogo_condition == 'go' and test_trials.iloc[row].delay == 2:
        delay_2__gng_go__mismatch += 1
          
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].go_nogo_condition == 'nogo' and test_trials.iloc[row].delay == 2:
        delay_2__gng_nogo__match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].go_nogo_condition == 'nogo' and test_trials.iloc[row].delay == 2:
        delay_2__gng_nogo__mismatch += 1
        
        
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].go_nogo_condition == 'go' and test_trials.iloc[row].delay == 3:
        delay_3__gng_go__match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].go_nogo_condition == 'go' and test_trials.iloc[row].delay == 3:
        delay_3__gng_go__mismatch += 1
          
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].go_nogo_condition == 'nogo' and test_trials.iloc[row].delay == 3:
        delay_3__gng_nogo__match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].go_nogo_condition == 'nogo' and test_trials.iloc[row].delay == 3:
        delay_3__gng_nogo__mismatch += 1
        
        
print("delay_1__gng_go__match = " + str(delay_1__gng_go__match) + " / " + str(len(test_trials)))
print("delay_1__gng_go__mismatch = " + str(delay_1__gng_go__mismatch) + " / " + str(len(test_trials)))
print("delay_1__gng_nogo__match = " + str(delay_1__gng_nogo__match) + " / " + str(len(test_trials)))
print("delay_1__gng_nogo__mismatch = " + str(delay_1__gng_nogo__mismatch) + " / " + str(len(test_trials)))

print("delay_2__gng_go__match = " + str(delay_2__gng_go__match) + " / " + str(len(test_trials)))
print("delay_2__gng_go__mismatch = " + str(delay_2__gng_go__mismatch) + " / " + str(len(test_trials)))
print("delay_2__gng_nogo__match = " + str(delay_2__gng_nogo__match) + " / " + str(len(test_trials)))
print("delay_2__gng_nogo__mismatch = " + str(delay_2__gng_nogo__mismatch) + " / " + str(len(test_trials)))

print("delay_3__gng_go__match = " + str(delay_3__gng_go__match) + " / " + str(len(test_trials)))
print("delay_3__gng_go__mismatch = " + str(delay_3__gng_go__mismatch) + " / " + str(len(test_trials)))
print("delay_3__gng_nogo__match = " + str(delay_3__gng_nogo__match) + " / " + str(len(test_trials)))
print("delay_3__gng_nogo__mismatch = " + str(delay_3__gng_nogo__mismatch) + " / " + str(len(test_trials)))


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

