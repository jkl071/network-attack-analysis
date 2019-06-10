#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:18:49 2018

@author: jamie

go nogo single task network

go go go go nogo
5 trial types

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'go_nogo_single_task_network_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

go_nogo_conditions = ['go','nogo']

go = 0
nogo = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].go_nogo_condition == 'go':
        go += 1
    
    elif test_trials.iloc[row].go_nogo_condition == 'nogo':
        nogo += 1
   
        
        

        
        
print("go = " + str(go) + " / " + str(len(test_trials)))
print("nogo = " + str(nogo) + " / " + str(len(test_trials)))




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