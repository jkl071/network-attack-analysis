#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:53:37 2018

@author: jamie

stop_signal_with_directed_forgetting
SS: go, go, stop
Directed: ['pos', 'pos', 'neg', 'con']

180 total trials, 36 trials per block, 5 blocks
full counterbalancing
12 minimum trials
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'stop_signal_with_directed_forgetting_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

directed_forgetting_conditions = ['pos','pos','con','neg']

SS_stop__pos = 0
SS_stop__con = 0
SS_stop__neg = 0

SS_go__pos = 0
SS_go__con = 0
SS_go__neg = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].directed_forgetting_condition == 'pos' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__neg += 1
        
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'pos' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__neg += 1
        
        
print("SS_stop__pos = " + str(SS_stop__pos) + " / " + str(len(test_trials)))
print("SS_stop__con = " + str(SS_stop__con) + " / " + str(len(test_trials)))
print("SS_stop__neg = " + str(SS_stop__neg) + " / " + str(len(test_trials)))

print("SS_go__pos = " + str(SS_go__pos) + " / " + str(len(test_trials)))
print("SS_go__con = " + str(SS_go__con) + " / " + str(len(test_trials)))
print("SS_go__neg = " + str(SS_go__neg) + " / " + str(len(test_trials)))


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