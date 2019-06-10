#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:53:49 2018

@author: jamie

predictable task switching single task

task: switch vs stay
task: magnitude vs parity
full counterbalancing
1 throwaway trial per block of trials

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/predictable_task_switching_single_task_network/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'predictable_task_switching_single_task_network_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

predictive_stay__dim_mag = 0 
predictive_stay__dim_par = 0
predictive_switch__dim_mag = 0
predictive_switch__dim_par = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].predictive_condition == "stay" and test_trials.iloc[row].predictive_dimension == "magnitude":
        predictive_stay__dim_mag += 1
    
    elif test_trials.iloc[row].predictive_condition == "stay" and test_trials.iloc[row].predictive_dimension == "parity":
        predictive_stay__dim_par += 1
    
    elif test_trials.iloc[row].predictive_condition == "switch" and test_trials.iloc[row].predictive_dimension == "magnitude":
        predictive_switch__dim_mag += 1
    
    elif test_trials.iloc[row].predictive_condition == "switch" and test_trials.iloc[row].predictive_dimension == "parity":
        predictive_switch__dim_par += 1

        
        
print("predictive_stay__dim_mag = " + str(predictive_stay__dim_mag) + " / " + str(len(test_trials)))
print("predictive_stay__dim_par = " + str(predictive_stay__dim_par) + " / " + str(len(test_trials))) 

print("predictive_switch__dim_mag = " + str(predictive_switch__dim_mag) + " / " + str(len(test_trials)))
print("predictive_switch__dim_par = " + str(predictive_switch__dim_par) + " / " + str(len(test_trials))) 


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