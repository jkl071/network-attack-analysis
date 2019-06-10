#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:12:34 2018

@author: jamie

shape_matching_single_task_network

shape_matching_with_two_by_two
shape_matching_conditions = ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']

5 blocks of 49 trials, 245 total.  
lowest counterbalance = 7
full counterbalancing
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/shape_matching_single_task_network/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'shape_matching_single_task_network_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

shape_matching_conditions = ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']

DDD = 0
SDD = 0
DSD = 0
DDS = 0
SSS = 0
SNN = 0
DNN = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].shape_matching_condition == 'DDD':
        DDD += 1
    
    elif test_trials.iloc[row].shape_matching_condition == 'SDD':
        SDD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DSD':
        DSD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDS':
        DDS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SSS':
        SSS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SNN':
        SNN += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DNN':
        DNN += 1
        
        

        
        
print("DDD = " + str(DDD) + " / " + str(len(test_trials)))
print("SDD = " + str(SDD) + " / " + str(len(test_trials)))
print("DSD = " + str(DSD) + " / " + str(len(test_trials)))
print("DDS = " + str(DDS) + " / " + str(len(test_trials)))
print("SSS = " + str(SSS) + " / " + str(len(test_trials)))
print("SNN = " + str(SNN) + " / " + str(len(test_trials)))
print("DNN = " + str(DNN) + " / " + str(len(test_trials)))




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