#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:07:51 2018

@author: jamie

shape_matching_with_predictable_task_switching

shape_matching_conditions = ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']
predictable_task_switching_conditions = ['congruent','incongruent']

280 trials total, 56 trials per block, 5 blocks
lowest counterbalance = 14
full counterbalancing

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'shape_matching_with_predictable_task_switching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

shape_matching_conditions = ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']

switch__DDD = 0
switch__SDD = 0
switch__DSD = 0
switch__DDS = 0
switch__SSS = 0
switch__SNN = 0
switch__DNN = 0

stay__DDD = 0
stay__SDD = 0
stay__DSD = 0
stay__DDS = 0
stay__SSS = 0
stay__SNN = 0
stay__DNN = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].shape_matching_condition == 'DDD' and test_trials.iloc[row].predictive_condition == 'switch' :
        switch__DDD += 1
    
    elif test_trials.iloc[row].shape_matching_condition == 'SDD' and test_trials.iloc[row].predictive_condition == 'switch':
        switch__SDD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DSD' and test_trials.iloc[row].predictive_condition == 'switch':
        switch__DSD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDS' and test_trials.iloc[row].predictive_condition == 'switch':
        switch__DDS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SSS' and test_trials.iloc[row].predictive_condition == 'switch':
        switch__SSS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SNN' and test_trials.iloc[row].predictive_condition == 'switch':
        switch__SNN += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DNN' and test_trials.iloc[row].predictive_condition == 'switch':
        switch__DNN += 1
        
    
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDD' and test_trials.iloc[row].predictive_condition == 'stay':
        stay__DDD += 1
    
    elif test_trials.iloc[row].shape_matching_condition == 'SDD' and test_trials.iloc[row].predictive_condition == 'stay':
        stay__SDD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DSD' and test_trials.iloc[row].predictive_condition == 'stay':
        stay__DSD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDS' and test_trials.iloc[row].predictive_condition == 'stay':
        stay__DDS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SSS' and test_trials.iloc[row].predictive_condition == 'stay':
        stay__SSS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SNN' and test_trials.iloc[row].predictive_condition == 'stay':
        stay__SNN += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DNN' and test_trials.iloc[row].predictive_condition == 'stay':
        stay__DNN += 1
        

        
        
print("switch__DDD = " + str(switch__DDD) + " / " + str(len(test_trials)))
print("switch__SDD = " + str(switch__SDD) + " / " + str(len(test_trials)))
print("switch__DSD = " + str(switch__DSD) + " / " + str(len(test_trials)))
print("switch__DDS = " + str(switch__DDS) + " / " + str(len(test_trials)))
print("switch__SSS = " + str(switch__SSS) + " / " + str(len(test_trials)))
print("switch__SNN = " + str(switch__SNN) + " / " + str(len(test_trials)))
print("switch__DNN = " + str(switch__DNN) + " / " + str(len(test_trials)))

print("stay__DDD = " + str(stay__DDD) + " / " + str(len(test_trials)))
print("stay__SDD = " + str(stay__SDD) + " / " + str(len(test_trials)))
print("stay__DSD = " + str(stay__DSD) + " / " + str(len(test_trials)))
print("stay__DDS = " + str(stay__DDS) + " / " + str(len(test_trials)))
print("stay__SSS = " + str(stay__SSS) + " / " + str(len(test_trials)))
print("stay__SNN = " + str(stay__SNN) + " / " + str(len(test_trials)))
print("stay__DNN = " + str(stay__DNN) + " / " + str(len(test_trials)))




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