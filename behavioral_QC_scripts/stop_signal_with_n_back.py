#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:02:47 2018

@author: jamie

stop_signal_with_n_back

SS: go, go, stop
N-Back: mismatch, mismatch, mismatch, mismatch, match
delays - 1,2,3

270 total trials, 45 trials per block, 6 blocks
15 minimum trials
full counterbalancing
note: this nback must have blocks % 3 == 0, need equal amount of blocks per delay
"""



import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'stop_signal_with_n_back_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

nback_conditions = ['match','mismatch']
delays = ['1','2','3']

SS_stop__one_match = 0
SS_stop__one_mismatch = 0
SS_stop__two_match = 0
SS_stop__two_mismatch = 0
SS_stop__three_match = 0
SS_stop__three_mismatch = 0

SS_go__one_match = 0
SS_go__one_mismatch = 0
SS_go__two_match = 0
SS_go__two_mismatch = 0
SS_go__three_match = 0
SS_go__three_mismatch = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__one_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__one_mismatch += 1
  
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__two_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__two_mismatch += 1
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__three_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__three_mismatch += 1
        
        
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__one_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 1 and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__one_mismatch += 1
  
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__two_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 2 and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__two_mismatch += 1
        
    elif test_trials.iloc[row].n_back_condition == 'match' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__three_match += 1
        
    elif test_trials.iloc[row].n_back_condition == 'mismatch' and test_trials.iloc[row].delay == 3 and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__three_mismatch += 1
        
        
print("SS_stop__one_match = " + str(SS_stop__one_match) + " / " + str(len(test_trials)))
print("SS_stop__one_mismatch = " + str(SS_stop__one_mismatch) + " / " + str(len(test_trials)))
print("SS_stop__two_match = " + str(SS_stop__two_match) + " / " + str(len(test_trials)))
print("SS_stop__two_mismatch = " + str(SS_stop__two_mismatch) + " / " + str(len(test_trials)))
print("SS_stop__three_match = " + str(SS_stop__three_match) + " / " + str(len(test_trials)))
print("SS_stop__three_mismatch = " + str(SS_stop__three_mismatch) + " / " + str(len(test_trials)))

print("SS_go__one_match = " + str(SS_go__one_match) + " / " + str(len(test_trials)))
print("SS_go__one_mismatch = " + str(SS_go__one_mismatch) + " / " + str(len(test_trials)))
print("SS_go__two_match = " + str(SS_go__two_match) + " / " + str(len(test_trials)))
print("SS_go__two_mismatch = " + str(SS_go__two_mismatch) + " / " + str(len(test_trials)))
print("SS_go__three_match = " + str(SS_go__three_match) + " / " + str(len(test_trials)))
print("SS_go__three_mismatch = " + str(SS_go__three_mismatch) + " / " + str(len(test_trials)))



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