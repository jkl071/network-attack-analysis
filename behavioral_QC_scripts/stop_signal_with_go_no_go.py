#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:47:39 2018

@author: jamie

stop_signal_with_go_no_go

SS: go, go, stop
GNG: go, go, go, go, nogo

300 total trials, 60 trials per block, 5 blocks tota
15 trials minimum
full counterbalancing

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'stop_signal_with_go_no_go_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice


SS_go__go = 0
SS_go__nogo = 0

SS_nogo__go = 0
SS_nogo__nogo = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].go_nogo_condition == 'go' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__go += 1
    
    elif test_trials.iloc[row].go_nogo_condition == 'nogo' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__nogo += 1
        
        
    elif test_trials.iloc[row].go_nogo_condition == 'go' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_nogo__go += 1
    
    elif test_trials.iloc[row].go_nogo_condition == 'nogo' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_nogo__nogo += 1
   
        
        

        
        
print("SS_go__go = " + str(SS_go__go) + " / " + str(len(test_trials)))
print("SS_go__nogo = " + str(SS_go__nogo) + " / " + str(len(test_trials)))

print("SS_nogo__go = " + str(SS_nogo__go) + " / " + str(len(test_trials)))
print("SS_nogo__nogo = " + str(SS_nogo__nogo) + " / " + str(len(test_trials)))




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